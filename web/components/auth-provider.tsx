// Who is logged in, shared across every page.
//
// WHY THREE STATES: the session lives in an httpOnly cookie that JavaScript
// can't read, so on first load we genuinely don't know yet whether someone is
// logged in — we have to ask the API (GET /api/auth/session). Until it answers
// the state is "loading", and pages show a skeleton instead of flashing the
// login page at someone who is in fact logged in. A page refresh no longer logs
// anyone out: the cookie survives it, and /session re-reads the profile.
//
// TWO KINDS OF ACCOUNT: a student or a teacher (2026-10-02). `role` says which,
// and exactly one of `student` / `teacher` is set when authenticated. Each set
// of pages guards for its own role (RequireAuth), and the API enforces the same
// split on every request, so this is about showing the right screens, not
// security.

"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";

import {
  getSession,
  login as apiLogin,
  logout as apiLogout,
  register as apiRegister,
  setUnauthorizedHandler,
  teacherLogin as apiTeacherLogin,
  type RegisterInput,
  type Session,
  type StudentProfile,
  type TeacherProfile,
} from "@/lib/api";

export type AuthStatus = "loading" | "authenticated" | "unauthenticated";
export type Role = Session["role"];

// Where each kind of account lands after logging in.
export const HOME: Record<Role, string> = { student: "/roadmap", teacher: "/teacher" };

interface AuthContextValue {
  status: AuthStatus;
  role: Role | null;
  student: StudentProfile | null;
  teacher: TeacherProfile | null;
  login: (username: string, password: string) => Promise<StudentProfile>;
  teacherLogin: (username: string, password: string) => Promise<TeacherProfile>;
  register: (input: RegisterInput) => Promise<StudentProfile>;
  logout: () => Promise<void>;
  // True after the user pressed "Log out" (as opposed to a session that
  // expired): the route guard then sends them to the plain login page instead
  // of "log in to come back here", which would hand the next person on a
  // shared classroom computer the previous student's page.
  loggedOutOnPurpose: boolean;
  // After PATCH /api/profile, store the returned profile.
  setStudent: (student: StudentProfile) => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [session, setSession] = useState<Session | null>(null);
  const [status, setStatus] = useState<AuthStatus>("loading");
  const [loggedOutOnPurpose, setLoggedOutOnPurpose] = useState(false);

  const signedIn = useCallback((next: Session) => {
    setSession(next);
    setStatus("authenticated");
    setLoggedOutOnPurpose(false);
  }, []);

  const signedOut = useCallback(() => {
    setSession(null);
    setStatus("unauthenticated");
  }, []);

  // Hydrate once on mount: is there a valid session cookie, and whose?
  useEffect(() => {
    getSession().then(signedIn, signedOut);
  }, [signedIn, signedOut]);

  // Any request that comes back 401 later (expired cookie) signs the user out;
  // the route guard then sends them to the right login page.
  useEffect(() => {
    setUnauthorizedHandler(signedOut);
    return () => setUnauthorizedHandler(null);
  }, [signedOut]);

  const value = useMemo<AuthContextValue>(() => {
    const asStudent = (profile: StudentProfile) => {
      signedIn({ role: "student", profile });
      return profile;
    };
    const asTeacher = (profile: TeacherProfile) => {
      signedIn({ role: "teacher", profile });
      return profile;
    };
    return {
      status,
      role: session?.role ?? null,
      student: session?.role === "student" ? session.profile : null,
      teacher: session?.role === "teacher" ? session.profile : null,
      login: (username, password) => apiLogin(username, password).then(asStudent),
      teacherLogin: (username, password) => apiTeacherLogin(username, password).then(asTeacher),
      register: (input) => apiRegister(input).then(asStudent),
      loggedOutOnPurpose,
      logout: async () => {
        try {
          await apiLogout();
        } finally {
          setLoggedOutOnPurpose(true);
          signedOut(); // even if the network call fails, forget the user locally
        }
      },
      setStudent: (profile) => {
        asStudent(profile);
      },
    };
  }, [status, session, signedIn, signedOut, loggedOutOnPurpose]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside <AuthProvider>");
  return ctx;
}

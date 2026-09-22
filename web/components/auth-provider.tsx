// Who is logged in, shared across every page.
//
// WHY THREE STATES: the session lives in an httpOnly cookie that JavaScript
// can't read, so on first load we genuinely don't know yet whether someone is
// logged in — we have to ask the API (GET /api/auth/me). Until it answers the
// state is "loading", and pages show a skeleton instead of flashing the login
// page at a student who is in fact logged in. A page refresh no longer logs
// anyone out: the cookie survives it, and /me re-reads the profile.

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
  getMe,
  login as apiLogin,
  logout as apiLogout,
  register as apiRegister,
  setUnauthorizedHandler,
  type RegisterInput,
  type StudentProfile,
} from "@/lib/api";

export type AuthStatus = "loading" | "authenticated" | "unauthenticated";

interface AuthContextValue {
  status: AuthStatus;
  student: StudentProfile | null;
  login: (username: string, password: string) => Promise<StudentProfile>;
  register: (input: RegisterInput) => Promise<StudentProfile>;
  logout: () => Promise<void>;
  // After PATCH /api/profile, store the returned profile.
  setStudent: (student: StudentProfile) => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [student, setStudentState] = useState<StudentProfile | null>(null);
  const [status, setStatus] = useState<AuthStatus>("loading");

  const signedIn = useCallback((profile: StudentProfile) => {
    setStudentState(profile);
    setStatus("authenticated");
    return profile;
  }, []);

  const signedOut = useCallback(() => {
    setStudentState(null);
    setStatus("unauthenticated");
  }, []);

  // Hydrate once on mount: is there a valid session cookie?
  useEffect(() => {
    getMe().then(signedIn, signedOut);
  }, [signedIn, signedOut]);

  // Any request that comes back 401 later (expired cookie) signs the user out;
  // the route guard then sends them to /login.
  useEffect(() => {
    setUnauthorizedHandler(signedOut);
    return () => setUnauthorizedHandler(null);
  }, [signedOut]);

  const value = useMemo<AuthContextValue>(
    () => ({
      status,
      student,
      login: (username, password) => apiLogin(username, password).then(signedIn),
      register: (input) => apiRegister(input).then(signedIn),
      logout: async () => {
        try {
          await apiLogout();
        } finally {
          signedOut(); // even if the network call fails, forget the user locally
        }
      },
      setStudent: signedIn,
    }),
    [status, student, signedIn, signedOut],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside <AuthProvider>");
  return ctx;
}

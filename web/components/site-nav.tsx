// The top navigation bar, shown on every page (rendered once in the root
// layout). Brand lockup on the left; on the right, what depends on who's here:
// logged out → Log in + Get Started; a student → My path, Mix-ups, Review,
// Settings, their avatar and Log out; a teacher → Classes, Account, avatar and
// Log out. On phones the links move to a bottom bar (the house style's mobile
// nav). A Client Component because it reads the auth state. Hidden when
// printing, so a teacher's printed sign-in slips are just the slips.

"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { BookOpen, Target, Trophy, UserRound, Users } from "lucide-react";

import { HOME, useAuth } from "@/components/auth-provider";
import { ThemeToggle } from "@/components/theme-toggle";
import { Button } from "@/components/ui/button";

const STUDENT_LINKS = [
  { href: "/roadmap", label: "My path", icon: Target },
  { href: "/mix-ups", label: "Mix-ups", icon: BookOpen },
  { href: "/review", label: "Review", icon: Trophy },
  { href: "/settings", label: "Settings", icon: UserRound },
];
const TEACHER_LINKS = [
  { href: "/teacher", label: "Classes", icon: Users },
  { href: "/teacher/account", label: "Account", icon: UserRound },
];

export function SiteNav() {
  const { status, role, student, teacher, logout } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  async function handleLogout() {
    const wasTeacher = role === "teacher";
    await logout();
    router.replace(wasTeacher ? "/teacher/login" : "/login");
  }

  const name = student?.name ?? teacher?.name;
  const links = role === "teacher" ? TEACHER_LINKS : STUDENT_LINKS;
  const isHere = (href: string) =>
    pathname === href || (href !== "/teacher" && pathname.startsWith(`${href}/`));

  return (
    <>
      <header className="topbar sticky top-0 print:hidden">
        <Link
          href={status === "authenticated" && role ? HOME[role] : "/"}
          className="brand-lockup"
        >
          <span className="brand-mark" aria-hidden>
            e
          </span>
          <span>
            ecolearn<span className="brand-period">.</span>
          </span>
        </Link>

        {/* Nothing while loading, so logged-in users never see a flash of "Log in". */}
        {status === "authenticated" && name && (
          <>
            <nav className="desktop-nav" aria-label="Main navigation">
              {links.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="nav-link"
                  aria-current={isHere(item.href) ? "page" : undefined}
                >
                  <item.icon size={16} aria-hidden />
                  {item.label}
                </Link>
              ))}
            </nav>
            <div className="top-actions">
              <ThemeToggle />
              <Link
                href={role === "teacher" ? "/teacher/account" : "/settings"}
                className="avatar"
                aria-label={`${name}: your account`}
                title={name}
              >
                {name.slice(0, 1).toUpperCase()}
              </Link>
              <Button variant="outline" size="sm" onClick={handleLogout}>
                Log out
              </Button>
            </div>
          </>
        )}
        {status === "unauthenticated" && (
          <div className="top-actions">
            <ThemeToggle />
            <Button variant="ghost" size="sm" asChild>
              <Link href="/login">Log in</Link>
            </Button>
            <Button size="sm" asChild>
              <Link href="/signup">Get started</Link>
            </Button>
          </div>
        )}
      </header>

      {status === "authenticated" && name && (
        <nav className="mobile-nav print:hidden" aria-label="Main navigation">
          {links.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="mobile-nav-item"
              aria-current={isHere(item.href) ? "page" : undefined}
            >
              <item.icon size={18} aria-hidden />
              <span>{item.label}</span>
            </Link>
          ))}
        </nav>
      )}
    </>
  );
}

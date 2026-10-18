"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState, type CSSProperties, type ReactNode } from "react";
import { ArrowRight, BookOpen, Moon, Sun, Target, Trophy, UserRound } from "lucide-react";
import * as api from "@/lib/api";

export const interestsUI = [
  { id:"cricket", name:"Cricket", emoji:"🏏", color:"#efb45b", hint:"Spin, swing & sixes" },
  { id:"football", name:"Football", emoji:"⚽", color:"#84be89", hint:"Curves & kicks" },
  { id:"gaming", name:"Gaming", emoji:"🎮", color:"#bd9ce2", hint:"Power up your brain" },
  { id:"smartphones", name:"Smartphones", emoji:"📱", color:"#78b9c7", hint:"The science in your pocket" },
  { id:"motorsport", name:"Motorsport", emoji:"🏎️", color:"#eb9170", hint:"Fast cars, real forces" },
];

export function ThemeToggle() {
  const [dark, setDark] = useState(true);
  useEffect(() => {
    const saved = localStorage.getItem("ecolearn-theme");
    const isDark = saved !== "light";
    document.documentElement.classList.toggle("dark", isDark);
    setDark(isDark);
  }, []);
  function toggle() {
    const next = !dark;
    setDark(next);
    document.documentElement.classList.toggle("dark", next);
    localStorage.setItem("ecolearn-theme", next ? "dark" : "light");
  }
  return <button className="theme-toggle" aria-label={`Switch to ${dark ? "light" : "dark"} theme`} onClick={toggle}>{dark ? <Sun size={17}/> : <Moon size={17}/>}</button>;
}

const nav = [
  { href:"/roadmap", label:"My path", icon:Target },
  { href:"/mix-ups", label:"Mix-ups", icon:BookOpen },
  { href:"/review", label:"Review", icon:Trophy },
  { href:"/settings", label:"Settings", icon:UserRound },
];

export function AppFrame({ children }: { children: ReactNode }) {
  const pathname=usePathname();
  const [studentName,setStudentName]=useState("Aarav");
  useEffect(() => { api.getMe().then(profile => { document.documentElement.dataset.interest = profile.interest; setStudentName(profile.name); }).catch(() => {}); }, [pathname]);
  return <div className="app-frame">
    <header className="topbar">
      <Link href="/" className="brand-lockup"><span className="brand-mark">e</span><span>ecolearn<span className="brand-period">.</span></span></Link>
      <nav className="desktop-nav" aria-label="Main navigation">{nav.map(item=><Link key={item.href} href={item.href} className="nav-link"><item.icon size={16}/>{item.label}</Link>)}<Link href="/teacher" className="nav-link teacher-link">Teacher view <ArrowRight size={14}/></Link></nav>
      <div className="top-actions"><ThemeToggle/><Link href="/settings" className="avatar" aria-label={`${studentName}'s settings`}>{studentName.slice(0,1).toUpperCase()}</Link></div>
    </header>
    <main>{children}</main>
    <nav className="mobile-nav" aria-label="Student navigation">{nav.slice(0,4).map(item=><Link key={item.href} href={item.href} className="mobile-nav-item"><item.icon size={18}/><span>{item.label}</span></Link>)}</nav>
  </div>;
}

export function PageHeading({ eyebrow, title, description, action }: { eyebrow?:string; title:string; description?:string; action?:ReactNode }) {
  return <div className="page-heading fade-up"><div>{eyebrow&&<p className="eyebrow">{eyebrow}</p>}<h1 className="display">{title}</h1>{description&&<p className="heading-description">{description}</p>}</div>{action}</div>;
}
export function Button({ children, href, variant="", onClick, disabled=false, type="button", className="" }: {children:ReactNode;href?:string;variant?:string;onClick?:()=>void;disabled?:boolean;type?:"button"|"submit";className?:string}) {
  const cls=`button ${variant} ${className}`.trim();
  return href?<Link href={href} className={cls}>{children}</Link>:<button type={type} className={cls} onClick={onClick} disabled={disabled}>{children}</button>;
}
export function Panel({ children, className="" }: {children:ReactNode;className?:string}) { return <section className={`surface panel ${className}`}>{children}</section>; }
export function Pill({ children, className="" }: {children:ReactNode;className?:string}) { return <span className={`tag ${className}`}>{children}</span>; }
export function Meter({ value, max=100, color }: {value:number;max?:number;color?:string}) { return <div className="progress-track"><div className="progress-fill" style={{width:`${Math.max(0,Math.min(100,value/max*100))}%`,background:color}}/></div>; }
export function EmptyState({ title, copy, href, action }: {title:string;copy:string;href?:string;action?:string}) { return <div className="empty-state"><span className="empty-spark">✳</span><h3>{title}</h3><p>{copy}</p>{href&&<Button href={href}>{action??"Keep going"} <ArrowRight size={16}/></Button>}</div>; }
export function Skeleton({ rows=3 }: {rows?:number}) { return <div className="skeleton-stack" aria-label="Loading"><span className="skeleton-line wide"/>{Array.from({length:rows},(_,i)=><span key={i} className="skeleton-line"/>)}</div>; }
export function InterestMark({ id, large=false }: {id:string;large?:boolean}) { const item=interestsUI.find(i=>i.id===id)??interestsUI[0];return <span className={`interest-mark ${large?"large":""}`} style={{"--interest":item.color} as CSSProperties}>{item.emoji}</span>; }
export function ChoiceButton({ letter, children, selected, onClick, disabled=false }: {letter:string;children:ReactNode;selected:boolean;onClick:()=>void;disabled?:boolean}) {
 return <button disabled={disabled} onClick={onClick} className={`choice-button ${selected?"selected":""}`}><span className="choice-letter">{letter}</span><span>{children}</span>{selected&&<span className="choice-check">✓</span>}</button>;
}
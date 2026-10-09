"use client";
import { MotionConfig } from "framer-motion";
import { AppFrame } from "./ui-kit";
import { AuthScreen, LandingScreen, MixUpsScreen, RoadmapScreen, SettingsScreen, StartScreen } from "./student-screens";
import { EndCheckScreen, LessonScreen, ReviewScreen } from "./study-screens";
import { TeacherClassScreen, TeacherHomeScreen } from "./teacher-screens";

export function Experience({ page }: { page: string }) {
  let screen;
  switch (page) {
    case "/": screen = <LandingScreen/>; break;
    case "/signup": screen = <AuthScreen signup/>; break;
    case "/login": screen = <AuthScreen/>; break;
    case "/start": screen = <StartScreen/>; break;
    case "/roadmap": screen = <RoadmapScreen/>; break;
    case "/lesson": screen = <LessonScreen/>; break;
    case "/mix-ups": screen = <MixUpsScreen/>; break;
    case "/review": screen = <ReviewScreen/>; break;
    case "/end-check": screen = <EndCheckScreen/>; break;
    case "/settings": screen = <SettingsScreen/>; break;
    case "/teacher": screen = <TeacherHomeScreen/>; break;
    case "/teacher/class": screen = <TeacherClassScreen/>; break;
    default: screen = <LandingScreen/>;
  }
  return <MotionConfig reducedMotion="user"><AppFrame>{screen}</AppFrame></MotionConfig>;
}
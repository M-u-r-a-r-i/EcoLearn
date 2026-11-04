// Fonts for the three preview directions, loaded with next/font (self-hosted
// at build time, nothing fetched from Google by the visitor's browser).
import type { Metadata } from "next";
import {
  Barlow,
  Barlow_Condensed,
  Fraunces,
  Fredoka,
  JetBrains_Mono,
  Nunito,
  Source_Sans_3,
} from "next/font/google";

export const metadata: Metadata = { title: "EcoLearn design previews" };

const aDisplay = Fredoka({ variable: "--f-a-display", subsets: ["latin"], weight: ["500", "600", "700"] });
const aBody = Nunito({ variable: "--f-a-body", subsets: ["latin"], weight: ["400", "600", "700", "800"] });
const bDisplay = Fraunces({ variable: "--f-b-display", subsets: ["latin"], axes: ["opsz"] });
const bBody = Source_Sans_3({ variable: "--f-b-body", subsets: ["latin"], weight: ["400", "600", "700"] });
const cDisplay = Barlow_Condensed({ variable: "--f-c-display", subsets: ["latin"], weight: ["600", "700", "800"], style: ["normal", "italic"] });
const cBody = Barlow({ variable: "--f-c-body", subsets: ["latin"], weight: ["400", "500", "600"] });
const cMono = JetBrains_Mono({ variable: "--f-c-mono", subsets: ["latin"], weight: ["500", "700"] });

export default function PreviewLayout({ children }: { children: React.ReactNode }) {
  const vars = [aDisplay, aBody, bDisplay, bBody, cDisplay, cBody, cMono].map((f) => f.variable).join(" ");
  return <div className={vars}>{children}</div>;
}

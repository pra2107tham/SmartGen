"use client";
import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { useState } from 'react';
import { SparklesCore } from "@/components/ui/sparkles";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});


import SessionProvider from "@/app/utils/SessionProvider";

export default function RootLayout({
  children,
  session,
}: Readonly<{
  children: React.ReactNode;
  session: any
}>) {
  const [isDarkMode, setIsDarkMode] = useState(true);
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased relative bg-black flex flex-col items-center justify-center overflow-hidden`}
      >
        <SessionProvider session={session}>
        <div className={isDarkMode ? 'dark' : ''}>
          <div className="w-full absolute inset-0 h-screen">
            <SparklesCore
              id="tsparticlesfullpage"
              background="transparent"
              minSize={0.6}
              maxSize={1.4}
              particleDensity={20}
              className="w-full h-full"
              particleColor="#FFFFFF"
            />
          </div>
          <div className="relative z-20">
            {children}
          </div>
        </div>
        </SessionProvider> 
      </body>
    </html>
  );
}

import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Sparkles from "../app/Components/SparklesCore"
import { getServerSession  } from "next-auth";
import SessionProvider from "@/app/utils/SessionProvider";
import { Toaster } from "@/components/ui/toaster"

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

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  const session = await getServerSession();
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased relative bg-black flex flex-col items-center justify-center overflow-hidden`}
      >
        <SessionProvider session={session}>
        <div className={'dark'}>
          <div className="w-full absolute inset-0 h-screen">
           <Sparkles /> 
          </div>
          <div className="relative z-20">
            {children}
          </div>
          <Toaster />
        </div>
        </SessionProvider> 
      </body>
    </html>
  );
}

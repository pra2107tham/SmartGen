"use client"
import React from "react";
import Image from "next/image";
import { Navbar } from "./Components/Navbar";
import { HoveredLink} from "../components/ui/navbar-menu";
import { Cover } from "@/components/ui/cover";
import { useSession } from "next-auth/react";

export default function Home() {
  const menuItems = [
    {
      item: "Services",
      content: (
        <div className="flex flex-col space-y-4 text-sm">
          <HoveredLink href="/instagram-integration">
            Instagram Integration
          </HoveredLink>
          <HoveredLink href="/product-extraction">
            Product Data Extraction
          </HoveredLink>
          <HoveredLink href="/seo-optimization">
            SEO Optimization
          </HoveredLink>
          <HoveredLink href="/amazon-compliance">
            Amazon Compliance Checks
          </HoveredLink>
        </div>
      ),
    },
    {
      item: "Sign Up",
      content: (
        <div className="flex flex-col space-y-4 text-sm">
          <HoveredLink href="/signup">Create Your Account</HoveredLink>
        </div>
      ),
    },
    {
      item: "Login",
      content: (
        <div className="flex flex-col space-y-4 text-sm">
          <HoveredLink href="/login">Access Your Account</HoveredLink>
        </div>
      ),
    },
  ];

  return (
      <div className="relative bg-transparent">
        <Navbar className="top-2" menuItems={menuItems} darkMode={true} />
        <div className="h-screen flex flex-col items-center justify-center">
          <h1 className="md:text-7xl text-3xl lg:text-8xl font-bold text-center text-white">
            SmartGen
          </h1>
          <h2 className="text-4xl md:text-4xl lg:text-6xl font-semibold max-w-7xl mx-auto text-center mt-6 relative z-20 py-6 bg-clip-text text-transparent bg-gradient-to-b from-neutral-800 via-neutral-700 to-neutral-700 dark:from-neutral-800 dark:via-white dark:to-white">
            One Stop Social Media-to-Ecommerce <Cover>Transformation</Cover> Hub
          </h2>
        </div>
        {/* Content can be added here */}
      </div>
  );
}

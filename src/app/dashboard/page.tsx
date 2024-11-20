"use client";
import React, { useEffect } from "react";
import {Navbar} from '@/app/Components/Navbar'; // Adjust the import path as necessary
import { signOut, useSession } from 'next-auth/react';
import { HoveredLink, ProductItem } from '@/components/ui/navbar-menu';
import { redirect } from "next/navigation";

const DashboardPage: React.FC = () => {
    let session = useSession();
    useEffect(() => {
        console.log(session);
        if(session.status == "unauthenticated"){
            redirect("/login");
        }
    },[session])
    const menuItems: { item: string, content: React.ReactNode }[] = [
        {
          item: "Services",
          content: (
            <div className="flex flex-col space-y-4 text-sm">
              <HoveredLink href="/web-dev">Web Development</HoveredLink>
              <HoveredLink href="/interface-design">Interface Design</HoveredLink>
              <HoveredLink href="/seo">Search Engine Optimization</HoveredLink>
              <HoveredLink href="/branding">Branding</HoveredLink>
            </div>
          ),
        },
        {
          item: "Products",
          content: (
            <div className="text-sm grid grid-cols-2 gap-10 p-4">
              <ProductItem
                title="Algochurn"
                href="https://algochurn.com"
                src="https://assets.aceternity.com/demos/algochurn.webp"
                description="Prepare for tech interviews like never before."
              />
              <ProductItem
                title="Tailwind Master Kit"
                href="https://tailwindmasterkit.com"
                src="https://assets.aceternity.com/demos/tailwindmasterkit.webp"
                description="Production ready Tailwind css components for your next project"
              />
              <ProductItem
                title="Moonbeam"
                href="https://gomoonbeam.com"
                src="https://assets.aceternity.com/demos/Screenshot+2024-02-21+at+11.51.31%E2%80%AFPM.png"
                description="Never write from scratch again. Go from idea to blog in minutes."
              />
              <ProductItem
                title="Rogue"
                href="https://userogue.com"
                src="https://assets.aceternity.com/demos/Screenshot+2024-02-21+at+11.47.07%E2%80%AFPM.png"
                description="Respond to government RFPs, RFIs and RFQs 10x faster using AI"
              />
            </div>
          ),
        },
        {
          item: "Company",
          content: (
            <div className="flex flex-col space-y-4 text-sm">
              <HoveredLink href="/about">About Us</HoveredLink>
              <HoveredLink href="/careers">Careers</HoveredLink>
              <HoveredLink href="/contact">Contact Us</HoveredLink>
              <HoveredLink href="/blog">Blog</HoveredLink>
            </div>
          ),
        },
        {
          item: "Account",
          content: (
            <div className="flex flex-col space-y-4 text-sm">
              {session ? (
                <>
                  <HoveredLink href="/dashboard">Dashboard</HoveredLink>
                  <HoveredLink href="/" onClick={async () => await signOut()}>Sign Out</HoveredLink>
                </>
              ) : (
                <>
                  <HoveredLink href="/login">Login</HoveredLink>
                  <HoveredLink href="/signup">Sign Up</HoveredLink>
                </>
              )}
            </div>
          ),
        }
      ];
    
    return (
        <div>
            <Navbar menuItems={menuItems} darkMode={false} />
            <h1>Dashboard</h1>
            <p>Welcome to the dashboard!</p>
        </div>
    );
};

export default DashboardPage;
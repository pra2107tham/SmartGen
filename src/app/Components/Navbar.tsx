"use client";
import React, { useState, ReactNode } from "react";
import { HoveredLink, Menu, MenuItem, ProductItem } from "../../components/ui/navbar-menu"
import { cn } from "@/lib/utils";
import { signOut, useSession } from "next-auth/react";

interface NavbarProps {
  className?: string;
  menuItems: {
    item: string;
    content: ReactNode;
  }[];
  darkMode: boolean;
}

function Navbar({ className, menuItems, darkMode }: NavbarProps) {
  const [active, setActive] = useState<string | null>(null);
  return (
    <div
      className={cn("fixed top-10 inset-x-0 max-w-2xl mx-auto z-50", className, darkMode ? 'dark' : '')}
    >
      <Menu setActive={setActive}>
        {menuItems.map(({ item, content }) => (
          <MenuItem key={item} setActive={setActive} active={active} item={item}>
            {content}
          </MenuItem>
        ))}
      </Menu>
    </div>
  );
}

export { Navbar };

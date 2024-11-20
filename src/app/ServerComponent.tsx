// ServerComponent.tsx
import { getServerSession } from "next-auth";
import RootLayout from "@/app/layout";

export default async function ServerComponent({ children }: { children: React.ReactNode }) {
  const session = await getServerSession();
  return <RootLayout session={session}>{children}</RootLayout>;
}
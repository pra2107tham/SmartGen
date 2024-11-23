import { getSession } from 'next-auth/react';
import { redirect } from 'next/navigation';

export default async function Dashboard() {
  redirect('/dashboard/overview');
}
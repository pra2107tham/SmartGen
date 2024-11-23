import OverViewPage from './_components/overview';
import { getServerSession } from 'next-auth';
import { redirect } from 'next/navigation';

export default async function page() {
  const session = await getServerSession();
  
  if (!session) {
    redirect('/');
  }

  return <OverViewPage />;
}

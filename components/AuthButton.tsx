import { createClient } from '@/utils/supabase/server'
import Link from 'next/link'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export default async function AuthButton() {
  const cookieStore = cookies()
  const supabase = createClient(cookieStore)

  const {
    data: { user },
  } = await supabase.auth.getUser()
  let metadata = user?.user_metadata

  const signOut = async () => {
    'use server'

    const cookieStore = cookies()
    const supabase = createClient(cookieStore)
    await supabase.auth.signOut()
    return redirect('/')
  }

  return user ? (
    <div className="flex flex-row items-center gap-8 text-sm font-medium">
      {metadata && `Hello, ${metadata.first_name}!`}
      <Link
      href="/dashboard"
      className="text-sm font-medium border rounded-full py-2 px-3 text-gray-700"
    >
      dashboard
    </Link>
      
    <form action={signOut} style={{ margin: 0, padding: 0, border: 'none' }}>
      <button
      className="text-sm font-medium border rounded-full py-2 px-3 text-gray-700">
        log out
      </button>
    </form>
    
      
    </div>
  ) : (
    <Link
      href="/login"
      className="text-sm font-medium border rounded-full py-2 px-3 mx-2 text-gray-700"
    >
      log in
    </Link>
  )
}

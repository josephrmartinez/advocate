import Link from "next/link"
import { CardHeader, CardContent, Card } from "@/components/ui/card"

import Header from "@/components/Header"

export default function Component() {
  return (
    <div className="flex flex-col items-center min-h-screen bg-[#ffffff]">
      <Header/>
      
      <main className="flex-1">
        <section className="w-screen flex flex-col items-center py-12 md:py-24 lg:py-32 xl:py-48 bg-[#f7f7f7]">
        User dashboard
        </section>
          
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t bg-[#f7f7f7]">
        <p className="text-xs text-gray-500">© PatientAdvocate All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4 text-[#757575]" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4 text-[#757575]" href="#">
            Privacy
          </Link>
          <Link className="text-xs hover:underline underline-offset-4 text-[#757575]" href="#">
            Contact
          </Link>
          
        </nav>
      </footer>
    </div>
  )
}



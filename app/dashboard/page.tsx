import Link from "next/link"
import { Button } from "@/components/ui/button"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import { Avatar } from "@/components/ui/avatar"
import AuthButton from "@/components/AuthButton"

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen w-full bg-[#ffffff]">
      <header className="px-4 lg:px-6 h-16 flex items-center bg-[#f7f7f7]">
        <Link className="flex items-center justify-center" href="#">
          <HeartIcon className="h-6 w-6" />
          <span className="ml-2 text-lg font-semibold">PatientAdvocate</span>
          <span className="sr-only">PatientAdvocate</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <AuthButton/>
          
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-[#f7f7f7]">
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

function HeartIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
    </svg>
  )
}


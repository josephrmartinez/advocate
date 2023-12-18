import Link from "next/link"
import AuthButton from "./AuthButton"

export default function Header() {
  return (
    <header className="w-screen px-4 lg:px-6 h-16 flex items-center bg-[#f7f7f7]">
        <Link href="/" className="flex items-center justify-center">
          <span className="ml-2 text-lg font-semibold">PatientAdvocate</span>
          <span className="sr-only">PatientAdvocate</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <AuthButton/>
        </nav>
      </header>
  )
}

import Link from "next/link"
import Header from "@/components/Header"
import { CardTitle, CardHeader, CardContent, Card } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function Component() {
  return (
    <div className="flex flex-col items-center min-h-screen bg-[#ffffff]">
      <Header/>
      
      <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-10 w-screen">
      <div className="grid grid-cols-5 grid-rows-8 gap-4">
  
  <div className="col-span-1 row-start-2 flex flex-col">
  <button className="text-center text-lg font-bold rounded-full px-4 py-4 mb-2 hover:bg-gray-100">
    + New appointment
  </button>
   
    
          
  </div>

  
  <div className="col-start-2 col-span-4 row-span-1">
    <Input className="pl-8 my-4 h-16 w-full" placeholder="Search all appointments..." type="search" />
  </div>

  <div className="col-start-2 col-span-4 row-start-2 row-span-7">
    <Card>
            <CardHeader className="flex flex-row items-center pb-2 space-y-0">
              <CalendarIcon className="w-4 h-4 mr-4 text-gray-500 dark:text-gray-400" />
              <CardTitle className="text-sm font-medium">November 14, 2023</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex items-center justify-between py-6">
                <p className="text-lg font-semibold">Dr. Smith Intake</p>
                <Badge>Oncologist</Badge>
              </div>
              <div className="flex flex-col items-center">
                <audio className="mt-2 w-full my-4" controls src="/placeholder-audio.mp3">
                  Your browser does not support the audio element.
                </audio>
                <Input className="pl-8 my-4 w-11/12" placeholder="Search this appointment..." type="search" />
                <div className="w-11/12">
                  <a className="text-lg font-semibold text-gray-700 mt-2 underline underline-offset-4" href="#">
                    Transcript ^
                  </a>
                  <p>
                    "Looking forward to our next appointment. We will discuss the progress of your treatment and possible
                    adjustments."
                  </p>
                </div>
              </div>
              
            </CardContent>
    </Card>
  </div>
</div>
        
        
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





function BookIcon(props) {
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
      <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20" />
    </svg>
  )
}


function CalendarIcon(props) {
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
      <rect width="18" height="18" x="3" y="4" rx="2" ry="2" />
      <line x1="16" x2="16" y1="2" y2="6" />
      <line x1="8" x2="8" y1="2" y2="6" />
      <line x1="3" x2="21" y1="10" y2="10" />
    </svg>
  )
}


function PlusIcon(props) {
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
      <path d="M5 12h14" />
      <path d="M12 5v14" />
    </svg>
  )
}


function SearchIcon(props) {
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
      <circle cx="11" cy="11" r="8" />
      <path d="m21 21-4.3-4.3" />
    </svg>
  )
}

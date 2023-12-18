import Link from "next/link"
import { Button } from "@/components/ui/button"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import { Avatar } from "@/components/ui/avatar"
import AuthButton from "@/components/AuthButton"

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen bg-[#ffffff]">
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
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              
                <p className="mx-auto text-gray-600 font-bold text-5xl  dark:text-gray-400">
                Record your medical appointments. 
                </p>
                <p className="mx-auto text-gray-600  text-3xl  dark:text-gray-400">
                Get clarity, accountability, and better outcomes.
                </p>

              
              <div className="py-10">
              <Link
              href="/signup"
                className="border-2 border-green-700 text-center rounded-md px-4 py-2 text-foreground mb-2"
              >
                Get Started
              </Link>
              </div>
                
              
            </div>
          </div>
        </section>
        <section className="w-full py-12">
        <div className="container px-4 md:px-6">
        <h2 className="mb-12 text-2xl font-semibold text-center text-[#757575]">
              PatientAdvocate platform:
            </h2>
          <div className="container grid gap-6 px-4 md:px-6 lg:grid-cols-3">
            <Card>
              <CardHeader>
                <div className="flex flex-row">
                  <CheckCircleIcon className="w-6 h-6 mr-4 text-[#007bff]" />
                  <h3 className="text-xl font-medium text-[#757575]">RECORD</h3>
                </div>
                
              </CardHeader>
              <CardContent>
                <p className="text-gray-700 font-semibold text-xl mb-6">
                  Seamlessly capture your medical appointments with our easy and secure audio recording tool.  
                </p>
                <p className="text-gray-500">Automatic transcriptions of your appointment
                  recordings give you a record of exactly who said exactly what. No more missed details, no more
                  forgotten advice. Recordings are stored permanently in a secure, encrypted environment.</p>
              </CardContent>
            </Card>
            <Card>
              <CardHeader>
                <div className="flex flex-row">
                  <CheckCircleIcon className="w-6 h-6 mr-4 text-[#007bff]" />
                  <h3 className="text-xl font-medium text-[#757575]">REVIEW</h3>
                </div>
                
              </CardHeader>
              <CardContent>
                <p className="text-gray-700 font-semibold text-xl mb-6">
                Effortlessly search, review, and interact with your healthcare provider conversations.
                </p>
                <p className="text-gray-500">Access your recordings anytime from our user-friendly, private dashboard that lets you take control of your health narrative. Get recommendations of alternative approaches that may not have been highlighted during your appointments. </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <div className="flex flex-row">
                  <CheckCircleIcon className="w-6 h-6 mr-4 text-[#007bff]" />
                  <h3 className="text-xl font-medium text-[#757575]">GET ASSISTANCE</h3>
                </div>
                
              </CardHeader>
              <CardContent>
                <p className="text-gray-700 font-semibold text-xl mb-6">
                Personalized suggestions informed by the latest medical research and your appointment recordings.
                </p>
                <p className="text-gray-500">The HealthAdvocate platform helps with identifying concerns, exploring alternative approaches, and maximizing your appointment time, providing comprehensive insights for proactive healthcare management.</p>
              </CardContent>
            </Card>
            
            

          </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-[#f7f7f7]">
          <div className="container px-4 md:px-6">
            
            
          </div>
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

function BarChartIcon(props) {
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
      <line x1="12" x2="12" y1="20" y2="10" />
      <line x1="18" x2="18" y1="20" y2="4" />
      <line x1="6" x2="6" y1="20" y2="16" />
    </svg>
  )
}


function CheckCircleIcon(props) {
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
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
      <polyline points="22 4 12 14.01 9 11.01" />
    </svg>
  )
}


function FacebookIcon(props) {
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
      <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
    </svg>
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


function InstagramIcon(props) {
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
      <rect width="20" height="20" x="2" y="2" rx="5" ry="5" />
      <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
      <line x1="17.5" x2="17.51" y1="6.5" y2="6.5" />
    </svg>
  )
}


function TwitterIcon(props) {
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
      <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z" />
    </svg>
  )
}

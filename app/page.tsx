import Link from "next/link"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import Header from "@/components/Header"

export default function Component() {
  return (
    <div className="flex flex-col items-center min-h-screen bg-[#ffffff]">
      <Header />

      <main className="flex-1">
        <section className="w-screen flex flex-col items-center py-12 md:py-24 lg:py-32 xl:py-48 bg-[#f7f7f7]">
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
                  <div className="flex flex-row items-center">
                    <img src="/icons/record-fill-red.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-lg tracking-wide font-medium text-[#757575]">RECORD</h3>
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
                  <div className="flex flex-row items-center">
                  <img src="/icons/list-magnifying-glass.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-lg tracking-wide font-medium text-[#757575]">REVIEW</h3>
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
                  <div className="flex flex-row items-center">
                    <img src="/icons/binoculars-duotone.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-lg tracking-wide font-medium text-[#757575]">GET ASSISTANCE</h3>
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


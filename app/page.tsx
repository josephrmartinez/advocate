import Link from "next/link"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import FAQ from "@/components/FAQ"

export default function Landing() {
  return (
    <div className="flex flex-col flex-1 items-center min-h-screen bg-[#ffffff]">
      <main className="flex-1">
        <section className="w-screen flex flex-col items-center py-12 md:py-24 lg:py-32 xl:py-48 bg-[#f7f7f7]">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
                <p className="mx-auto text-gray-600 font-bold text-5xl  dark:text-gray-400">
                Record your medical appointments. 
                </p>
                <p className="mx-auto text-gray-500 font-semibold text-4xl  dark:text-gray-400">
                Get clarity, accountability, and better outcomes.
                </p>
              <div className="py-10">
              
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12">
          <div className="px-4">
            <h2 className="mb-12 text-2xl font-semibold text-center text-[#757575]">
                patient-directed healthcare:
            </h2>
            <div className="grid gap-6 px-4 items-center lg:grid-cols-3">
            <Card>
                <CardHeader>
                  <div className="flex flex-row items-center">
                    <img src="/icons/binoculars-duotone.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-md tracking-wide font-semibold text-[#757575]">PREP</h3>
                  </div>
                  
                </CardHeader>
                <CardContent>
                  <p className="text-gray-700 font-semibold text-xl mb-6">
                  Get support preparing for your medical appointments. 
                  </p>
                  <p className="text-gray-500">Receive personalized questions to ask your doctors based on your health history and current trends in medical research. Be prepared for your next appointment with insights that help you make the most out of your time with healthcare providers.</p>
                </CardContent>
              </Card>
              
              <Card>
                <CardHeader>
                  <div className="flex flex-row items-center">
                    <img src="/icons/record-fill-red.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-md tracking-wide font-semibold text-[#757575]">RECORD</h3>
                  </div>
                  
                </CardHeader>
                <CardContent>
                  <p className="text-gray-700 font-semibold text-xl mb-6">
                    Capture your medical appointments with our easy and secure audio recording tool.  
                  </p>
                  <p className="text-gray-500">Automatic transcriptions of your appointment recordings give you a record of exactly who said exactly what. No more missed details, no more forgotten advice. Recordings and transcripts are stored permanently in a secure, encrypted environment.</p>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <div className="flex flex-row items-center">
                  <img src="/icons/list-magnifying-glass.png" className="w-6 h-6 mr-4" />
                    <h3 className="text-md tracking-wide font-semibold text-[#757575]">REVIEW</h3>
                  </div>
                  
                </CardHeader>
                <CardContent>
                  <p className="text-gray-700 font-semibold text-xl mb-6">
                  Search, review, and interact with your healthcare provider conversations.
                  </p>
                  <p className="text-gray-500">Share your transcribed recordings with family or approved caregivers. Identify potential irregularities. Get recommendations of alternative approaches and recent medical research that may not have been highlighted during your appointments.</p>
                </CardContent>
              </Card>

              
              
              

            </div>
          </div>
        </section>
        <section className="w-screen flex flex-col items-center py-32 bg-[#f7f7f7]">
          
            <div className="flex flex-col w-[40rem]">
                <p className="ml-0 mb-8  text-gray-600 font-bold text-5xl dark:text-gray-400">
                FAQs 
                </p>
                <FAQ 
                  question={"Is my data safe?"}
                  answer={"‍advocate.ai encrypts and stores all user data in secure storage. No data is sold to third parties."}
                  />
                <FAQ 
                  question={"Is advocate.ai HIPAA compliant?"}
                  answer={"‍The app is patient-directed and does not receive electronic medical information from a Covered Provider and is therefore not covered by HIPAA. advocate.ai protects personal health information (PHI) and is fully compliant with FDA and FTC regulations on patient recordings of consults."}
                  />
                <FAQ 
                question={"Is recording legal?"}
                answer={"You have the right to record your medical appointments. In most states, it is not necessary to request permission from your provider in order to make a recording. You must obtain consent from all parties to record in the following states: California, Connecticut, Florida, Illinois, Maryland, Massachusetts, Montana, New Hampshire, Pennsylvania and Washington."}
                  />
                <FAQ 
                  question={"What if there are signs saying recording isn’t allowed?"}
                  answer={"Those signs are to keep you from recording other patients. There’s nothing wrong with asking your doctor if it’s okay to record your consultation."}
                  />
                <FAQ 
                question={"Does advocate.ai offer medical advice?"}
                answer={"advocate.ai is a patient-directed health advocacy tool that is meant to compliment your interactions with medical providers. This tool does not offer medical advice and is not a replacement for trained medical professionals."}
                  />
                
              
            </div>
          
        </section>

      </main>    


    </div>
  )
}


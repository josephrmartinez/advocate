'use client'
import React from "react"
import { useState } from "react"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import Transcript from '../dev/Transcript'; 


export default function Component() {

  const [contentVisible, setContentVisible] = useState(false);

  const toggleContent = () => {
    setContentVisible(!contentVisible);
    console.log("attempted toggle")
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-[#ffffff]">
      
      <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-10 w-screen">
      <div className="grid grid-cols-5 grid-rows-8 gap-4">
  
  <div className="col-span-1 row-start-2 flex flex-col">
  <button className="text-center text-lg font-bold rounded-full px-4 py-4 mb-2 hover:bg-gray-100">
    + New appointment
  </button>
  <button className="text-center text-lg font-bold rounded-full px-4 py-4 mb-2 hover:bg-gray-100">
    Prep for appointment
  </button>
    
          
  </div>

  
  <div className="col-start-2 col-span-4 row-span-1">
    <Input className="pl-8 my-4 h-16 w-full" placeholder="Search all appointments..." type="search" />
  </div>

  <div className="col-start-2 col-span-4 row-start-2 row-span-7">
    <Card>
            <CardHeader className="grid grid-cols-5 border rounded-lg items-center pb-5 mb-5 space-y-0">
              <p className="text-lg font-semibold">Dr. Smith Intake</p>
              

            <div className="flex flex-row items-center">
              <div className="text-sm bg-black rounded-full py-2 px-3 mx-2 text-gray-100">oncology</div>
              <div className="text-sm bg-black rounded-full py-2 px-3 mx-2 text-gray-100">specialist</div>
              
            </div>

              <div className="flex flex-row items-center col-start-4">
                <CalendarIcon className="w-4 h-4 mr-4 text-gray-500 dark:text-gray-400" />
                <div className="text-sm font-medium">November 29, 2023</div>
              </div>
              
              <div 
              className="col-start-5 text-center text-sm text-gray-600 underline underline-offset-2 hover:cursor-pointer"
              onClick={toggleContent}>
                expand
              </div>



            </CardHeader>

            {contentVisible && 
            <CardContent>
            
            <div className="flex flex-col items-center">
              <audio className="mt-2 w-full my-4" controls>
                <source src="/dev/Amols.wav" type="audio/wav" />
                Your browser does not support the audio element.
              </audio>
              <Input className="pl-8 my-4 w-11/12" placeholder="Ask about this appointment..." type="search" />
              <div className="w-11/12 ">
                <div className="flex flex-row">
                <a className="text-lg font-semibold text-gray-700 mt-2 underline underline-offset-4"
                href="#">
                  Transcript
                </a>
                <a className="text-lg font-semibold text-gray-700 mt-2 underline underline-offset-4"
                href="#">
                  Summary
                </a>
                <a className="text-lg font-semibold text-gray-700 mt-2 underline underline-offset-4"
                href="#">
                  Resources
                </a>
                </div>
                
                <div className="h-48 overflow-y-scroll border border-gray-100 rounded-lg">
                  <Transcript/>
                </div>
                
              </div>
            </div>
            
          </CardContent>
            
            }
            
    </Card>
  </div>
</div>
        
        
      </main>

      
    </div>
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




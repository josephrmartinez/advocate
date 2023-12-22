'use client'
import React from "react"
import { Input } from "@/components/ui/input"
import AppointmentCard from "@/components/AppointmentCard"


export default function Dashboard() {

  const appointmentData = {
    title: "New Patient Intake",
    clinic: "New Direction Fertility Center",
    tags: ["fertility", "specialist"],
    date: "November 29, 2023",
    audio: "/dev/Amols.wav"
}

const secondAppt = {
  title: "Review blood work",
  clinic: "Naturopathic Clinic",
  tags: ["blood work"],
  date: "November 19, 2023",
  audio: "/dev/Amols.wav"
}

const thirdAppt = {
  title: "Consultation",
  clinic: "Naturopathic Clinic",
  tags: ["cholesterol"],
  date: "December 21, 2023",
  audio: "/dev/Amols.wav"
}

  return (
    <div className="flex flex-col items-center min-h-screen bg-[#ffffff]">
      <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-10 w-screen">
        <div className="grid grid-cols-5 grid-rows-8 gap-4">
          <div className="col-span-1 row-start-2 row-span-6 flex flex-col items-start">
            <button className="text-left text-md font-semibold text-gray-700 rounded-full px-4 py-4 mb-2">
              New appointment
            </button>
            <button className="text-left text-md font-semibold text-gray-700 rounded-full px-4 py-4 mb-2">
              Prep for appointment
            </button>   
          </div>
          <div className="col-start-2 col-span-4 row-span-1">
            <Input className="pl-8 my-4 h-16 w-full" placeholder="Search all appointments..." type="search" />
          </div>

          <div className="col-start-2 col-span-4 row-start-2 row-span-7 h-[36rem] pr-4 overflow-y-scroll">
            
            <AppointmentCard appointmentData={thirdAppt}/>
            <AppointmentCard appointmentData={appointmentData}/>
            <AppointmentCard appointmentData={secondAppt}/>
            
          </div>

        </div>
      </main>
    </div>
  )
}


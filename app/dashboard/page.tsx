'use client'
import React from "react"
import { Input } from "@/components/ui/input"
import AppointmentCard from "@/components/AppointmentCard"


export default function Component() {


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
            <AppointmentCard/>
          </div>

        </div>
      </main>
    </div>
  )
}


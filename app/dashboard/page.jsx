'use client'
import React from "react"
import Link from "next/link"

import AllAppointments from "@/components/AllAppointments";
import InviteCaregiver from "@/components/InviteCaregiver";
import PrepareForAppointment from "@/components/PrepareForAppointment";
import RecordAppointment from "@/components/RecordAppointment";
import UploadAppointment from "@/components/UploadAppointment";
import Settings from "@/components/Settings";
import { useState } from "react"

export default function Dashboard() {

  const [selectedSection, setSelectedSection] = useState("view-all-appointments");

  const renderSelectedComponent = () => {
    switch (selectedSection) {
      case "view-all-appointments":
        return <AllAppointments />;
      case "invite-caregiver":
        return <InviteCaregiver />;
      case "prepare-for-appointment":
        return <PrepareForAppointment />;
      case "record-appointment":
        return <RecordAppointment />;
      case "upload-appointment":
        return <UploadAppointment />;
      case "settings":
        return <Settings />;
      default:
        return "view-all-appointments";
  }
}

  return (
    <div className="flex flex-col items-center bg-[#ffffff]">
      <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-10 w-screen">
        <div className="grid grid-cols-5 grid-rows-8 gap-4">
          <div className="border rounded-lg col-span-1 row-span-2 flex flex-col items-start bg-gray-50/30">
            <div
              onClick={() => setSelectedSection("view-all-appointments")}
              className="text-left text-md font-semibold border-b border-gray-100 text-gray-700 px-4 py-4 w-full"
            >
              View all appointments
            </div>
            <div
              onClick={() => setSelectedSection("upload-appointment")}
              className="text-left text-md font-semibold border-b border-gray-100 text-gray-700 px-4 py-4 w-full"
            >
              Upload appointment
            </div>
          </div>
          

          <div className="col-start-2 col-span-4 row-start-1 row-span-7">
            {renderSelectedComponent()}
          </div>

        </div>
      </main>
    </div>
  )
}


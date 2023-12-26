import AppointmentCard from "@/components/AppointmentCard"
import { Input } from "@/components/ui/input"



export default function AllAppointments() {


  const appointmentData = {
    title: "New Patient Intake",
    clinic: "Nova Fertility Center",
    tags: ["fertility", "specialist"],
    date: "November 29, 2023",
    audio: "/dev/Amols.wav"
}

const secondAppt = {
  title: "Review blood work",
  clinic: "RDM Naturopathic Clinic",
  tags: ["blood work"],
  date: "November 19, 2023",
  audio: "/dev/Amols.wav"
}

const thirdAppt = {
  title: "Consultation",
  clinic: "RDM Naturopathic Clinic",
  tags: ["cholesterol"],
  date: "December 21, 2023",
  audio: "/dev/Amols.wav"
}


const fourthAppt = {
  title: "Consultation",
  clinic: "Minute Clinic",
  tags: ["rib pain", "urgent"],
  date: "November 3, 2023",
  audio: "/dev/Amols.wav"
}

const fifthAppt = {
  title: "Consultation",
  clinic: "Naturopathic Clinic",
  tags: ["cholesterol"],
  date: "October 16, 2023",
  audio: "/dev/Amols.wav"
}



    return <div className="grid grid-cols-4">
    <div className="col-span-4 row-span-1 ">
      <Input className="pl-8 mb-4 h-16 w-full" placeholder="Search all appointments..." type="search" />
    </div>
    <div className="col-span-4 row-start-2 h-[36rem] pr-4 overflow-y-scroll">
      <AppointmentCard appointmentData={thirdAppt}/>
      <AppointmentCard appointmentData={appointmentData}/>
      <AppointmentCard appointmentData={secondAppt}/>
      <AppointmentCard appointmentData={fourthAppt}/>
      <AppointmentCard appointmentData={fifthAppt}/>
    </div>
    
    </div>;
  };


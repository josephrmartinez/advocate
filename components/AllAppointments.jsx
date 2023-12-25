import AppointmentCard from "@/components/AppointmentCard"



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



    return <>
    <AppointmentCard appointmentData={thirdAppt}/>
    <AppointmentCard appointmentData={appointmentData}/>
    <AppointmentCard appointmentData={secondAppt}/>
    <AppointmentCard appointmentData={fourthAppt}/>
    <AppointmentCard appointmentData={fifthAppt}/>
    </>;
  };


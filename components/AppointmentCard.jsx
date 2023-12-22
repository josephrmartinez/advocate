import React from "react"
import { useState, useEffect } from "react"
import { CardHeader, CardContent, Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import transcriptContent from './dev/transcriptContent'
import summaryContent from './dev/summaryContent'
import feedbackContent from './dev/feedbackContent'


export default function AppointmentCard({ appointmentData }){

const [contentVisible, setContentVisible] = useState(false);
const [activeTab, setActiveTab] = useState('transcript');




const toggleContent = () => {
  setContentVisible(!contentVisible);
  console.log("attempted toggle")
};

const handleTabClick = (tab) => {
  setActiveTab(tab);
};

const ContentRenderer = ({ content }) => {
    return <>{content}</>;
  };

return (
<Card>
    <CardHeader className="grid grid-cols-5 border border-gray-100 rounded-lg items-center pb-5 space-y-0">
        <p className="text-lg font-semibold">{appointmentData.title}</p>
        <p className="text-sm font-medium">{appointmentData.clinic}</p>
        <div className="flex flex-row items-center">
            {appointmentData.tags.map((tag, index) => (
                <div
                    key={index} 
                    className="text-sm bg-black rounded-full py-2 px-3 mx-2 text-gray-100"
                >
                    {tag}
                </div>
            ))}
        </div>

        <div className="flex flex-row items-center col-start-4">
            <CalendarIcon className="w-4 h-4 mr-3 text-gray-500 dark:text-gray-400" />
            <div className="text-sm font-medium">{appointmentData.date}</div>
        </div>
        
        <div 
        className="col-start-5 text-center text-sm text-gray-600 underline underline-offset-2 hover:cursor-pointer"
        onClick={toggleContent}>
            {contentVisible ? 'hide' : 'view'}
        </div>



        </CardHeader>

        {contentVisible && 
        <CardContent>
        
        <div className="flex flex-col items-center mt-5">
        <audio className="w-full my-4" controls>
            <source src={appointmentData.audio} type="audio/wav" />
            Your browser does not support the audio element.
        </audio>
        <Input className="pl-6 my-4 w-11/12" placeholder="Ask about this appointment..." type="search" />
        <div className="w-11/12 ">
        
            <div className="grid grid-cols-5 mb-4">
            
            <button className={`text-lg font-semibold text-gray-500 mt-2 ${activeTab === 'transcript' && 'text-gray-700 underline underline-offset-4'}`}
                onClick={() => handleTabClick('transcript')}>Transcript</button>
            <button className={`text-lg font-semibold text-gray-500 mt-2 ${activeTab === 'summary' && 'text-gray-700 underline underline-offset-4'}`}
                onClick={() => handleTabClick('summary')}>Summary</button>
            <button className={`text-lg font-semibold text-gray-500 mt-2 ${activeTab === 'feedback' && 'text-gray-700 underline underline-offset-4'}`}
                onClick={() => handleTabClick('feedback')}>Feedback</button>
            
            </div>

            <div className="h-48 overflow-y-scroll border p-2 border-gray-100 rounded-lg">
            {activeTab === 'transcript' && <ContentRenderer content={transcriptContent}/>}
            {activeTab === 'summary' && <ContentRenderer content={summaryContent}/>}
            {activeTab === 'feedback' && <ContentRenderer content={feedbackContent}/>}
            </div>
        </div>
        
        </div>

        
    </CardContent>
        
        }
        
</Card>
);

  
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
  
  
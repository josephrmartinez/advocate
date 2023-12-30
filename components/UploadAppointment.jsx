'use client'

import { useState } from 'react';
import { uploadFile } from '@/utils/supabase/uploadFile';


const UploadAppointment = () => {
  const [file, setFile] = useState(null);

  

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    try {
        await uploadFile('recordings', file.name, file);
        // Additional logic after successful upload
      } catch (error) {
        console.error('Error uploading file:', error.message);
      }
    };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadAppointment;
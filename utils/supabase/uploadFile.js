import * as tus from 'tus-js-client';
import { createClient } from './client';

const projectId = 'dtsakdgzzxjacefvloeu';

async function uploadFile(bucketName, fileName, file) {
    const supabase = createClient()

  const { data, error } = await supabase.auth.getSession();
  
  const userId = data.session.user.id

  const { upload, uploadError } = await supabase.storage.from(bucketName).upload(`${userId}/`, file)
  if (uploadError) {
    // Handle error
  } else {
    // Handle success
  }
}

  // return new Promise((resolve, reject) => {
  //   console.log('userId', userId)
  //   var upload = new tus.Upload(file, {
  //     endpoint: `https://${projectId}.supabase.co/storage/v1/upload/resumable`,
  //     retryDelays: [0, 3000, 5000, 10000, 20000],
  //     headers: {
  //       authorization: `Bearer ${data.session.access_token}`,
  //       'x-upsert': 'true',
  //     },
  //     uploadDataDuringCreation: true,
  //     removeFingerprintOnSuccess: true,
  //     metadata: {
  //       bucketName: bucketName,
  //       objectName: `${userId}/${fileName}`,
  //       contentType: file.type,
  //       cacheControl: 3600,
  //     },
  //     chunkSize: 6 * 1024 * 1024,
  //     onError: function (error) {
  //       console.log('Failed because: ' + error);
  //       console.log('data session access_token', data.session.access_token);
  //       console.log('user', user)
  //       reject(error);
  //     },
  //     onProgress: function (bytesUploaded, bytesTotal) {
  //       var percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2);
  //       console.log(bytesUploaded, bytesTotal, percentage + '%');
  //     },
  //     onSuccess: function () {
  //       console.log('Download %s from %s', upload.file.name, upload.url);
  //       resolve();
  //     },
  //   });

  //   // Check if there are any previous uploads to continue.
  //   return upload.findPreviousUploads().then(function (previousUploads) {
  //     // Found previous uploads so we select the first one.
  //     if (previousUploads.length) {
  //       upload.resumeFromPreviousUpload(previousUploads[0]);
  //     }

  //     // Start the upload
  //     upload.start();
  //   });
  // });


export { uploadFile };

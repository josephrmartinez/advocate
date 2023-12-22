import { GeistSans } from 'geist/font/sans'
import './globals.css'
import Header from '@/components/Header'


const defaultUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : 'http://localhost:3000'

export const metadata = {
  metadataBase: new URL(defaultUrl),
  title: 'PatientAdvocate',
  description: 'Start recording your medical appointments.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${GeistSans.className} antialiased`}>
        <Header />
        {children}
      </body>
    </html>
  )
}

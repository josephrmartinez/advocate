import { GeistSans } from 'geist/font/sans'
import './globals.css'
import Header from '@/components/Header'
import Head from 'next/head'


const defaultUrl = process.env.VERCEL_URL
  ? `https://${process.env.VERCEL_URL}`
  : 'http://localhost:3000'

export const metadata = {
  metadataBase: new URL(defaultUrl),
  title: 'advocate.ai',
  description: 'Start recording your medical appointments.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
    
    <html lang="en">
      <Head>
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <body className={`${GeistSans.className} antialiased pt-16`}>
        <Header />
        {children}
      </body>
    </html>
    </>
  )
}

import { GeistSans } from 'geist/font/sans'
import './globals.css'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import Head from 'next/head'

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
    <div className="bg-background text-foreground min-h-screen flex flex-col items-center">
      <Head>
        <html lang="en" className={GeistSans.className}/>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
      </Head>
      <Header />
      <main>
      {children}
      </main>
      <Footer />
    </div>
  )
}

import RootLayout from './layout'
import Head from 'next/head';

function MyApp({ Component, pageProps }) {
 return (
    
  <RootLayout>
    <Head>
      <link rel='favicon' href='/favicon.ico'/>
    </Head>
    <Component {...pageProps} />
  </RootLayout>
 );
}

export default MyApp;
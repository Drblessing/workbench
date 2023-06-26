import './globals.css';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'Create Next App',
  author: 'John Patterson',
  description: 'Generated by create next app1',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang='en'>
      <head>
        <meta charSet='utf-8' />
        <meta name='author' content={metadata.author} />
      </head>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
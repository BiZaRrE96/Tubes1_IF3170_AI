import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Tugas Besar 1 IF3070 Dasar Inteligensi Artifisial & IF3170 Inteligensi Artifisial",
  description: "Pencarian Solusi Diagonal Magic Cube dengan Local Search",
  keywords: ["Artificial Intelligence", "Local Search", "Diagonal Magic Cube", "IF3070", "IF3170", "Inteligensi Artifisial", "Tugas Besar"],
  openGraph: {
    type: 'website',
    locale: 'id_ID',
    url: 'https://yourwebsite.com/diagonal-magic-cube',
    title: 'Tugas Besar 1 IF3070 & IF3170 | Pencarian Solusi Diagonal Magic Cube',
    description: 'Temukan solusi untuk Diagonal Magic Cube menggunakan metode Local Search dalam Tugas Besar 1 untuk mata kuliah IF3070 Dasar Inteligensi Artifisial dan IF3170 Inteligensi Artifisial.',
    siteName: 'Tugas Besar AI',
  },
  twitter: {
    card: 'summary_large_image',
    site: '@your_twitter_handle',
    title: 'Tugas Besar 1 IF3070 & IF3170 | Pencarian Solusi Diagonal Magic Cube',
    description: 'Solusi Diagonal Magic Cube menggunakan metode Local Search untuk mata kuliah IF3070 dan IF3170 Inteligensi Artifisial.',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}

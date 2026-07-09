import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BERENT WORKSHOPS",
  description: "Workshop-Plattform von BERENT",
  icons: {
    icon: "/assets/images/favicon.png",
    shortcut: "/assets/images/favicon.png",
    apple: "/assets/images/favicon.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="de" className="h-full antialiased">
      <body className="min-h-full flex flex-col bg-bg text-text font-body">
        {children}
      </body>
    </html>
  );
}

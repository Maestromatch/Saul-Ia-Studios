import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AETRIA STUDIOS | IA, automatizacion y desarrollo web",
  description:
    "AETRIA STUDIOS construye sistemas de IA, automatizacion, agentes inteligentes y desarrollo web para empresas modernas.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es-CL" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}

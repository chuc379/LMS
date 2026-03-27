import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-slate-900">
        <nav className="p-4 bg-white border-b shadow-sm mb-6">
          <div className="max-w-6xl mx-auto font-bold text-xl text-indigo-600">
            🚀 TeenUp LMS Portal
          </div>
        </nav>
        {children}
      </body>
    </html>
  )
}
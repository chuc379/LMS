'use client'
import { useState } from 'react';
import ParentStudentForm from '../components/ParentStudentForm';
import WeeklyCalendar from '../components/WeeklyCalendar';
import RegistrationModal from '../components/RegistrationModal';

export default function Home() {
  const [selectedClass, setSelectedClass] = useState(null);

  return (
    <main className="max-w-6xl mx-auto p-4 space-y-10">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Bên trái: Form tạo data */}
        <div className="md:col-span-1">
          <ParentStudentForm />
        </div>

        {/* Bên phải: Lịch học */}
        <div className="md:col-span-2">
          <WeeklyCalendar onSelectClass={(cls) => setSelectedClass(cls)} />
        </div>
      </div>

      {/* Popup khi click vào lớp */}
      {selectedClass && (
        <RegistrationModal 
          selectedClass={selectedClass} 
          onClose={() => setSelectedClass(null)} 
        />
      )}
    </main>
  );
}
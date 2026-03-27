import { useEffect, useState } from 'react';
import { api } from '../lib/api';

export default function WeeklyCalendar({ onSelectClass }) {
  const [calendar, setCalendar] = useState({});
  const days = [2, 3, 4, 5, 6, 7, 8];

  const fetchWeek = async () => {
    const data = {};
    for (const d of days) {
      try {
        data[d] = await api.getClassesByDay(d);
      } catch (e) { data[d] = []; }
    }
    setCalendar(data);
  };

  useEffect(() => { fetchWeek(); }, []);

  return (
    <div className="bg-white rounded-xl shadow-md border border-gray-100 overflow-hidden">
      <div className="p-4 border-b flex justify-between items-center">
        <h2 className="text-xl font-bold">Lịch Lớp Học</h2>
        <button onClick={fetchWeek} className="text-sm text-indigo-600 hover:underline">Làm mới</button>
      </div>
      <div className="grid grid-cols-7 gap-px bg-gray-200">
        {days.map(d => (
          <div key={d} className="bg-white min-h-[400px]">
            <div className="p-2 bg-gray-50 text-center border-b font-bold text-gray-600 text-sm">
              Thứ {d === 8 ? 'CN' : d}
            </div>
            <div className="p-2 space-y-2">
              {calendar[d]?.map(cls => (
                <div 
                  key={cls.id}
                  onClick={() => onSelectClass(cls)}
                  className="p-3 bg-indigo-50 border border-indigo-100 rounded-lg cursor-pointer hover:bg-indigo-100 transition-colors shadow-sm"
                >
                  <h4 className="font-bold text-indigo-900 text-sm leading-tight">{cls.name}</h4>
                  <p className="text-[10px] text-indigo-600 font-medium mt-1 uppercase">{cls.subject}</p>
                  <p className="text-[11px] text-gray-500 mt-2">🕒 {cls.time_slot.slice(0,5)}</p>
                  <p className="text-[11px] text-gray-400 italic">👤 {cls.teacher_name}</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
import { useState } from 'react';
import { api } from '../lib/api';

export default function RegistrationModal({ selectedClass, onClose }) {
  const [studentId, setStudentId] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  if (!selectedClass) return null;

  const handleRegister = async () => {
    if (!studentId) return;
    setLoading(true);
    setError("");
    try {
      await api.registerStudentToClass(selectedClass.id, parseInt(studentId));
      alert("Đăng ký thành công!");
      onClose();
    } catch (err) {
      setError(err.detail || "Lỗi không xác định");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl p-8 max-w-md w-full shadow-2xl">
        <h3 className="text-2xl font-bold text-gray-900">Đăng ký lớp học</h3>
        <div className="mt-4 p-4 bg-gray-50 rounded-xl">
          <p className="text-sm font-bold text-indigo-600 uppercase tracking-wide">{selectedClass.subject}</p>
          <p className="text-lg font-semibold text-gray-800">{selectedClass.name}</p>
          <div className="flex justify-between mt-2 text-sm text-gray-500">
            <span>📅 Thứ {selectedClass.day_of_week === 8 ? 'CN' : selectedClass.day_of_week}</span>
            <span>⏰ {selectedClass.time_slot.slice(0,5)}</span>
          </div>
        </div>

        <div className="mt-6">
          <label className="block text-sm font-bold text-gray-700 mb-2">ID Học sinh</label>
          <input 
            type="number" 
            className="w-full p-3 border-2 border-gray-100 rounded-xl focus:border-indigo-500 outline-none transition-all"
            placeholder="Nhập ID học sinh (ví dụ: 1)"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
          />
        </div>

        {error && (
          <div className="mt-4 p-3 bg-red-50 text-red-600 text-sm rounded-lg border border-red-100 font-medium">
            ⚠️ {error}
          </div>
        )}

        <div className="mt-8 flex gap-3">
          <button onClick={onClose} className="flex-1 py-3 text-gray-500 font-bold hover:bg-gray-50 rounded-xl">Hủy</button>
          <button 
            onClick={handleRegister} 
            disabled={loading}
            className="flex-1 py-3 bg-indigo-600 text-white font-bold rounded-xl hover:bg-indigo-700 shadow-lg shadow-indigo-200 disabled:opacity-50"
          >
            {loading ? "Đang đăng ký..." : "Xác nhận"}
          </button>
        </div>
      </div>
    </div>
  );
}

import { useState } from 'react';
import { api } from '../lib/api';

export default function ParentStudentForm() {
  const [parentId, setParentId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const onParentSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const formData = new FormData(e.target);
    try {
      const res = await api.createParent(Object.fromEntries(formData));
      setParentId(res.id);
      setMessage("Đã tạo Phụ huynh! Hãy tiếp tục tạo Học sinh.");
    } catch (err) { setMessage("Lỗi: " + (err.detail || "Không thể tạo")); }
    setLoading(false);
  };

  const onStudentSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const formData = new FormData(e.target);
    const data = { ...Object.fromEntries(formData), parent_id: parentId, dob: "2015-01-01" };
    try {
      const res = await api.createStudent(data);
      setMessage(`Thành công! ID Học sinh: ${res.id}`);
      e.target.reset();
    } catch (err) { setMessage("Lỗi: " + (err.detail || "Không thể tạo")); }
    setLoading(false);
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-md border border-gray-100">
      {!parentId ? (
        <form onSubmit={onParentSubmit} className="space-y-4">
          <h2 className="text-xl font-bold text-gray-800">1. Đăng ký Phụ huynh</h2>
          <input name="name" placeholder="Họ tên" className="w-full p-2 border rounded-lg" required />
          <input name="phone" placeholder="Số điện thoại" className="w-full p-2 border rounded-lg" required />
          <input name="email" type="email" placeholder="Email" className="w-full p-2 border rounded-lg" />
          <button disabled={loading} className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700">
            {loading ? "Đang xử lý..." : "Tiếp theo"}
          </button>
        </form>
      ) : (
        <form onSubmit={onStudentSubmit} className="space-y-4">
          <h2 className="text-xl font-bold text-green-600">2. Đăng ký Học sinh</h2>
          <p className="text-xs text-gray-500 italic">Parent ID: {parentId}</p>
          <input name="name" placeholder="Tên học sinh" className="w-full p-2 border rounded-lg" required />
          <input name="current_grade" type="number" placeholder="Lớp (1-12)" className="w-full p-2 border rounded-lg" required />
          <button disabled={loading} className="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700">
            Tạo hồ sơ học sinh
          </button>
          <button type="button" onClick={() => setParentId(null)} className="w-full text-xs text-gray-400">Tạo Parent khác</button>
        </form>
      )}
      {message && <p className="mt-4 text-sm font-medium text-center text-indigo-600">{message}</p>}
    </div>
  );
}
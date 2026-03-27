const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5001/api";

/**
 * Hàm helper xử lý response và lỗi tập trung
 */
const handleResponse = async (response) => {
  const data = await response.json().catch(() => ({ detail: "Lỗi kết nối Server" }));
  if (!response.ok) {
    throw data; // Ném lỗi để các component bắt được trong try/catch
  }
  return data;
};

export const api = {
  // --- PARENTS ---
  // POST /api/parents
  createParent: (data) => 
    fetch(`${API_BASE}/parents/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(handleResponse),

  // GET /api/parents/{id}
  getParent: (id) => fetch(`${API_BASE}/parents/${id}`).then(handleResponse),


  // --- STUDENTS ---
  // POST /api/students
  createStudent: (data) => 
    fetch(`${API_BASE}/students/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(handleResponse),

  // GET /api/students/{id}
  getStudent: (id) => fetch(`${API_BASE}/students/${id}`).then(handleResponse),


  // --- CLASSES ---
  // POST /api/classes
  createClass: (data) => 
    fetch(`${API_BASE}/classes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(handleResponse),

  // GET /api/classes?day={weekday}
  getClassesByDay: (weekday) => 
    fetch(`${API_BASE}/classes?day=${weekday}`).then(handleResponse),


  // --- CLASS REGISTRATIONS ---
  // POST /api/classes/{class_id}/register
  // Backend xử lý: Kiểm tra sĩ số, Trùng lịch, Gói học (Expiry & Sessions)
  registerStudent: (classId, studentId) => 
    fetch(`${API_BASE}/classes/${classId}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ student_id: studentId })
    }).then(handleResponse),

  // DELETE /api/registrations/{id}
  // Backend xử lý: Hủy trước 24h hoàn buổi, dưới 24h không hoàn buổi
  cancelRegistration: (regId) => 
    fetch(`${API_BASE}/registrations/${regId}`, {
      method: 'DELETE'
    }).then(handleResponse),


  // --- SUBSCRIPTIONS ---
  // POST /api/subscriptions
  createSubscription: (data) => 
    fetch(`${API_BASE}/subscriptions/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(handleResponse),

  // PATCH /api/subscriptions/{id}/use
  useSession: (subId) => 
    fetch(`${API_BASE}/subscriptions/${subId}/use`, {
      method: 'PATCH'
    }).then(handleResponse),

  // GET /api/subscriptions/{id}
  getSubscription: (subId) => 
    fetch(`${API_BASE}/subscriptions/${subId}`).then(handleResponse),
};
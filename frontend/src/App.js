// frontend/src/App.js (ファイル全体をこれで上書きしてください)

import React, { useEffect } from 'react'; 
import axios from 'axios'; 
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom'; 
import Login from './components/Login'; 
import Signup from './components/Signup'; // Signupコンポーネントもインポート

function App() {

  // アプリ初回ロード時にCSRFトークンを取得
  useEffect(() => {
    const getCsrfToken = async () => {
      try {
        await axios.get('http://localhost:8000/api/csrf/');
        console.log("CSRF cookie set via GET /api/csrf/"); 
      } catch (error) {
        console.error("Error fetching CSRF token:", error);
      }
    };
    getCsrfToken();
  }, []); // 空の配列で初回のみ実行

  return (
    <Router>
      <div className="App">
        <nav style={{ padding: '10px', marginBottom: '20px', borderBottom: '1px solid #eee' }}>
          <Link to="/login" style={{ marginRight: '15px' }}>ログイン</Link>
          <Link to="/signup">新規登録</Link>
        </nav>

        <Routes>
          <Route path="/login" element={<Login />} /> 
          <Route path="/signup" element={<Signup />} /> 
          <Route path="/" element={<Navigate replace to="/login" />} /> 
        </Routes>
      </div>
    </Router>
  );
}

export default App;
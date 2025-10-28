import React, { useState } from 'react';
import axios from 'axios';

// DjangoのSECRET_KEYや環境によってCSRFトークンの問題が発生する可能性があるため、
// 以下の設定を追加することで、セッションクッキーを確実に送受信します。
axios.defaults.withCredentials = true; 

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage('ログイン中...');

    try {
      // ⚠️ http://localhost:8000/api/login/ へPOSTリクエスト
      const response = await axios.post('http://localhost:8000/api/login/', {
        username: username,
        password: password,
      });

      if (response.data.success) {
        setMessage(`✅ ログイン成功！ユーザー: ${response.data.username}`);
        // 成功後の処理（画面遷移など）
      } else {
        setMessage('❌ ログイン失敗: ' + response.data.message);
      }
    } catch (error) {
      console.error("ログインエラー:", error);
      if (error.response) {
        if (error.response.status === 401) {
          setMessage('❌ ログイン失敗: ユーザー名またはパスワードが不正です。');
        } else {
          setMessage(`❌ サーバーエラー (${error.response.status})`);
        }
      } else {
        setMessage('❌ ネットワークエラー: バックエンドサーバーに接続できません。');
      }
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', maxWidth: '400px', margin: '50px auto' }}>
      <h2>ユーザーログイン</h2>
      <form onSubmit={handleLogin}>
        <div style={{ marginBottom: '10px' }}>
          <label style={{ display: 'block' }}>ユーザー名:</label>
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            required 
          />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <label style={{ display: 'block' }}>パスワード:</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
        </div>
        <button type="submit" style={{ padding: '10px 15px', backgroundColor: '#007bff', color: 'white', border: 'none', cursor: 'pointer' }}>ログイン</button>
      </form>
      <p style={{ color: message.includes('成功') ? 'green' : 'red', marginTop: '15px' }}>{message}</p>
    </div>
  );
}

export default Login;
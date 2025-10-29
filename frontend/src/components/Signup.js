import React, { useState } from 'react';
import axios from 'axios';

// セッションクッキーの送受信設定は継続
axios.defaults.withCredentials = true; 

function Signup() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSignup = async (e) => {
    e.preventDefault();
    setMessage('登録中...');

    try {
      // ⚠️ http://localhost:8000/api/signup/ へPOSTリクエスト
      const response = await axios.post('http://localhost:8000/api/signup/', {
        username: username,
        password: password,
        // emailフィールドはオプションで追加可能
      });

      if (response.status === 201) {
        setMessage(`✅ 登録成功！ログイン画面へ移動してください。`);
        // 成功後の処理（ログインページへのリダイレクトなど）
        setUsername('');
        setPassword('');
      }
    } catch (error) {
      console.error("登録エラー:", error);
      if (error.response) {
        if (error.response.status === 409) {
          setMessage('❌ 登録失敗: このユーザー名は既に使用されています。');
        } else {
          setMessage(`❌ サーバーエラー (${error.response.status}): ${error.response.data.message}`);
        }
      } else {
        setMessage('❌ ネットワークエラー: バックエンドサーバーに接続できません。');
      }
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', maxWidth: '400px', margin: '50px auto' }}>
      <h2>新規ユーザー登録</h2>
      <form onSubmit={handleSignup}>
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
        <button type="submit" style={{ padding: '10px 15px', backgroundColor: '#28a745', color: 'white', border: 'none', cursor: 'pointer' }}>アカウント作成</button>
      </form>
      <p style={{ color: message.includes('成功') ? 'green' : 'red', marginTop: '15px' }}>{message}</p>
    </div>
  );
}

export default Signup;
// frontend/src/App.js
import React from 'react';
import Login from './components/Login'; // 👈 Loginコンポーネントをインポート

function App() {
  return (
    <div className="App">
      {/* 既存のコードを消してLoginコンポーネントを表示 */}
      <Login /> 
    </div>
  );
}

export default App;
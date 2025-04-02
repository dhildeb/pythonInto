import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const api = axios.create({
    baseURL: 'http://localhost:8000'
  });
  
  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const response = await api.get('/get-message');
        console.log(response)
        setMessage(response.data.message);
      } catch (error) {
        console.error('Error fetching message:', error);
      }
    };

    fetchMessage();
  }, []);

  const updateText = async (text: string) => {
    try {
      const res = await api.put(`/change?text=${text}`) 
      setMessage(res.data.message)
    } catch (error) {
      console.error('Error updating message', error)
    }
  }

  return (
    <div className="App">
      <h1>My FastAPI + React Ap</h1>
      <p>{message}</p>
      <input onBlur={(e) => {updateText(e.target.value); e.target.value = ''}} placeholder='Change text...' />
    </div>
  );
}

export default App;
import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/home.css'


export default function Home() {
  const navigate = useNavigate();

  return (
      <>
      <div className="container">
          <h1>Simulation and Queuing Calculator</h1>
          <h4>Group Members:</h4>
          <ul className="member-list">
              <li><p>Mehak Fatima (B21110006057)</p></li>
              <li><p>Rimsha Laraib (B21110006107)</p></li>
              <li><p>Tahrim Bilal (B21110006153)</p></li>
              <li><p>Yumna Mubeen (B21110006165)</p></li>
          </ul>
          <h3>Submitted to: Dr Shaista Rais</h3>
          <div>
              <button onClick={() => navigate('/queue')}>Queuing calculator</button>
              <button onClick={() => navigate('/simulation')}>Simulator</button>
          </div>
      </div>
      </>
  );
}

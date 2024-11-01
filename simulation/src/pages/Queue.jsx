import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/queue.css'; 

export default function Queue() {
    const navigate = useNavigate();

    return (
        <div className="container">
            <h1>Select a Queuing Model</h1>
            <div className="model-buttons">
                <button className='model-button' onClick={() => navigate('/mm1')}>M/M/1</button>
                <button className='model-button' onClick={() => navigate('/mms')}>M/M/s</button>
                <button className='model-button' onClick={() => navigate('/mg1')}>M/G/1</button>
                <button className='model-button' onClick={() => navigate('/mgs')}>M/G/s</button>
                <button className='model-button' onClick={() => navigate('/gg1')}>G/G/1</button>
                <button className='model-button' onClick={() => navigate('/ggs')}>G/G/s</button>
            </div>
        </div>
    );
}

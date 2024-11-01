// import React, { useState } from 'react';

// const MM1 = () => {
//     const [meanInterarrival, setMeanInterarrival] = useState('');
//     const [meanService, setMeanService] = useState('');
//     const [result, setResult] = useState(null);
//     const [error, setError] = useState('');

//     const calculateMetrics = () => {
//         const lam = 1 / meanInterarrival; // Arrival rate (lambda)
//         const meu = 1 / meanService;      // Service rate (mu)
//         const rho = meanService / meanInterarrival; // Utilization rate (rho)

//         if (rho >= 1) {
//             setError("Utilization (rho) cannot be greater than or equal to 1.");
//             setResult(null);
//             return;
//         }

//         // Calculating metrics
//         const Lq= (rho ** 2) / (1 - rho);
//         const Wq = Lq/ lam;
//         const Ws = Wq + (1 / meu);
//         const Ls = Ws * lam;
//         const idle = 1 - rho;

//         // Setting results
//         setResult({
//             Lq,
//             Wq,
//             Ws,
//             Ls,
//             idle,
//         });
//         setError(''); // Clear previous errors
//     };

//     return (
//         <div>
//             <h2>MM1 Queue Model</h2>
//             <div>
//                 <label>
//                     Mean Interarrival Time:
//                     <input 
//                         type="number" 
//                         value={meanInterarrival} 
//                         onChange={(e) => setMeanInterarrival(e.target.value)} 
//                     />
//                 </label>
//                 <br />
//                 <label>
//                     Mean Service Time:
//                     <input 
//                         type="number" 
//                         value={meanService} 
//                         onChange={(e) => setMeanService(e.target.value)} 
//                     />
//                 </label>
//                 <br />
//                 <button onClick={calculateMetrics}>Calculate</button>
//             </div>
// {error ? (
//         <p style={{ color: "red" }}>{error}</p>
//       ) : (
//         result && (
//           <div style={{ marginTop: "20px" }}>
//             <h3>Performance Metrics</h3>
//             <p>
//               Average number of customers in the system (Ls):{" "}
//               {result.Ls.toFixed(3)}
//             </p>
//             <p>
//               Average time a customer spends in the system (Ws):{" "}
//               {result.Ws.toFixed(3)} minutes
//             </p>
//             <p>
//               Average number of customers in the queue (Lq):
//               {result.Lq.toFixed(3)}
//             </p>
//             <p>
//               Average time a customer spends waiting in the queue (Wq):{" "}
//               {result.Wq.toFixed(3)} minutes
//             </p>
//             <p>Time the server was idle:{result.idle.toFixed(3)}</p>
//             <p>Time the server was busy: {result.p.toFixed(2)}</p>
//             {/* <p>Coefficient of variation of service time (Cs²): {result.Cs2.toFixed(3)}</p>
//                 <p>Coefficient of variation of arrival process (Ca²): {result.Ca2.toFixed(3)}</p> */}
//           </div>
//         )
//       )}
//     </div>
//   );
// };

// export default MM1;


import React, { useState } from 'react';

const MM1 = () => {
    const [meanInterarrival, setMeanInterarrival] = useState('');
    const [meanService, setMeanService] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState('');

    const calculateMetrics = () => {
        // Input validation
        if (!meanInterarrival || !meanService) {
            setError("Both mean interarrival time and mean service time must be provided.");
            setResult(null);
            return;
        }

        // Parse inputs to floats for calculation
        const lam = 1 / parseFloat(meanInterarrival); // Arrival rate (lambda)
        const meu = 1 / parseFloat(meanService);      // Service rate (mu)

        // Utilization calculation
        const rho = lam / meu; // Utilization rate (rho)

        if (rho >= 1) {
            setError("Utilization (rho) cannot be greater than or equal to 1.");
            setResult(null);
            return;
        }

        // Calculating metrics
        const Lq = (rho ** 2) / (1 - rho); // Average number of customers in queue
        const Wq = Lq / lam; // Average wait time in queue
        const Ws = Wq + (1 / meu); // Average time spent in the system
        const Ls = Ws * lam; // Average number of customers in the system
        const idle = 1 - rho; // Proportion of time server is idle

        // Setting results
        setResult({
            Lq,
            Wq,
            Ws,
            Ls,
            idle,
            rho, // Include utilization in the result for display
        });
        setError(''); // Clear previous errors
    };

    return (
        <div>
            <h2>MM1 Queue Model</h2>
            <div>
                <label>
                    Mean Interarrival Time:
                    <input 
                        type="number" 
                        value={meanInterarrival} 
                        onChange={(e) => setMeanInterarrival(e.target.value)} 
                    />
                </label>
                <br />
                <label>
                    Mean Service Time:
                    <input 
                        type="number" 
                        value={meanService} 
                        onChange={(e) => setMeanService(e.target.value)} 
                    />
                </label>
                <br />
                <button onClick={calculateMetrics}>Calculate</button>
            </div>
            {error ? (
                <p style={{ color: "red" }}>{error}</p>
            ) : (
                result && (
                    <div style={{ marginTop: "20px" }}>
                        <h3>Performance Metrics</h3>
                        <p>Average number of customers in the system (Ls): {result.Ls.toFixed(3)}</p>
                        <p>Average time a customer spends in the system (Ws): {result.Ws.toFixed(3)} minutes</p>
                        <p>Average number of customers in the queue (Lq): {result.Lq.toFixed(3)}</p>
                        <p>Average time a customer spends waiting in the queue (Wq): {result.Wq.toFixed(3)} minutes</p>
                        <p>Time the server was idle: {result.idle.toFixed(3)}</p>
                        <p>Time the server was busy: {result.rho.toFixed(2)}</p>
                    </div>
                )
            )}
        </div>
    );
};

export default MM1;

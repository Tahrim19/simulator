import React, { useState } from "react";

const GG1 = () => {
  // State variables for user inputs
  const [interArrivalDistribution, setInterArrivalDistribution] =
    useState("gamma");
  const [serviceDistribution, setServiceDistribution] = useState("gamma");

  const [meanInterArrival, setMeanInterArrival] = useState("");
  const [varianceInterArrival, setVarianceInterArrival] = useState("");

  const [meanService, setMeanService] = useState("");
  const [varianceService, setVarianceService] = useState("");

  const [minInterArrival, setMinInterArrival] = useState("");
  const [maxInterArrival, setMaxInterArrival] = useState("");

  const [minService, setMinService] = useState("");
  const [maxService, setMaxService] = useState("");

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const calculateQueueMetrics = () => {
    try {
      const lamda = parseFloat(meanInterArrival);
      const mu = parseFloat(meanService);

      if (lamda <= 0 || mu <= 0) {
        setError("Mean inter-arrival and service times must be positive.");
        return;
      }

      const p = mu / lamda; // Utilization factor
      const Ca2 = parseFloat(varianceInterArrival) / Math.pow(lamda, 2);
      const Cs2 = parseFloat(varianceService) / Math.pow(mu, 2);

      if (p >= 1) {
        setError(
          "System is overloaded (p >= 1). Infinite queue and wait times expected."
        );
        return;
      }

      const Lq =
        (Math.pow(p, 2) * (1 + Cs2) * (Ca2 + Math.pow(p, 2) * Cs2)) /
        (2 * (1 - p) * (1 + Math.pow(p, 2) * Cs2));
      const Wq = Lq / (1 / lamda);
      const Ws = Wq + 1 / (1 / mu);
      const Ls = (1 / lamda) * Ws;
      const idle = 1 - p;

      setResult({
        p,
        Ca2,
        Cs2,
        Lq,
        Wq,
        Ws,
        Ls,
        idle,
      });
      setError(null);
    } catch (err) {
      setError("Error in calculation. Please check your input values.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h2>G/G/1 Queue Calculator</h2>

      <div>
        <h3>Inter-arrival Time Distribution</h3>
        <label>
          Distribution Type:
          <select
            value={interArrivalDistribution}
            onChange={(e) => setInterArrivalDistribution(e.target.value)}
          >
            <option value="gamma">Gamma</option>
            <option value="uniform">Uniform</option>
            <option value="normal">Normal</option>
          </select>
        </label>

        {interArrivalDistribution === "gamma" && (
          <>
            <label>
              Mean Inter-arrival Time:
              <input
                type="number"
                value={meanInterArrival}
                onChange={(e) => setMeanInterArrival(e.target.value)}
              />
            </label>
            <label>
              Variance Inter-arrival Time:
              <input
                type="number"
                value={varianceInterArrival}
                onChange={(e) => setVarianceInterArrival(e.target.value)}
              />
            </label>
          </>
        )}

        {interArrivalDistribution === "uniform" && (
          <>
            <label>
              Min Inter-arrival Time:
              <input
                type="number"
                value={minInterArrival}
                onChange={(e) => setMinInterArrival(e.target.value)}
              />
            </label>
            <label>
              Max Inter-arrival Time:
              <input
                type="number"
                value={maxInterArrival}
                onChange={(e) => setMaxInterArrival(e.target.value)}
              />
            </label>
          </>
        )}

        {interArrivalDistribution === "normal" && (
          <>
            <label>
              Mean Inter-arrival Time:
              <input
                type="number"
                value={meanInterArrival}
                onChange={(e) => setMeanInterArrival(e.target.value)}
              />
            </label>
            <label>
              Variance Inter-arrival Time:
              <input
                type="number"
                value={varianceInterArrival}
                onChange={(e) => setVarianceInterArrival(e.target.value)}
              />
            </label>
          </>
        )}
      </div>

      <div>
        <h3>Service Time Distribution</h3>
        <label>
          Distribution Type:
          <select
            value={serviceDistribution}
            onChange={(e) => setServiceDistribution(e.target.value)}
          >
            <option value="gamma">Gamma</option>
            <option value="uniform">Uniform</option>
            <option value="normal">Normal</option>
          </select>
        </label>

        {serviceDistribution === "gamma" && (
          <>
            <label>
              Mean Service Time:
              <input
                type="number"
                value={meanService}
                onChange={(e) => setMeanService(e.target.value)}
              />
            </label>
            <label>
              Variance Service Time:
              <input
                type="number"
                value={varianceService}
                onChange={(e) => setVarianceService(e.target.value)}
              />
            </label>
          </>
        )}

        {serviceDistribution === "uniform" && (
          <>
            <label>
              Min Service Time:
              <input
                type="number"
                value={minService}
                onChange={(e) => setMinService(e.target.value)}
              />
            </label>
            <label>
              Max Service Time:
              <input
                type="number"
                value={maxService}
                onChange={(e) => setMaxService(e.target.value)}
              />
            </label>
          </>
        )}

        {serviceDistribution === "normal" && (
          <>
            <label>
              Mean Service Time:
              <input
                type="number"
                value={meanService}
                onChange={(e) => setMeanService(e.target.value)}
              />
            </label>
            <label>
              Variance Service Time:
              <input
                type="number"
                value={varianceService}
                onChange={(e) => setVarianceService(e.target.value)}
              />
            </label>
          </>
        )}
      </div>

      <button onClick={calculateQueueMetrics}>Calculate</button>
      {error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : (
        result && (
          <div style={{ marginTop: "20px" }}>
            <h3>Performance Metrics</h3>
            <p>
              Average number of customers in the system (Ls):{" "}
              {result.Ls.toFixed(3)}
            </p>
            <p>
              Average time a customer spends in the system (Ws):{" "}
              {result.Ws.toFixed(3)} minutes
            </p>
            <p>
              Average number of customers in the queue (Lq):
              {result.Lq.toFixed(3)}
            </p>
            <p>
              Average time a customer spends waiting in the queue (Wq):{" "}
              {result.Wq.toFixed(3)} minutes
            </p>
            <p>Time the server was idle:{result.idle.toFixed(3)}</p>
            <p>Time the server was busy: {result.p.toFixed(2)}</p>
            {/* <p>Coefficient of variation of service time (Cs²): {result.Cs2.toFixed(3)}</p>
                <p>Coefficient of variation of arrival process (Ca²): {result.Ca2.toFixed(3)}</p> */}
          </div>
        )
      )}
    </div>
  );
};

export default GG1;

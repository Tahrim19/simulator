import React, { useState } from "react";

const MGS = () => {
  const [interArrivalTime, setInterArrivalTime] = useState("");
  const [serviceDistribution, setServiceDistribution] = useState("normal");
  const [meanServiceTime, setMeanServiceTime] = useState("");
  const [stdDevServiceTime, setStdDevServiceTime] = useState("");
  const [minServiceTime, setMinServiceTime] = useState("");
  const [maxServiceTime, setMaxServiceTime] = useState("");
  const [shapeParam, setShapeParam] = useState("");
  const [scaleParam, setScaleParam] = useState("");
  const [numServers, setNumServers] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const calculateMetrics = () => {
    const lambdaRate = 1 / interArrivalTime;
    let mu, sigmaS2;

    if (serviceDistribution === "normal") {
      mu = 1 / meanServiceTime;
      sigmaS2 = stdDevServiceTime ** 2;
    } else if (serviceDistribution === "uniform") {
      mu = 1 / ((parseFloat(minServiceTime) + parseFloat(maxServiceTime)) / 2);
      sigmaS2 = (maxServiceTime - minServiceTime) ** 2 / 12;
    } else if (serviceDistribution === "gamma") {
      mu = 1 / (shapeParam * scaleParam);
      sigmaS2 = shapeParam * scaleParam ** 2;
    } else {
      setError("Unsupported distribution type.");
      return;
    }

    const s = parseInt(numServers);
    const rho = lambdaRate / (s * mu);

    if (rho >= 1) {
      setError(
        "Utilization factor cannot be 1 or greater. Please adjust λ or the number of servers."
      );
      return;
    }

    // Calculate performance metrics
    const L =
      lambdaRate * mu + (lambdaRate ** 2 * sigmaS2) / (2 * s * (1 - rho));
    const W = L / lambdaRate;
    const Lq = L - lambdaRate / mu;
    const Wq = Lq / lambdaRate;
    const idleTime = 1 - rho;

    // Set results
    setResult({
      L,
      W,
      Lq,
      Wq,
      idleTime,
      utilization: rho,
    });
    setError(""); // Clear previous errors
  };

  return (
    <div>
      <h2>M/G/s Queue Model</h2>
      <div>
        <label>
          Inter-arrival time:
          <input
            type="number"
            value={interArrivalTime}
            onChange={(e) => setInterArrivalTime(e.target.value)}
          />
        </label>
        <label>
          Service Time Distribution:
          <select
            value={serviceDistribution}
            onChange={(e) => setServiceDistribution(e.target.value)}
          >
            <option value="normal">Normal</option>
            <option value="uniform">Uniform</option>
            <option value="gamma">Gamma</option>
          </select>
        </label>
        {serviceDistribution === "normal" && (
          <>
            <label>
              Mean Service Time:
              <input
                type="number"
                value={meanServiceTime}
                onChange={(e) => setMeanServiceTime(e.target.value)}
              />
            </label>
            <label>
              Standard Deviation of Service Time:
              <input
                type="number"
                value={stdDevServiceTime}
                onChange={(e) => setStdDevServiceTime(e.target.value)}
              />
            </label>
          </>
        )}
        {serviceDistribution === "uniform" && (
          <>
            <label>
              Minimum Service Time:
              <input
                type="number"
                value={minServiceTime}
                onChange={(e) => setMinServiceTime(e.target.value)}
              />
            </label>
            <label>
              Maximum Service Time:
              <input
                type="number"
                value={maxServiceTime}
                onChange={(e) => setMaxServiceTime(e.target.value)}
              />
            </label>
          </>
        )}
        {serviceDistribution === "gamma" && (
          <>
            <label>
              Shape Parameter (k):
              <input
                type="number"
                value={shapeParam}
                onChange={(e) => setShapeParam(e.target.value)}
              />
            </label>
            <label>
              Scale Parameter (θ):
              <input
                type="number"
                value={scaleParam}
                onChange={(e) => setScaleParam(e.target.value)}
              />
            </label>
          </>
        )}
        <label>
          Number of Servers (s):
          <input
            type="number"
            value={numServers}
            onChange={(e) => setNumServers(e.target.value)}
          />
        </label>
        <button onClick={calculateMetrics}>Calculate</button>
      </div>
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

export default MGS;

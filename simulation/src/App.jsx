import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home'; 
import Queue from './pages/Queue'; 
import Simulation from './pages/Simulation'; 
import MG1 from './components/MG1';
import MGS from './components/MGS';
import MM1 from './components/MM1';
import MMS from './components/MMS';
import GG1 from './components/GG1';
import GGS from './components/GGS';
import MMSimulate from './simulate/MMSimulate'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/queue" element={<Queue />} />
        <Route path="/simulation" element={<Simulation />} />
        <Route path='/mm1' element={<MM1/>}/>
        <Route path='/mms' element={<MMS/>}/>
        <Route path='/mg1' element={<MG1/>}/>
        <Route path='/mgs' element={<MGS/>}/>
        <Route path='/gg1' element={<GG1/>}/>
        <Route path='/ggs' element={<GGS/>}/>
        <Route path='/mmSimulate' element={<MMSimulate/>}/>

      </Routes>
    </Router>
  );
}

export default App;



// // home -> proj heading name and seatno. user option quwuing ye simulation
// // route to queue = user option which queue => route to new 
// // route to simualtion








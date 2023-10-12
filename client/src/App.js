import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './assets/Navbar';
import Hero from './pages/Hero';
import HeroDetail from './pages/HeroDetail';
import Admin from './pages/Admin';
import HeroList from './pages/HeroList';
import AddHero from './pages/AddHero'; 
import EditHero from './pages/EditHero';
import PowerList from './pages/PowerList';
import AddPower from './pages/AddPower';
import HeroPower from './pages/HeroPower';

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/hero/:id" element={<HeroDetail />} />
        <Route path="/admin" element={<Admin />}>
          <Route path="heroes" element={<HeroList />} />
          <Route path="heroes/add" element={<AddHero />} />
          <Route path="heroes/:id/edit" element={<EditHero />} />
          <Route path="powers" element={<PowerList/>} />
          <Route path="powers/add" element={<AddPower />} />
          <Route path="create_hp" element={<HeroPower />} />
          {/* <Route path="profile" element={<Profile />} /> */}
        </Route>
      </Routes>
    </>
  );
}

export default App;

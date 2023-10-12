import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import SearchIcon from '@mui/icons-material/Search';
import Typography from '@mui/material/Typography';

const Hero = () => {
  const [heroes, setHeroes] = useState([]);
  const [searchText, setSearchText] = useState('');
  const [filteredHeroes, setFilteredHeroes] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/heroes')
      .then((response) => {
        setHeroes(response.data);
      })
      .catch((error) => {
        console.error('Error fetching hero data:', error);
      });
  }, []);

  // Function to handle search
  function handleSearch(event) {
    const searchTerm = event.target.value;
    setSearchText(searchTerm);

    const filteredHeroes = heroes.filter((hero) => {
      const nameMatch = hero.name.toLowerCase().includes(searchTerm.toLowerCase());
      const supernameMatch = hero.supername.toLowerCase().includes(searchTerm.toLowerCase());

      // Use a scoring system to prioritize results based on relevance
      const score = nameMatch * 2 + supernameMatch;

      return nameMatch || supernameMatch;
    });

    // Sort the filteredHeroes by their score in descending order
    filteredHeroes.sort((a, b) => {
      const scoreA = a.name.toLowerCase().includes(searchTerm.toLowerCase()) * 2 + a.supername.toLowerCase().includes(searchTerm.toLowerCase());
      const scoreB = b.name.toLowerCase().includes(searchTerm.toLowerCase()) * 2 + b.supername.toLowerCase().includes(searchTerm.toLowerCase());

      return scoreB - scoreA;
    });

    setFilteredHeroes(filteredHeroes);
  }

  const displayedHeroes = searchText.length > 0 ? filteredHeroes : heroes;

  return (
    <div className="container mt-4">
      <Typography variant="h4" align="center" style={{ marginTop: '3cm' }}>
        Welcome to the Hero App
      </Typography>
      <div className="container mt-4" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div className="mb-4" style={{ marginTop: '3cm' }}>
          <TextField
            variant="outlined"
            fullWidth
            value={searchText}
            onChange={handleSearch}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
            InputLabelProps={{
              shrink: searchText !== '',
            }}
            label="Search for a Hero"
            placeholder="Type a name or supername"
            style={{ width: '600px' }}
          />
        </div>
      </div>


      <div className="row justify-content-center" style={{ marginTop: '3cm' }}>
        {displayedHeroes.map((hero) => (
          <div className="col-md-2 mb-4" key={hero.id}>
            <Link to={`/hero/${hero.id}`} className="card-link">
              <div className="card" style={{ maxWidth: '150px', height: '60%', overflow: 'hidden' }}>
                <img
                  src={hero.image_url}
                  className="card-img-top"
                  alt={`${hero.supername} - ${hero.name}`}
                  style={{ objectFit: 'cover', width: '100%', height: '100%' }}
                />
              </div>
              <div className="mt-2 text-center">
                <h5>{hero.supername}</h5>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Hero;

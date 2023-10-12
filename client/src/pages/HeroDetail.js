import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Rate from '../assets/Rate';

const HeroDetail = () => {
  const { id } = useParams();
  const [hero, setHero] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/heroes/${id}`)
      .then((response) => {
        setHero(response.data);
      })
      .catch((error) => {
        console.error('Error fetching hero data:', error);
      });
  }, [id]);

  if (hero) {
    return (
      <div className="container mt-4">
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Card style={{ height: 'auto', maxWidth: '300px' }}>
            <CardMedia
              component="img"
              alt={hero.name}
              height="400"
              image={hero.image_url}
            />
          </Card>
          <div
            style={{
              marginLeft: '20px',
              maxWidth: '50%',
            }}
          >
            <Typography variant="h3" gutterBottom style={{ fontSize: '24px' }}>
              This is  {hero.name}
            </Typography>
            <Typography variant="h5" color="textSecondary" style={{ fontSize: '18px' }}>
              Who also goes by <span style={{ color: 'blue' }}>{hero.supername}</span>
            </Typography>
            <Typography variant="h5" color="textSecondary" style={{ fontSize: '18px' }}>
            {hero.supername} has the following powers:
            </Typography>
            <div
              style={{
                maxHeight: '200px',
                overflowY: 'auto',
              }}
            >
              <ul style={{ listStyle: 'none', padding: 0 }}>
                {hero.powers.map((power) => (
                  <li
                    key={power.name}
                  >
                    <strong>{power.name}:</strong> {power.description}
                  </li>
                ))}
                <Rate/>
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return <p>Loading...</p>;
  }
};

export default HeroDetail;

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom'; 
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Swal from 'sweetalert2';

const EditHero = () => {
  const { id } = useParams();
  const navigate = useNavigate(); 

  const [hero, setHero] = useState({
    id: '',
    name: '',
    supername: '',
    image_url: '',
  });

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/heroes/${id}`)
      .then((response) => {
        setHero(response.data);
      })
      .catch((error) => {
        console.error('Error fetching hero data:', error);
      });
  }, [id]);

  const handleSubmit = () => {
    axios.put(`http://127.0.0.1:5000/heroes/${id}/update`, hero)
      .then(() => {
        // Show a success message with SweetAlert2
        Swal.fire('Success', 'Hero updated successfully!', 'success').then(() => {
          // Redirect back to the hero list page
          navigate('/admin/heroes');
        });
      })
      .catch((error) => {
        Swal.fire('Error', 'An error occurred while updating the hero', 'error');
        console.error('Error updating hero:', error);
      });
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setHero({ ...hero, [name]: value });
  };

  return (
    <div>
      <h2>Edit Hero</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <TextField
            id="name"
            name="name"
            label="Name"
            variant="outlined"
            fullWidth
            margin="normal"
            value={hero.name}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <TextField
            id="supername"
            name="supername"
            label="Supername"
            variant="outlined"
            fullWidth
            margin="normal"
            value={hero.supername}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <TextField
            id="image_url"
            name="image_url"
            label="Image URL"
            variant="outlined"
            fullWidth
            margin="normal"
            value={hero.image_url}
            onChange={handleInputChange}
          />
        </div>
        <Button type="submit" variant="contained" color="primary">
          Update Hero
        </Button>
      </form>
    </div>
  );
};

export default EditHero;

import React, { useEffect, useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Swal from 'sweetalert2';
import MenuItem from '@mui/material/MenuItem';
import { useNavigate } from 'react-router-dom';

const HeroPower = () => {
  const navigate = useNavigate();
  const [heroes, setHeroes] = useState([]);
  const [powers, setPowers] = useState([]);

  useEffect(() => {
    // Fetch heroes from the server
    axios.get('http://127.0.0.1:5000/heroes').then((response) => {
      setHeroes(response.data);
    });

    // Fetch powers from the server
    axios.get('http://127.0.0.1:5000/powers').then((response) => {
      setPowers(response.data);
    });
  }, []);

  const initialValues = {
    strength: '',
    hero_id: '',
    power_id: '',
  };

  const validationSchema = Yup.object({
    strength: Yup.string().required('Strength is required'),
    hero_id: Yup.string().required('Hero is required'),
    power_id: Yup.string().required('Power is required'),
  });

  const handleSubmit = (values) => {
    axios
      .post('http://127.0.0.1:5000/hero_powers', values)
      .then((response) => {
        Swal.fire('Success', 'HeroPower association created successfully!', 'success').then(() => {
          navigate('/admin/heropowers');
        });
      })
      .catch((error) => {
        Swal.fire('Error', 'An error occurred while creating HeroPower association', 'error');
        console.error('Error creating HeroPower association:', error);
      });
  };

  const formik = useFormik({
    initialValues,
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <div>
      <h2>Create HeroPower Association</h2>
      <form onSubmit={formik.handleSubmit}>
        <div>
          <TextField
            id="strength"
            name="strength"
            label="Strength"
            variant="outlined"
            fullWidth
            margin="normal"
            error={formik.touched.strength && formik.errors.strength ? true : false}
            helperText={formik.touched.strength && formik.errors.strength}
            {...formik.getFieldProps('strength')}
          />
        </div>
        <div>
          <TextField
            id="hero_id"
            name="hero_id"
            label="Hero"
            variant="outlined"
            select
            fullWidth
            margin="normal"
            error={formik.touched.hero_id && formik.errors.hero_id ? true : false}
            helperText={formik.touched.hero_id && formik.errors.hero_id}
            {...formik.getFieldProps('hero_id')}
          >
            {heroes.map((hero) => (
              <MenuItem key={hero.id} value={hero.id}>
              {`${hero.id} - ${hero.name}`}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <div>
          <TextField
            id="power_id"
            name="power_id"
            label="Power"
            variant="outlined"
            select
            fullWidth
            margin="normal"
            error={formik.touched.power_id && formik.errors.power_id ? true : false}
            helperText={formik.touched.power_id && formik.errors.power_id}
            {...formik.getFieldProps('power_id')}
          >
            {powers.map((power) => (
              <MenuItem key={power.id} value={power.id}>
                {`${power.id} - ${power.name}`}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <Button type="submit" variant="contained" color="primary">
          Create HeroPower
        </Button>
      </form>
    </div>
  );
};

export default HeroPower;

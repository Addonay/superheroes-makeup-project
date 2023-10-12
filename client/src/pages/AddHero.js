import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Swal from 'sweetalert2';
import { useNavigate } from 'react-router-dom'; 

const AddHero = () => {
  const initialValues = {
    name: '',
    supername: '',
    image_url: '',
  };

  const validationSchema = Yup.object({
    name: Yup.string().required('Name is required'),
    supername: Yup.string().required('Supername is required'),
    image_url: Yup.string().url('Invalid URL').required('Image URL is required'),
  });

  const navigate = useNavigate(); 

  const handleSubmit = (values) => {
    axios
      .post('http://127.0.0.1:5000/add_hero', values)
      .then((response) => {
        Swal.fire('Success', 'Hero added successfully!', 'success').then(() => {
          navigate('/admin/heroes');
        });
      })
      .catch((error) => {
        Swal.fire('Error', 'An error occurred while adding the hero', 'error');
        console.error('Error adding hero:', error);
      });
  };

  const formik = useFormik({
    initialValues,
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <div>
      <h2>Add Hero</h2>
      <form onSubmit={formik.handleSubmit}>
        <div>
          <TextField
            id="name"
            name="name"
            label="Name"
            variant="outlined"
            fullWidth
            margin="normal"
            error={formik.touched.name && formik.errors.name ? true : false}
            helperText={formik.touched.name && formik.errors.name}
            {...formik.getFieldProps('name')}
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
            error={formik.touched.supername && formik.errors.supername ? true : false}
            helperText={formik.touched.supername && formik.errors.supername}
            {...formik.getFieldProps('supername')}
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
            error={formik.touched.image_url && formik.errors.image_url ? true : false}
            helperText={formik.touched.image_url && formik.errors.image_url}
            {...formik.getFieldProps('image_url')}
          />
        </div>
        <Button type="submit" variant="contained" color="primary">
          Add Hero
        </Button>
      </form>
    </div>
  );
};

export default AddHero;

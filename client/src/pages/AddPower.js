import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Swal from 'sweetalert2';
import { useNavigate } from 'react-router-dom';

const AddPower = () => {
  const navigate = useNavigate();

  const initialValues = {
    name: '',
    description: '',
  };

  const validationSchema = Yup.object({
    name: Yup.string().required('Name is required'),
    description: Yup.string().required('Description is required'),
  });

  const handleSubmit = (values) => {
    axios
      .post('http://127.0.0.1:5000/add_power', values) 
      .then((response) => {
        Swal.fire('Success', 'Power added successfully!', 'success').then(() => {
          navigate('/admin/powers');
        });
      })
      .catch((error) => {
        Swal.fire('Error', 'An error occurred while adding the power', 'error');
        console.error('Error adding power:', error);
      });
  };

  const formik = useFormik({
    initialValues,
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <div>
      <h2>Add Power</h2>
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
            id="description"
            name="description"
            label="Description"
            variant="outlined"
            fullWidth
            margin="normal"
            error={formik.touched.description && formik.errors.description ? true : false}
            helperText={formik.touched.description && formik.errors.description}
            {...formik.getFieldProps('description')}
          />
        </div>
        <Button type="submit" variant="contained" color="primary">
          Add Power
        </Button>
      </form>
    </div>
  );
};

export default AddPower;

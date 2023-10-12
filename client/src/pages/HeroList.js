import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import { Link } from 'react-router-dom';
import Swal from 'sweetalert2';

const buttonStyle = {
  margin: '4px',
  padding: '8px',
};

const HeroList = () => {
  const [heroes, setHeroes] = useState([]);

  useEffect(() => {
    // Fetch heroes from your server's API endpoint
    axios
      .get('http://127.0.0.1:5000/heroes')
      .then((response) => {
        setHeroes(response.data);
        // Add an empty row at the end
        setHeroes([...response.data, { id: '', name: '', supername: '', image_url: '' }]);
      })
      .catch((error) => {
        console.error('Error fetching hero data:', error);
      });
  }, []);

  const handleDelete = (id, name) => {
    // Show a confirmation dialog with SweetAlert2
    Swal.fire({
      title: `Are you sure you want to delete ${name}?`,
      text: 'This action cannot be undone.',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it',
      cancelButtonText: 'No, cancel',
    }).then((result) => {
      if (result.isConfirmed) {
        // Send a DELETE request to the server to delete the hero
        axios
          .delete(`http://127.0.0.1:5000/heroes/${id}/delete`)
          .then(() => {
            // If the deletion is successful, remove the hero from the state
            setHeroes(heroes.filter((hero) => hero.id !== id));
            // Show a success message with SweetAlert2
            Swal.fire('Deleted!', `${name} has been successfully deleted.`, 'success');
          })
          .catch((error) => {
            console.error('Error deleting hero:', error);
            Swal.fire('Error', 'An error occurred while deleting the hero.', 'error');
          });
      }
    });
  };

  return (
    <div>
      <h2>Hero List</h2>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Supername</TableCell>
              <TableCell>Image</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {heroes.map((hero) => (
              <TableRow key={hero.id}>
                <TableCell>
                  {hero.id === '' ? (
                    <Button
                      component={Link}
                      to="/admin/heroes/add"
                      variant="contained"
                      color="primary"
                      startIcon={<AddIcon />}
                      style={buttonStyle}
                    >
                      Add
                    </Button>
                  ) : hero.id}
                </TableCell>
                <TableCell>{hero.name}</TableCell>
                <TableCell>{hero.supername}</TableCell>
                <TableCell>
                  <img src={hero.image_url} alt={hero.name} style={{ width: '50px' }} />
                </TableCell>
                <TableCell>
                  {hero.id !== '' && (
                    <>
                      <Button
                        component={Link}
                        to={`/admin/heroes/${hero.id}/edit`} 
                        variant="contained"
                        color="primary"
                        startIcon={<EditIcon />}
                        style={buttonStyle}
                      >
                        Edit
                      </Button>
                      <Button
                        variant="contained"
                        color="secondary"
                        startIcon={<DeleteIcon />}
                        style={buttonStyle}
                        onClick={() => handleDelete(hero.id, hero.name)}
                      >
                        Delete
                      </Button>
                    </>
                  )}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default HeroList;

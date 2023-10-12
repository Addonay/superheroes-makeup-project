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
import AddIcon from '@mui/icons-material/Add';
import { Link } from 'react-router-dom';

const buttonStyle = {
  margin: '4px',
  padding: '8px',
};

const PowerList = () => {
  const [powers, setPowers] = useState([]);

  useEffect(() => {
    // Fetch powers from your server's API endpoint
    axios
      .get('http://127.0.0.1:5000/powers')
      .then((response) => {
        setPowers(response.data);
        // Add an empty row at the end
        setPowers([...response.data, { id: '', name: '', description: '' }]);
      })
      .catch((error) => {
        console.error('Error fetching power data:', error);
      });
  }, []);


  return (
    <div>
      <h2>Powers List</h2>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {powers.map((power) => (
              <TableRow key={power.id}>
                <TableCell>
                  {power.id === '' ? (
                    <Button
                      component={Link}
                      to="/admin/powers/add"
                      variant="contained"
                      color="primary"
                      startIcon={<AddIcon />}
                      style={buttonStyle}
                    >
                      Add
                    </Button>
                  ) : power.id}
                </TableCell>
                <TableCell>{power.name}</TableCell>
                <TableCell>{power.description}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default PowerList;

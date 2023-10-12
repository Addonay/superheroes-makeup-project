import React from 'react';
import { useNavigate, Outlet } from 'react-router-dom';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';

const Admin = () => {
  const navigate = useNavigate();

  const handleContentChange = (content) => {
      navigate(`/admin/${content.toLowerCase()}`);
  }

  return (
    <Container maxWidth="lg" style={{ display: 'flex', height: '100vh',marginTop:"2cm" }}>
      <Grid container spacing={2} style={{ flex: 1 }}>
        <Grid item xs={3}>
          <Paper elevation={3} style={{ height: '100%' }}>
            <Typography variant="h5" align="center" style={{ padding: '20px', marginBottom: '20px' }}>
              Dashboard
            </Typography>
            <List component="nav" aria-label="admin sidebar">
              <ListItemButton
                onClick={() => handleContentChange('Heroes')}
              >
                <ListItemText primary="Heroes" />
              </ListItemButton>
              <ListItemButton
                onClick={() => handleContentChange('Powers')}
              >
                <ListItemText primary="Powers" />
              </ListItemButton>
              <ListItemButton
                onClick={() => handleContentChange('Create_HP')}
              >
                <ListItemText primary="Create HeroPower" />
              </ListItemButton>
            </List>
          </Paper>
        </Grid>
        <Grid item xs={9}>
          <Paper elevation={3} style={{ padding: '20px', height: '100%' }}>
            <Typography variant="h5" gutterBottom>
              <Outlet />
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Admin;

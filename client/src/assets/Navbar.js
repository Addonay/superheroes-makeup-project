import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import useMediaQuery from '@mui/material/useMediaQuery'; 
import HomeIcon from '@mui/icons-material/Home';
import SupervisorAccountIcon from '@mui/icons-material/SupervisorAccount';

function Navbar() {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const isMobile = useMediaQuery('(max-width:900px)');

  return (
    <div>
      <AppBar position="fixed" sx={{ backgroundColor: 'transparent', boxShadow: 'none', border: 'none' }}>
        <Toolbar sx={{ display: 'flex' }}>
          <Typography variant="h4" component="div" sx={{ flexGrow: 1 }} style={{ textDecoration: 'none', color: 'orange' }}>
            SuperHero
          </Typography>
          {isMobile ? (
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ display: { xs: 'block', md: 'none' } }}
              onClick={handleMenuClick}
            >
              <MenuIcon />
            </IconButton>
          ) : (
            <div>
            <Link to="/" style={{ textDecoration: 'none', color: 'white' }}>
              <HomeIcon sx={{ fontSize: 28, verticalAlign: 'middle', mr: 2 }} />
            </Link>

            <Link to="/admin/heroes" style={{ textDecoration: 'none', color: 'white' }}>
              <SupervisorAccountIcon sx={{ fontSize: 28, verticalAlign: 'middle', mr: 2 }} />
            </Link>
          </div>
          )}
        </Toolbar>
      </AppBar>

      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleMenuClose}
      >
        <MenuItem onClick={handleMenuClose}>
          <Link to="/" style={{ textDecoration: 'none', color: 'black' }}>
            Home
          </Link>
        </MenuItem>
        <MenuItem onClick={handleMenuClose}>
          <Link to="/admin/heroes" style={{ textDecoration: 'none', color: 'black' }}>
            Admin
          </Link>
        </MenuItem>
      </Menu>
    </div>
  );
}

export default Navbar;

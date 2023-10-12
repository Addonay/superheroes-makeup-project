import React, { useState } from 'react';
import IconButton from '@mui/material/IconButton';
import StarIcon from '@mui/icons-material/Star';
import StarBorderIcon from '@mui/icons-material/StarBorder';
import { styled } from '@mui/system';

const useStyles = styled((theme) => ({
  star: {
    color: 'transparent',
    transition: 'color 0.3s',
    '&&.hovered': {
      color: 'yellow',
    },
  },
}));

const Rate = () => {
  const classes = useStyles();
  const [rating, setRating] = useState(0);
  const [hover, setHover] = useState(0);

  return (
    <div className="star-rating">
      {[...Array(5)].map((_, index) => {
        const starIndex = index + 1;
        return (
          <IconButton
            key={starIndex}
            className={`${classes.star} ${starIndex <= (hover || rating) ? 'hovered' : ''}`}
            onClick={() => setRating(starIndex)}
            onMouseEnter={() => setHover(starIndex)}
            onMouseLeave={() => setHover(rating)}
          >
            {starIndex <= (hover || rating) ? <StarIcon /> : <StarBorderIcon />}
          </IconButton>
        );
      })}
    </div>
  );
};

export default Rate;

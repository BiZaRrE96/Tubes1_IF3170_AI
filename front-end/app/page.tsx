
import React from 'react';
import MagicCube from './components/MagicCube';

export default function Home() {
  return (
    <div className='relative'>
      <div className='absolute'>
        <MagicCube />
      </div>
    </div>
  );
}

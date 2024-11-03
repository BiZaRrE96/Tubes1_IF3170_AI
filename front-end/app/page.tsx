import React from 'react';
import MagicCube from './components/MagicCube';

export default function Home() {
  return (
    <main className="w-full wrapper space-y-4 flex flex-col items-center">
      <div className='w-full flex items-center justify-between text-white font-medium'>
        <h1>Pencarian Solusi Diagonal Magic Cube dengan Local Search</h1>
        <p>Tugas Besar 1 IF3070</p>
      </div>
      <div className='flex items-start justify-between'>
        <div>

        </div>
        <div className='w-full h-full z-20'>
          <MagicCube />
        </div>
      </div>
    </main>
  );
}

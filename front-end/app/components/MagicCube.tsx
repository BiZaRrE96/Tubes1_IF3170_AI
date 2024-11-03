'use client'
import React, { useMemo } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry';
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader';
import robotoFontUrl from 'three/examples/fonts/helvetiker_regular.typeface.json';

const generateRandomNumbers = (size: number) => {
  return Array.from({ length: size * size * size }, () => Math.floor(Math.random() * 100));
};

const Cube = ({ position, number }: { position: [number, number, number]; number: number }) => {
  const font = useMemo(() => new FontLoader().parse(robotoFontUrl), []);
  const textGeometry = useMemo(() => {
    const geometry = new TextGeometry(`${number}`, {
      font,
      size: 0.3,
      height: 0.05,
    });
    geometry.center(); // Centers the text within the geometry
    return geometry;
  }, [font, number]);

  return (
    <group position={position}>
      <mesh geometry={textGeometry}>
        <meshStandardMaterial color="white" /> {/* Mengatur warna teks menjadi hitam */}
      </mesh>
    </group>
  );
};

const MagicCube = () => {
  const size = 5;
  const spacing = 1.5;
  const randomNumbers = generateRandomNumbers(size);

  return (
    <div className="w-full h-full border-2 border-black rounded-xl">
      <Canvas camera={{ position: [0, 0, 10] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <OrbitControls enableZoom={true} />
        {Array.from({ length: size }).map((_, x) =>
          Array.from({ length: size }).map((_, y) =>
            Array.from({ length: size }).map((_, z) => {
              const index = x * size * size + y * size + z;
              const number = randomNumbers[index];
              return (
                <Cube
                  key={`${x}-${y}-${z}`}
                  position={[x * spacing - (size * spacing) / 2, y * spacing - (size * spacing) / 2, z * spacing - (size * spacing) / 2]}
                  number={number}
                />
              );
            })
          )
        )}
      </Canvas>
    </div>
  )
}

export default MagicCube
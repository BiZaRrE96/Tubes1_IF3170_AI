'use client'

import React, { useMemo, useRef } from 'react';
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry';
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader';
import poppinsFontUrl from '@/app/fonts/Poppins_Regular.json'

const generateRandomNumbers = (size: number) => {
  return Array.from({ length: size * size * size }, () => Math.floor(Math.random() * 100));
};

const Cube = ({ position, number }: { position: [number, number, number]; number: number }) => {
  const font = useMemo(() => new FontLoader().parse(poppinsFontUrl), []);
  const textMeshRef = useRef<THREE.Mesh>(null!);
  const { camera } = useThree();

  useFrame(() => {
    if (textMeshRef.current) {
      textMeshRef.current.quaternion.copy(camera.quaternion);
    }
  });

  const textGeometry = useMemo(() => {
    const geometry = new TextGeometry(`${number}`, {
      font,
      size: 0.3,
      height: 0.05,
    });
    geometry.center();

    const colors = [];
    const color1 = new THREE.Color(0x0000FF); 
    const color2 = new THREE.Color(0x8E54E9); 

    for (let i = 0; i < geometry.attributes.position.count; i++) {
      const y = geometry.attributes.position.getY(i);
      const color = color1.clone().lerp(color2, (y + 0.5) / 1.0);
      colors.push(color.r, color.g, color.b);
    }
    geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
    return geometry;
  }, [font, number]);

  return (
    <group position={position}>
      <mesh ref={textMeshRef} geometry={textGeometry}>
        <meshStandardMaterial 
          vertexColors={true} 
          emissive={new THREE.Color(0xffffff)} emissiveIntensity={0.5}
        /> 
      </mesh>
    </group>
  );
};

const MagicCube = ({ 
  numbers 
}: {
  numbers: number[] | undefined
}) => {
  const size = 5;
  const spacing = 1.5;
  const randomNumbers = numbers

  return (
    <div className="w-full h-full border-2 border-black rounded-xl flex items-center justify-center">
      {numbers ? (
        <Canvas camera={{ position: [0, 0, 10] }}>
          <ambientLight intensity={0.5} />
          <pointLight position={[10, 10, 10]} />
          <OrbitControls enableZoom={true} />
          {Array.from({ length: size }).map((_, x) =>
            Array.from({ length: size }).map((_, y) =>
              Array.from({ length: size }).map((_, z) => {
                const index = x * size * size + y * size + z;
                // @ts-ignore
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
      ) : (
        <h1 className='text-white font-medium text-xl'>No Cube Generated</h1>
      )}
    </div>
  )
}

export default MagicCube
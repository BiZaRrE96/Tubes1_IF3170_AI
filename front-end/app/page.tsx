'use client'

import React, { useEffect, useState } from 'react';
import MagicCube from './components/MagicCube';
import { Button } from '@/components/ui/button';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
import Title from './components/Title';

export default function Home() {
  const [executionTime, setExecutionTime] = useState(0.00)
  const [algorithm, setAlgorithm] = useState("")
  const [cubeResult, setCubeResult] = useState();
  const [loading, setLoading] = useState(false);
  const [direction, setDirection] = useState<'horizontal' | 'vertical'>('horizontal');

  const generateCube = async () => {
    setLoading(true)
    try {
      const n = 125;
      const response = await fetch(`/api/generate-cube?n=${n}&straight=false`)
      const data = await response.json()
      setCubeResult(data)  
    } catch (error) {
      console.error("Failed to fetch:", error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 768) {
        setDirection('vertical');
      } else {
        setDirection('horizontal');
      }
    };

    handleResize();

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <main className="w-full wrapper space-y-4 flex flex-col items-center transition-all">
      {/* Title */}
      <Title />

      {/* Algorithm */}
      <ResizablePanelGroup direction={direction} className='flex flex-row items-start justify-between w-full gap-x-8'>
        {/* Choose Algoritma */}
        <ResizablePanel defaultSize={40} className='text-white flex flex-col items-start'>
          <h3 className='text-2xl font-bold'>Choose The Algorithm 🚀</h3>
          <div className='py-4 flex items-center gap-x-4 gap-y-4 flex-wrap z-20'>
            <Button 
              variant={"outline"} 
              className='bg-white/10 text-white py-4'
              onClick={generateCube}
              disabled={loading}
            >
              {loading ? "Generating Cube..." : "Generate Cube"}
            </Button>
            <div className='space-y-2'>
              <p>Hill Climbing</p>
              <div className='flex gap-4 flex-wrap'>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Steepest Ascent Hill-Climbing
                </Button>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Stochastic Hil Climbing
                </Button>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Hill-Climbing With Sideways Move
                </Button>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Random Restart Hill-Climbing
                </Button>
              </div>
            </div>
            <div className='space-y-2'>
              <p>Other Algorithm</p>
              <div className='flex gap-x-4 gap-y-2 flex-wrap'>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Simulated Annealing
                </Button>
                <Button variant={"outline"} className='bg-white/10 text-white'>
                  Genetic Algorithm
                </Button>
              </div>
            </div>
          </div>
          {/* Result Box */}
          <div className='w-full border-t-2 border-white/25 mt-4 py-4'>
            <p>Time Execition : {executionTime}</p>
          </div>
        </ResizablePanel>
        <ResizableHandle className='z-20 w-[1px] bg-white h-[550px] hidden md:block' withHandle />
        
        {/* Magic Cube Display */}
        <ResizablePanel defaultSize={60} className='hidden md:block border-2 border-white/10 rounded-lg p-0 margin-0 h-[550px]'>
          <MagicCube numbers={cubeResult} />
        </ResizablePanel>
      </ResizablePanelGroup>
    </main>
  );
}

'use client'

import React, { useState } from 'react';
import MagicCube from './components/MagicCube';
import { Button } from '@/components/ui/button';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

export default function Home() {
  const [executionTime, setExecutionTime] = useState(0.00)

  return (
    <main className="w-full wrapper space-y-4 flex flex-col items-center transition-all">
      {/* Title */}
      <div className='w-full flex items-center justify-between text-white font-medium mb-4'>
        <h1>🧑🏻‍🚀 Search for Diagonal Magic Cube Solutions with Local Search</h1>
        <p>Tugas Besar 1 IF3070</p>
      </div>
      {/* Algorithm */}
      <ResizablePanelGroup direction='horizontal' className='flex items-start justify-between w-full gap-x-8'>
        {/* Choose Algoritma */}
        <ResizablePanel defaultSize={25} className='text-white flex flex-col items-start'>
          <h3 className='text-2xl font-bold'>Choose The Algorithm 🚀</h3>
          <div className='py-4 flex items-center gap-x-4 gap-y-4 flex-wrap z-20'>
            <div className='space-y-2'>
              <p>Hill Climbing</p>
              <div className='flex gap-x-4 gap-y-2 flex-wrap'>
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
        <ResizableHandle className='z-20 w-[1px] bg-white h-[550px]' withHandle />
        {/* Magic Cube Display */}
        <ResizablePanel defaultSize={75} className='border-2 border-white/10 rounded-lg p-0 margin-0 h-[550px]'>
          <MagicCube />
        </ResizablePanel>
      </ResizablePanelGroup>
    </main>
  );
}

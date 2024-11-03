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
import { useToast } from '@/hooks/use-toast';
import { cn } from '@/lib/utils';

export default function Home() {
  const { toast } = useToast()
  const [algorithm, setAlgorithm] = useState("")
  const [cubeResult, setCubeResult] = useState();
  const [loading, setLoading] = useState(false);
  const [isAlgorithmLoading, setIsAlgorithmLoading] = useState(false)
  const [direction, setDirection] = useState<'horizontal' | 'vertical'>('horizontal');
  const [executionTime, setExecutionTime] = useState(0.00)
  // Hill-Climbing with Sideways Move
  const [maxSidewayMoves, setMaxSidewayMoves] = useState(0)
  // Random Start Hill-Climbing
  const [maxRestart, setMaxRestart] = useState(0)
  // Genetic Algorithm
  const [populasi, setPopulasi] = useState(0)
  const [iterasi, setIterasi] = useState(0)

  const generateCube = async () => {
    setLoading(true)
    setAlgorithm("")
    try {
      const n = 125;
      const response = await fetch(`/api/generate-cube?n=${n}&straight=false`)
      const data = await response.json()
      setCubeResult(data)  
      toast({
        title: "Cube Generated!",
        description: "Successfully generated 125 random numbers"
      })
    } catch (error) {
      console.error("Failed to fetch:", error)
      toast({
        title: "Failed to Generate Cube"
      })
    } finally {
      setLoading(false)
    }
  }

  const generateCubeByAlgorithm = async (algorithm: string) => {
    setIsAlgorithmLoading(true)
    toast({
      title: "Searching...",
      description: `Search for Diagonal Magic Cube Solutions with ${algorithm}`
    })
    try {
      const endpoint = algorithm.toLowerCase().replace(/\s+/g, "-")
      const response = await fetch(`/api/${endpoint}`)
      const data = await response.json()
      // Set cube result
      // Set exectuion time
      // success toast 
    } catch (error) {
      console.error("Failed to fetch:", error)
      toast({
        title: "Failed to Generate Cube"
      })
    } finally {
      setIsAlgorithmLoading(false)
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
        <ResizablePanel defaultSize={40} className='text-white flex flex-col items-start h-[550px] overflow-y-scroll'>
          <h3 className='text-2xl font-bold'>Choose The Algorithm 🚀</h3>
          {/* Choose Algoritma */}
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
                <Button 
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Steepest Ascent-Hill-Climbing" && "bg-white/50"
                  )} 
                  onClick={() => {
                    setAlgorithm("Steepest Ascent-Hill-Climbing")
                    generateCubeByAlgorithm("Steepest Ascent-Hill-Climbing")
                  }}
                >
                  Steepest Ascent Hill-Climbing
                </Button>
                <Button 
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Stochastic Hill-Climbing" && "bg-white/50"
                  )} 
                  onClick={() => {
                    setAlgorithm("Stochastic Hill-Climbing")
                    generateCubeByAlgorithm("Stochastic Hill-Climbing")
                  }}
                >
                  Stochastic Hill-Climbing
                </Button>
                <Button  
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Hill-Climbing With Sideways Move" && "bg-white/50"
                  )} 
                  onClick={() => { 
                    setAlgorithm("Hill-Climbing With Sideways Move")  
                    // generateCubeByAlgorithm("Hill-Climbing With Sideways Move") 
                  }}
                >
                  Hill-Climbing With Sideways Move
                </Button>
                <Button 
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Random Start Hill-Climbing" && "bg-white/50"
                  )} 
                  onClick={() => { 
                    setAlgorithm("Random Start Hill-Climbing")
                    // generateCubeByAlgorithm("Random Restart Hill-Climbing") 
                  }}
                >
                  Random Restart Hill-Climbing
                </Button>
              </div>
            </div>
            <div className='space-y-2'>
              <p>Other Algorithm</p>
              <div className='flex gap-x-4 gap-y-2 flex-wrap'>
                <Button 
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Simulated-Annealing" && "bg-white/50"
                  )} 
                  onClick={() => { 
                    setAlgorithm("Simulated-Annealing")
                    generateCubeByAlgorithm("Simulated-Annealing")
                  }}
                >
                  Simulated Annealing
                </Button>
                <Button 
                  disabled={!cubeResult || isAlgorithmLoading} 
                  variant={"outline"} 
                  className={cn(
                    'bg-white/10 text-white',
                    algorithm === "Genetic Algorithm" && "bg-white/50"
                  )} 
                  onClick={() => { 
                    setAlgorithm("Genetic Algorithm")
                    // generateCubeByAlgorithm("Genetic-Algorithm")
                  }}
                >
                  Genetic Algorithm
                </Button>
              </div>
            </div>
            {
              algorithm && (
                <div>
                  { algorithm === "Hill-Climbing With Sideways Move" && (
                    <div>
                    
                    </div>
                  )}
                  { algorithm === "Random Start Hill-Climbing" && (
                    <div>
                    
                    </div>
                  )}
                  { algorithm === "Genetic Algorithm" && (
                    <div>
                    
                    </div>
                  )}
                </div>
              )
            }
          </div>
          {/* Result Box */}
          <div className='w-full border-t-2 border-white/25 mt-4 py-4 flex flex-col items-start'>
            <p>Time Execition : {executionTime}</p>
            <p>Objective Function Value : </p>
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

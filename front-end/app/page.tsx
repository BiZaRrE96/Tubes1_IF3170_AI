'use client'

import React, { useEffect, useState } from 'react';
import MagicCube from './components/MagicCube';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
import Title from './components/Title';
import { useToast } from '@/hooks/use-toast';
import { cn } from '@/lib/utils';
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { geneticAlgorithm, geneticAlgorithmType, maxRestarts, maxRestartType, maxSidewaysMove, maxSidewaysMoveType } from '@/lib/schemas';
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { ChartPlot } from './components/ChartPlot';
import { Card, CardContent, CardHeader } from '@/components/ui/card';

export default function Home() {
  const { toast } = useToast()
  const [algorithm, setAlgorithm] = useState<string>("")
  const [cubeResult, setCubeResult] = useState();
  const [submitted, setSubmitted] = useState<boolean>(false);
  const [initialCubeState, setInitialCubeState] = useState();
  const [loading, setLoading] = useState(false);
  const [cubeState, setCubeState] = useState<"Initial" | "Final">("Initial");
  const [isAlgorithmLoading, setIsAlgorithmLoading] = useState<boolean>(false)
  const [direction, setDirection] = useState<'horizontal' | 'vertical'>('horizontal');
  const [executionTime, setExecutionTime] = useState<number>(0.00)
  // Hill-Climbing with Sideways Move
  const [maxSidewaysMoves, setMaxSidewaysMoves] = useState<number>(0)
  // Random Start Hill-Climbing
  const [maxRestart, setMaxRestart] = useState<number>(0)
  // Genetic Algorithm
  const [populasi, setPopulasi] = useState<number>(0)
  const [iterasi, setIterasi] = useState<number>(0)
  const [logs, setLogs] = useState<string>("")
  const [seconds, setSeconds] = useState<number>(0);
  const [finalObjValue, setFinalObjValue] = useState<number>(0)
  const [graph, setGraph] = useState()
  const [simulatedAnnealingGraph, setSimulatedAnnealingGraph] = useState()

  const convertToChartData = (data: any) => {
    // @ts-ignore
    return data.graph.map((fitness_value, index) => ({
      browser: `Browser ${index + 1}`,
      fitness_value: fitness_value,
      fill: "white",
    }));
  };

  const sidewaysForm = useForm<maxSidewaysMoveType>({
    resolver: zodResolver(maxSidewaysMove),
  })

  const randomRestartForm = useForm<maxRestartType>({
    resolver: zodResolver(maxRestarts),
  })

  const geneticForm = useForm<geneticAlgorithmType>({
    resolver: zodResolver(geneticAlgorithm),
  })

  const generateCube = async () => {
    setLoading(true)
    setAlgorithm("")
    setSeconds(0)

    try {
      const n = 125;
      const response = await fetch(`http://localhost:8000/generate-cube?n=${n}&straight=false`)
      const data = await response.json()
      setCubeResult(data)  
      setInitialCubeState(data)
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
    setInitialCubeState(cubeResult)
    toast({
      title: "Searching...",
      description: `Search for Diagonal Magic Cube Solutions with ${algorithm}`
    })

    try {
      const endpoint = algorithm.toLowerCase().replace(/\s+/g, "-")

      let bodyToSend = JSON.stringify({ cube: cubeResult })
      if (endpoint === "hill-climbing-with-sideways-move") {
        bodyToSend = JSON.stringify({
          cube: cubeResult,
          max_iteration: 3,
          max_sidewaysmove: maxSidewaysMoves
        });
      }
      if (endpoint === "random-start-hill-climbing") {
        bodyToSend = JSON.stringify({
          cube: cubeResult,
          max_iteration: 3,
          max_restarts: maxRestart
        });
      }
      if (endpoint === "genetic-algorithm") {
        bodyToSend = JSON.stringify({
          populasi: populasi,
          iterasi: iterasi,
        });
      }
      
      const response = await fetch(`http://localhost:8000/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: bodyToSend
      })

      const data = await response.json()
      console.log(data)

      if (data) {
        setInitialCubeState(data.first.cube)
        setCubeResult(data.end.cube)
        setFinalObjValue(data.end.value)
        setLogs(data.log)
        setExecutionTime(data.time)
        const newGraph = convertToChartData(data)
        setGraph(newGraph)        
      }
      
      toast({
        title: "Successfully generated cube",
      })
    } catch (error) {
      console.error("Failed to fetch:", error)
      toast({
        title: "Failed to Generate Cube"
      })
    } finally {
      setAlgorithm("")
      setIsAlgorithmLoading(false)
      setSubmitted(true)
      setSeconds(0)
      setMaxSidewaysMoves(0)
      setMaxRestart(0)
      setPopulasi(0)
      setIterasi(0)
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

  useEffect(() => {
    let timer: any;
    if (isAlgorithmLoading) {
      timer = setInterval(() => {
        setSeconds(prevSeconds => prevSeconds + 1);
      }, 1000);
    } else {
      setSeconds(0); 
    }

    return () => clearInterval(timer);
  }, [isAlgorithmLoading]);

  return (
    <main className="w-full wrapper space-y-4 flex flex-col items-center transition-all">
      {/* Title */}
      <Title />

      {/* Algorithm */}
      <ResizablePanelGroup direction={direction} className='flex flex-row items-start justify-between w-full gap-x-8'>
        <ResizablePanel defaultSize={46} className='text-white flex flex-col items-start h-[575px] overflow-y-scroll'>
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
                  }}
                >
                  Genetic Algorithm
                </Button>
              </div>
            </div>
            {
              algorithm && (
                <div className='text-white'>
                  { algorithm === "Hill-Climbing With Sideways Move" && (
                    <Form {...sidewaysForm}>
                      <form>
                        <FormField 
                          control={sidewaysForm.control}
                          name="maxSidewaysMove"
                          render={({ field }) => (
                            <FormItem>
                              <FormLabel>Max Sideways Move</FormLabel>
                              <FormControl>
                                <Input 
                                  {...field} 
                                  className='bg-white/10' 
                                  onChange={(event) => { 
                                    setMaxSidewaysMoves(Number(event.target.value)); 
                                    field.onChange(event); 
                                  }}
                                />
                              </FormControl>
                            </FormItem>
                          )}
                        />
                      </form>
                    </Form>
                  )}
                  { algorithm === "Random Start Hill-Climbing" && (
                    <Form {...randomRestartForm}>
                      <form>
                        <FormField 
                          control={randomRestartForm.control}
                          name="maxRestart"
                          render={({ field }) => (
                            <FormItem>
                              <FormLabel>Max Restart</FormLabel>
                              <FormControl>
                                <Input 
                                  {...field}
                                  type='number'
                                  className='bg-white/10' 
                                  onChange={(event) => { 
                                    setMaxRestart(Number(event.target.value)); 
                                    field.onChange(event); 
                                  }}
                                />
                              </FormControl>
                            </FormItem>
                          )}
                        />
                      </form>
                    </Form>
                  )}
                  { algorithm === "Genetic Algorithm" && (
                    <Form {...geneticForm}>
                     <form className='w-full flex justify-between gap-x-4'>
                       <FormField 
                         control={geneticForm.control}
                         name="populasi"
                         render={({ field }) => (
                           <FormItem>
                             <FormLabel>Polulation</FormLabel>
                             <FormControl>
                              <Input 
                                {...field}
                                type='number'
                                className='bg-white/10' 
                                onChange={(event) => { 
                                  setPopulasi(Number(event.target.value)); 
                                  field.onChange(event); 
                                }}
                              />
                             </FormControl>
                           </FormItem>
                         )}
                       />
                       <FormField 
                         control={geneticForm.control}
                         name="iterasi"
                         render={({ field }) => (
                           <FormItem>
                             <FormLabel>Iteration</FormLabel>
                             <FormControl>
                             <Input 
                                {...field}
                                type='number'
                                className='bg-white/10' 
                                onChange={(event) => { 
                                  setIterasi(Number(event.target.value)); 
                                  field.onChange(event); 
                                }}
                              />
                             </FormControl>
                           </FormItem>
                         )}
                       />
                     </form>
                   </Form>
                  )}
                </div>
              )
            }
          </div>
          {/* Submit */}
          {algorithm && (
            <Button 
              disabled={isAlgorithmLoading} 
              className='mt-2 w-full z-20 max-w-[200px] flex gap-x-2' 
              variant={"secondary"}
              onClick={() => {generateCubeByAlgorithm(algorithm)}}
            >
              {
                !isAlgorithmLoading && (
                  <span>Search</span>
                )
              }
              { 
                isAlgorithmLoading && (
                  <span>Searching {seconds}s</span>
                )
              } 
            </Button>
          )}

          {/* Result Box */}
          <div className='w-full border-t-2 border-white/25 mt-4 py-4 flex flex-col items-start'>
            <p>Time Execition : {executionTime}</p>
            <p>Final Objective Function Value : {finalObjValue} </p>
          </div>
        </ResizablePanel>
        <ResizableHandle className='z-20 w-[1px] bg-white h-[575px] hidden md:block' withHandle />
        
        {/* Magic Cube Display */}
        <ResizablePanel defaultSize={54} className='hidden md:block border-2 relative border-white/10 rounded-lg p-0 margin-0 h-[575px]'>
        {
          submitted && (
            <div className='w-full flex items-center justify-center gap-x-4 absolute top-4 right-4 z-20'>
              <Button 
                variant={"outline"}
                className={cn(
                  'bg-white/10 text-white',
                  cubeState === "Initial" && "bg-white/50"
                )}
                size={"sm"}
                onClick={() => setCubeState("Initial")}
              >
                Initial State
              </Button>
              <Button 
                variant={"outline"}
                className={cn(
                  'bg-white/10 text-white',
                  cubeState === "Final" && "bg-white/50"
                )}
                size={"sm"}
                onClick={() => setCubeState("Final")}
              >
                Final State
              </Button>
            </div>
          )
        }
        {
          cubeState === "Initial" && (
            <MagicCube numbers={initialCubeState} />
          )
        }
        {
          cubeState === "Final" && (
            <MagicCube numbers={cubeResult} />
          )
        }
        </ResizablePanel>
      </ResizablePanelGroup>

      {/* Display Chart */}
      <div className='py-4' />
      <div className='w-full flex justify-between gap-x-4 mb-12 border-2 border-white/10 rounded-xl'>
        <ChartPlot graph={graph} />
        <Card className='text-white w-full bg-transparent border-none'>
          <CardHeader className='font-bold'>
            Logs
          </CardHeader>
          <CardContent className='text-white/80 font-light'>
            {logs}
          </CardContent>
        </Card>
      </div>
    </main>
  );
}

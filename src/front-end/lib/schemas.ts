import { z } from 'zod'

export const maxSidewaysMove = z.object({
  maxSidewaysMove: z.number().int().min(0).max(100)
})
export type maxSidewaysMoveType = z.infer<typeof maxSidewaysMove>

export const maxRestarts = z.object({
  maxRestart: z.number().int().min(0).max(100)
})
export type maxRestartType = z.infer<typeof maxRestarts>

export const geneticAlgorithm = z.object({
  populasi: z.number().int().min(0).max(100),
  iterasi: z.number().int().min(0).max(100)
})
export type geneticAlgorithmType = z.infer<typeof geneticAlgorithm>

export enum AlgorithmEnum {
  "Steepest Ascent-Hill-Climbing",
  "Stochastic Hill-Climbing",
  "Hill-Climbing With Sideways Move",
  "Random Start Hill-Climbing",
  "Simulated-Annealing",
  "Genetic Algorithm"
}
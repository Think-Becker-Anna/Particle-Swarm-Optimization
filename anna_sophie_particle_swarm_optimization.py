# -*- coding: utf-8 -*-
"""Anna Sophie Particle Swarm Optimization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cqtx1G_xQ0ZgP3dFQsnWCVEMpVql0BeL
"""

import random
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import imageio

def fitness_function(x, y):
  z=(x-2*y+3)**2+(2*x+y-8)**2
  return z

def update_velocity(particle, velocity, particle_best, global_best):
  max=1
  inertia_min=0.5
  c=0.1
  c1=c
  c2=c
  num_of_particles = len(particle)
  new_velocity = np.array([0.0 for i in range(num_of_particles)])
  random_1= random.uniform(0,max)
  random_2 = random.uniform(0,max)
  inertia_random = random.uniform(inertia_min,max)
  for i in range(num_of_particles):
    a = inertia_random*new_velocity[i]
    b = c1*random_1*(particle_best[i]-particle[i])
    d = c2*random_2*(global_best[i]-particle[i])
    new_velocity[i] = a+b+d
  return new_velocity

def update_position(particle, velocity):
  new_particle = particle + velocity
  return new_particle

def Particle_Swarm_Optimization(population, dimension, position_min, position_max, generation, fitness_criteria):
  particles = [[random.uniform(position_min, position_max) for j in range(dimension)] for i in range(population)]
  particle_best_position = particles
  particle_best_fitness_1 = [5] * len(particles)
  particle_best_fitness_2 = [fitness_function(p[0], p[1]) for p in particles]
  overall_best_fitness = np.argmin(particle_best_fitness_2)
  global_best_position = particle_best_position[overall_best_fitness]
  velocity = [[0.0 for j in range(dimension)] for i in range(population)]
  for t in range(generation):
    #print(f"{np.average(particle_best_fitness_2)-np.average(particle_best_fitness_1)}")
    #print(f"{np.abs(np.average(particle_best_fitness_1)-np.average(particle_best_fitness_2))<= fitness_criteria}")
    if np.abs(np.average(particle_best_fitness_1)-np.average(particle_best_fitness_2))<= fitness_criteria:
      break
    else:
      for n in range(population):
        velocity[n] = update_velocity(particles[n], velocity[n], particle_best_position[n], global_best_position)
        particles[n] = update_position(particles[n], velocity[n])
    particle_best_fitness_1 = particle_best_fitness_2
    print(f"{np.average(particle_best_fitness_1)}")
    particle_best_fitness_2 = [fitness_function(p[0], p[1]) for p in particles]
    print(f"{np.average(particle_best_fitness_2)}")
    overall_best_fitness = np.argmin(particle_best_fitness_2)
    global_best_position = particle_best_position[overall_best_fitness]
    print('Global Best Position: ', global_best_position)
    print('Best Fitness Value: ', min(particle_best_fitness_2))
    print('Average Particle Best Fitness Value: ', np.average(particle_best_fitness_2))
    print('Number of Generation: ', t+1)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    x = np.linspace(position_min, position_max, 200)
    y = np.linspace(position_min, position_max, 200)
    X, Y = np.meshgrid(x, y)
    Z= fitness_function(X,Y)
    ax.plot_wireframe(X, Y, Z, color='r', linewidth=0.2)

    # Animation image placeholder
    images = []

    # Add plot for each generation (within the generation for-loop)
    image = ax.scatter3D([
                          particles[n][0] for n in range(population)],
                         [particles[n][1] for n in range(population)],
                         [fitness_function(particles[n][0],particles[n][1]) for n in range(population)], c='b')
    images.append([image])

def main():
  population = 100
  dimension = 2
  position_min = -50
  position_max = 50
  generation = 400
  fitness_criteria = 10e-8
  Particle_Swarm_Optimization(population, dimension, position_min, position_max, generation, fitness_criteria)

if __name__=="__main__":
    main()
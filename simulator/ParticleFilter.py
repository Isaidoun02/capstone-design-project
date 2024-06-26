import random
import time
from Robot import *
from typing import *
from conf import *
from helper import *

class ParticleFilter:
    def __init__(self, num_particles: int, robot: Robot, obstacles: List[Tuple[float, float]]) -> None:
        self.num_particles = num_particles
        self.robot = robot
        self.obstacles = obstacles # act as reference points for the robot to estimate its position

        self.particles = self.create_particles()

    # particles are essentially just simulated robots
    def create_particles(self) -> List[Robot]:
        particles = []
        for _ in range(self.num_particles):
            particle = Robot(
                x = random.randint(0, WIDTH),
                y = random.randint(0, HEIGHT),
                theta = random.uniform(-math.pi, math.pi), # doesn't this get normalized in radians anyway, so why not use radians?
                color = PARTICLE_COLOR,
                # each particle follows the same error distribution as the robot
                noise_linear = random.uniform(*PARTICLE_NOISE_LINEAR_RANGE),
                noise_angular = random.uniform(*PARTICLE_NOISE_ANGULAR_RANGE),
                noise_measurement = random.uniform(*PARTICLE_NOISE_MEASUREMENT_RANGE)
            )
            particles.append(particle)
        return particles

    def apply_movement(self) -> None:
        # randomly get the linear and angular motion data to move both the robot and particles
        dist = random.uniform(*MOVEMENT_DISTANCE_RANGE)
        rot = random.uniform(*MOVEMENT_ROTATION_RANGE)

        # move the robot
        self.robot.move(dist, rot)

        # move each particle
        for particle in self.particles:
            particle.move(dist, rot)

    def update_particle_weights(self) -> None:
        robot_distances = self.robot.observe(self.obstacles)

        # for each particle, check how good of an estimation it is compared to the robot's reported distance and heading
        for particle in self.particles:
            likelihood = 1 # using 1 as a percentages, how good of an estimation is this specific particle?
            particle_distances = particle.observe(self.obstacles)

            # scale likelihood using a normal distribution with the actual robot's measurements as a reference point
            for robot_dist, particle_dist in zip(robot_distances, particle_distances): # compare all distances
                likelihood *= normal_distribution(robot_dist, DISTANCE_SIGMA, particle_dist)
            likelihood *= normal_distribution(self.robot.theta, HEADING_SIGMA, particle.theta) # compare heading angles

            particle.weight = likelihood

    # create new generation of particles based on the weights of the previous generation
    def regenerate_particles(self) -> None:
        total_weight = sum(particle.weight for particle in self.particles) or 1
        normalized_weights = [particle.weight / total_weight for particle in self.particles] # store the normalized weight for each particle

        new_particles = [ self.select_particle(normalized_weights) for _ in range(len(self.particles)) ]

        # update the particles to the newly sampled ones and add (deadreckoning?) noise
        for i, new_particle in enumerate(new_particles):
            if new_particle is None: # TODO: idk what's going on here, if NUM_PARTICLES is like 100 it's fine but if it's like 10 it's wonky??
                continue
            # TODO: understand noise better, it breaks if you don't add the noise here and idk why
            self.particles[i].x = new_particle.x + new_particle.noise_linear
            self.particles[i].y = new_particle.y + new_particle.noise_linear
            self.particles[i].theta = normalize_angle_radians(new_particle.theta + new_particle.noise_angular)
            self.particles[i].color = new_particle.color
            self.particles[i].weight = new_particle.weight

            # generate new noise for the next iteration
            self.particles[i].noise_linear = random.uniform(*PARTICLE_NOISE_LINEAR_RANGE)
            self.particles[i].noise_angular = random.uniform(*PARTICLE_NOISE_ANGULAR_RANGE)
            self.particles[i].noise_measurement = random.uniform(*PARTICLE_NOISE_MEASUREMENT_RANGE)

    # we want to do random selection with bias towards higher weighted particles
    def select_particle(self, weights) -> Robot:
        threshold = random.uniform(0, 1) # since weights are normalized, total weight is 1
        running_sum = 0
        
        # search for the particle in which the threshold falls into its range
        for i, weight in enumerate(weights):
            running_sum += weight
            if running_sum > threshold:
                return self.particles[i]

    # main function in PF. 1)Sampling; 2)Weighting; 3)Resampling
    def run_particle_filter(self) -> None:
        while True:
            self.apply_movement()
            self.update_particle_weights()
            self.regenerate_particles()
            time.sleep(0.15)
        
        # debug: first frame (comment out the while loop above to see this)
        # for p in self.particles:
        #     print(p.x, p.y, p.theta, p.weight)

import math

# General configuration variables
WIDTH = 500
HEIGHT = 500
NUM_PARTICLES = 100
NUM_OBSTACLES = 10
OBSTACLE_SEED = 45

# Robot starting parameters
ROBOT_STARTING_POS_X = 250
ROBOT_STARTING_POS_Y = 250
ROBOT_STARTING_ANGLE = math.pi
ROBOT_COLOR = "red"

PARTICLE_COLOR = "pink"

# Standard Deviations
# Tune based on how much tolerance we want to give to comparing each particle to the robot distance and heading measurements
# The higher the sigma, the more tolerant we are to differences in measurements
DISTANCE_SIGMA = 15
HEADING_SIGMA = 30

# Movement distance and rotation ranges for simulation purposes - for apply_movement()
MOVEMENT_DISTANCE_RANGE = [0, 4]
MOVEMENT_ROTATION_RANGE = [-0.15, 0.15]

# Noise ranges for the robot
ROBOT_NOISE_LINEAR_RANGE = [-0.5, 0.5]
ROBOT_NOISE_ANGULAR_RANGE = [-0.03, 0.03]
ROBOT_NOISE_MEASUREMENT_RANGE = [-2, 2]

# Noise ranges for the particles
PARTICLE_NOISE_LINEAR_RANGE = [-1, 1]
PARTICLE_NOISE_ANGULAR_RANGE = [-0.15, 0.15]
PARTICLE_NOISE_MEASUREMENT_RANGE = [-1, 1]
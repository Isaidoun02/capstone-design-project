# ----- Store configuration variables -----

ROBOT_STARTING_POS_X = 250
ROBOT_STARTING_POS_Y = 250
ROBOT_STARTING_HEADING = 0

# Particle Filter Configuration
NUM_OBSTACLES = 5
OBSTACLE_SEED = 45
NUM_PARTICLES = 100
WIDTH = 500
HEIGHT = 500

MOVEMENT_NOISE = [-1, 1]
HEADING_NOISE = [-1, 1]
MEASUREMENT_NOISE = [-1, 1]

# apply_movement() range
MOVEMENT_DIST = [0, 4]
HEADING_ROTATION = [-15, 15]

HEADING_RANGE = [-180, 180] # degrees to be constrained to

# Expected mean error of the movement, heading and measurement
# Standard deviation is per sqrt(distance) or sqrt(rotation) since we want to scale variance by distance or rotation
# MOVEMENT_ERR_MEAN = 0
# MOVEMENT_ERR_STDDEV = 1
# HEADING_ERR_MEAN = 0
# HEADING_ERR_STDDEV = 1
# MEASUREMENT_ERR_MEAN = 0
# MEASUREMENT_ERR_STDDEV = 1

# Standard Deviations
# Tune based on how much tolerance we want to give to comparing each particle to the robot distance and heading measurements
# The higher the sigma, the more tolerant we are to differences in measurements
DISTANCE_SIGMA = 30
HEADING_SIGMA = 15


# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (240, 240, 240)
import numpy as np

class DifferentialRobot:
    """
    Class to simulate a Differential Robot kinematic's based
    """

    def __init__(self, init_x, init_y, orientation, sample_time, R, L):
        """
        :param init_x: Initial x position
        :param init_y: Initial y position
        :param orientation: Initial orientation
        :param sample_time: Time between each simulation step
        :param R: Wheel diameter
        :param L: Distance between the wheels
        """
        self.x = init_x # [m]
        self.y = init_y # [m]
        self.orientation = orientation # [rad]
        self.sample_time = sample_time # [s]
        self.wheel_diameter = R # [m]
        self.axis_distance = L # [m]
    
        # wheels speed in rad/s
        self.w_right = 0
        self.w_left = 0

    def state(self, transpose=False, np=False):
        """
        Return the current state's robot in a matrix like:
        state =  |  x  |
                 |  y  |
                 | ori |
                 |  v  |
        if transpose is True, return:
        state = | x  y  ori  v |
        :param transpose: Flag to transpose the output state
        :return np.array:
        """
        if np:
            state = np.array([[self.x], [self.y], [self.orientation], [self.linear_speed]])
            if transpose:
                state = state.T
            return state
        else: 
            return self.x, self.y, self.orientation, self.linear_speed

    def step(self, w_left, w_right):
        """
        Receive left and right wheels speed [rad/s] and update robot's state
        :param w_left: left wheel speed [rad/s]
        :param w_right: right wheel speed [rad/s]
        """
        self.w_left = w_left
        self.w_right = w_right

        # first update orientation
        self.orientation += (self.wheel_diameter / self.axis_distance) * \
                            (self.w_right - self.w_left) * self.sample_time

        # update x position
        self.x += (self.wheel_diameter  / 2) * np.cos(self.orientation) * \
                  (self.w_right + self.w_left) * self.sample_time

        # update y postion
        self.y += (self.wheel_diameter  / 2) * np.sin(self.orientation) * \
                  (self.w_right + self.w_left) * self.sample_time

        return None

    @property
    def inputs(self):
        return (self.w_left, self.w_right)

    @property
    def linear_speed(self):
        """
        Return robot's linear speed in m/s
        """
        return (self.wheel_diameter / 2) * (self.w_right + self.w_left)
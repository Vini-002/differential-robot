import numpy as np

class DifferentialRobot:
    """
    Class to simulate a Differential Robot kinematic's based
    """

    def __init__(self, init_x, init_y, orientation, sample_time, R, L, w_max, a_max):
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
        self.wheel_max_speed = w_max # [rad/s]
        self.wheel_max_acc = a_max # [rad/s²]
    
        # wheels speed in rad/s
        self.w_right = 0
        self.w_left = 0

        # Wheels acceleration in rad/s²
        self.a_right = 0
        self.a_left = 0

    def state(self, transpose=False, np=False):
        """
        Return the current state's robot in a matrix like:
        state =  |  x  |
                 |  y  |
                 | ori |
                 |  v  |
                 |  w  |
        if transpose is True, return:
        state = | x  y  ori  v  w |
        :param transpose: Flag to transpose the output state
        :return np.array:
        """
        if np:
            state = np.array([[self.x], [self.y], [self.orientation], [self.linear_speed], [self.angular_velocity]])
            if transpose:
                state = state.T
            return state
        else:
            return self.x, self.y, self.orientation, self.linear_speed, self.angular_velocity

    def line_sensor(self):
        return np.clip(np.tan(self.orientation)*(0.1 + self.y /np.sin(self.orientation)), -2, 2)
        

    def step_wheel(self, des_left, des_right):
        """
        Receive left and right wheels speed [rad/s] and update robot's state
        :param w_left: left wheel speed [rad/s]
        :param w_right: right wheel speed [rad/s]
        """
        self.w_left = compute(des_left)
        self.w_right = w_right

        # first update orientation
        self.orientation += self.angular_velocity * self.sample_time

        # update x position
        self.x += self.linear_speed * np.cos(self.orientation) * \
                  self.sample_time

        # update y postion
        self.y += self.linear_speed * np.sin(self.orientation) * \
                  self.sample_time

        return None

    def step_acc(self, a_left, a_right):
        """
        Receive left and right wheels acceleration [rad/s²] and update robot's state
        :param w_left: left wheel acceleration [rad/s²]
        :param w_right: right wheel acceleration [rad/s²]
        """
        self.a_left = a_left
        self.a_right = a_right

        # updates left wheel speed
        self.w_left += self.wheel_acc(self.a_left, self.w_left) * self.sample_time

        # updates right wheel speed
        self.w_right += self.wheel_acc(self.a_right, self.w_right) * self.sample_time

        # first update orientation
        self.orientation += self.angular_velocity * self.sample_time

        # update x position
        self.x += self.linear_speed * np.cos(self.orientation) * \
                  self.sample_time

        # update y postion
        self.y += self.linear_speed * np.sin(self.orientation) * \
                  self.sample_time

        return None

    @property
    def inputs(self):
        return (self.w_left, self.w_right)

    @property
    def linear_speed(self):
        """
        Returns robot's linear speed in m/s
        """
        return (self.wheel_diameter / 2) * (self.w_right + self.w_left)
    
    @property
    def angular_velocity(self):
        """
        Returns robot's angular velocity in rad/s
        """
        return (self.wheel_diameter / self.axis_distance) * \
               (self.w_right - self.w_left)
    
    def compute(self, speed, desired):
        if (np.abs(speed - desired) <= self.wheel_max_acc):
            return desired
        else:
            return speed + self.wheel_max_acc

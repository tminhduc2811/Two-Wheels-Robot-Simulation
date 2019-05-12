import numpy as np
from matplotlib import pyplot as plt


class Robot:
    def __init__(self, x, y, w_left, w_right, r, theta, l, sample_time):
        # Init all parameters
        self.x = x
        self.y = y
        self.w_left = w_left
        self.w_right = w_right
        self.R = r
        self.theta = theta
        self.L = l
        self.sample_time = sample_time
        self.current_time = 0
        self.path_x = [x]
        self.path_y = [y]

    def update_parameters(self, w_left, w_right):
        # Calculate velocity with sample time
        v_left = self.R * w_left * self.sample_time
        v_right = self.R * w_right * self.sample_time
        w_dir = (v_right - v_left) / (2 * self.L)
        v_dir = (v_right + v_left) / 2
        self.theta = self.theta + w_dir

        # Update new position
        self.x = self.x + v_dir * np.cos(self.theta)
        self.y = self.y + v_dir * np.sin(self.theta)

        # Add new position to path
        self.path_x.append(self.x)
        self.path_y.append(self.y)

    def run(self, w_left, w_right, limit_time):
        while self.current_time < limit_time:
            self.current_time += self.sample_time
            self.update_parameters(w_left, w_right)
            plt.scatter(self.path_x, self.path_y)
            plt.pause(self.sample_time)


if __name__ == '__main__':
    # Initialize parameters
    my_robot = Robot(0, 0, 0, 0, 2, 0, 3.5, 0.1)
    my_robot.run(30, 32, 5)
    my_robot.run(42, 36, 7)
    my_robot.run(40, 40, 12)
    plt.show()

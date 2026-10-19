# Author: David Wang
# Date: 19 October 2026
# Description: A simple controller implementation as prescribed

class Controller:
    K_P = 0.15 # Proportional gain
    K_D = 0.6 # Derivative gain

    def __init__(self):
        self.prev_error = 0 # Assume e[-1] = 0

    def compute_action(self, curr_reference, curr_output):
        """
        Compute the control action based on the current reference, current
        output and previous error.
        """

        curr_error = curr_reference - curr_output

        action = (
            self.K_P * curr_error
            + self.K_D * (curr_error - self.prev_error)
        )

        self.prev_error = curr_error

        return action
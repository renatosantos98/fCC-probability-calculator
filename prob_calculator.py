import copy
import random


class Hat:
    """
    The `Hat` class takes a variable number of arguments that specify the number of balls of each color that are in the hat.
    For example, a class object could be created in any of these ways:

    ```
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    ```
    A hat must always be created with at least one ball.
    """

    def __init__(self, **balls):
        # balls is a **kwargs dictionary of the ball colours and amounts passed to the hat object.
        """The arguments passed into the hat object upon creation are converted to a `contents` instance variable.
        `contents` are a list of strings containing one item for each ball in the hat.
        Each item in the list is a color name representing a single ball of that color.
        For example, if your hat is `{"red": 2, "blue": 1}`, `contents` will be `["red", "red", "blue"]`."""
        self.contents = list()
        for color, add_amount in balls.items():
            for n in range(add_amount):
                self.contents.append(color)
        print(self.contents)

    def draw(self, draw_amount):
        """The `draw` method accepts an argument indicating the number of balls to draw from the hat.
        This method removes balls at random from `contents` and returns those balls as a list of strings.
        The balls do not go back into the hat during the draw, similar to an urn experiment without replacement.
        If the number of balls to draw exceeds the available quantity, the method returns all the balls."""
        balls_drawn = list()
        if draw_amount > len(self.contents):
            balls_drawn = self.contents
        else:
            for n in range(draw_amount):
                balls_drawn.append(
                    self.contents.pop(random.randint(0, len(self.contents) - 1))
                )
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """The `experiment` function accepts the following arguments:
    -   `hat`: A hat object containing balls that should be copied inside the function.
    -   `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
    -   `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
    -   `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

        The `experiment` function returns an approximate probability that a random draw of `num_balls_drawn` will draw the `expected_balls`. Since this is based on random draws, the probability will be slightly different each time the code is run."""
    ball_count = 0
    experiment_success = 0
    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_result = hat_copy.draw(num_balls_drawn)
        for ball in expected_balls:
            if draw_result.count(ball) >= expected_balls[ball]:
                ball_count += 1
        if ball_count == len(expected_balls):
            experiment_success += 1
        ball_count = 0
    probability = experiment_success / num_experiments
    return probability

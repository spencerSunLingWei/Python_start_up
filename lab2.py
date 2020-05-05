import math


def damped_oscillator_position(gamma, t, omega):
    """ (num, num, num) -> (num)
    This function takes in the damping coefficient (gamma), time (t) and the
    angular frenquency (omega), it produces the position of the oscillator
    at the given time.

    >>> position = damped_oscillator_position(gamma, t, omega)
    >>> position
    -0.7798529395484154
    """
    position = math.e**(-gamma*t)*math.cos(((omega)**2-(gamma)**2)**(1/2)*(t))
    return position





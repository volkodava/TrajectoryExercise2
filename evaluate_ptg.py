#!/usr/bin/env python

from cost_functions import *
from helpers import Vehicle, show_trajectory
from ptg import PTG

# TODO - tweak weights to existing cost functions
WEIGHTED_COST_FUNCTIONS = [
    (time_diff_cost, 1),
    (s_diff_cost, 1),
    (d_diff_cost, 1),
    (efficiency_cost, 1),
    (max_jerk_cost, 1),
    (total_jerk_cost, 1),
    (collision_cost, 1),
    (buffer_cost, 1),
    (max_accel_cost, 1),
    (total_accel_cost, 1),
]


def main():
    vehicle = Vehicle([0, 10, 0, 0, 0, 0])
    predictions = {0: vehicle}
    target = 0
    delta = [0, 0, 0, 0, 0, 0]
    start_s = [10, 10, 0]
    start_d = [4, 0, 0]
    T = 5.0
    best = PTG(start_s, start_d, target, delta, T, predictions, WEIGHTED_COST_FUNCTIONS)
    show_trajectory(best[0], best[1], best[2], vehicle)


if __name__ == "__main__":
    main()

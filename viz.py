#!/usr/bin/env python3

# Copyright (C) 2019  Matthias Paulmier

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from random import shuffle
import argparse
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from sorting_algs.algs import get_algs


def main(size, method):
    ''' Main function '''
    table = [x+1 for x in range(size)]
    color_map = plt.get_cmap('inferno')
    color = color_map(np.linspace(1, 0, size))
    y_pos = np.arange(1, size+1)
    shuffle(table)
    algs = get_algs()
    alg = algs[method][0](table)

    fig, axes = plt.subplots()
    rects = axes.bar(y_pos, table, color=[color[i-1] for i in table],
                     align='center')

    axes.set_title('Visualisation of the %s algorithm' %
                   algs[method][1])
    # Allows to see the entirety of the last element
    axes.set_xlim(0, size+1)
    axes.set_ylim(0, size)

    def animate(data):
        for rect, datum in zip(rects, data):
            rect.set_height(datum)
            rect.set_color(color[datum-1])

    _ = FuncAnimation(fig, func=animate, frames=alg,
                      interval=1, repeat=False)

    plt.show()


def positive_integer(string):
    ''' Helper function for checking if a string represents a positive
    integer
    '''
    value = int(string)
    if value < 0:
        msg = '%r is not a positive integer' % string
        raise argparse.ArgumentTypeError(msg)
    return value


def parse_args():
    ''' Parse command line arguments '''
    parser = argparse.ArgumentParser(
        description='Sorting Algorithms Visualization'
    )
    parser.add_argument('--size', type=positive_integer, default=100,
                        help='a positive integer, defaults to 100')
    parser.add_argument('--method', type=str, default='b',
                        choices=get_algs().keys(),
                        help='a character for the algorithm to visualize, \
                              defaults to b for running bubble sort')
    return parser.parse_args()


if __name__ == '__main__':
    ARGS = parse_args()
    N = ARGS.size
    METHOD = ARGS.method
    main(N, METHOD)

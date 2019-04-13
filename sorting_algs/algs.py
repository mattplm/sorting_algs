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

''' Module containing generators for common sorting algorithms '''


def _swap(table, i, j):
    ''' Function for swaping 2 elements in an array

    Parameters
    ==========
    table -- a list of elements
    i -- the first element to swap
    j -- the second element to swap
    '''
    if i != j:
        table[i], table[j] = table[j], table[i]


def bubble_sort(table):
    ''' Execute the bubble sort algorithm '''
    if len(table) == 1:
        return

    swapped = True
    t_len = len(table)
    while swapped:
        t_len -= 1
        swapped = False
        for i in range(t_len):
            if table[i] > table[i+1]:
                _swap(table, i, i+1)
                swapped = True
            yield table


def insertion_sort(table):
    ''' Execute the insertion sort algorithm '''
    for i in range(len(table)):
        for j in range(i, 0, -1):
            yield table
            if table[j-1] > table[j]:
                _swap(table, j, j-1)
            else:
                break


def selection_sort(table):
    ''' Execute the selection sort algorithm '''
    raise NotImplementedError()


def merge_sort(table, start=0, end=None):
    ''' Execute the merge sort algorithm '''
    raise NotImplementedError()


def merge(table, start, mid, end):
    ''' Helper function for merge_sort '''
    raise NotImplementedError()


def quick_sort(table, start=0, end=None):
    ''' Execute the quick sort algorithm '''
    raise NotImplementedError()


def heap_sort(table):
    ''' Execute the heap sort algotihm '''
    raise NotImplementedError()


def shell_sort(table):
    ''' Execute the shell sort algorithm '''
    raise NotImplementedError()


def comb_sort(table):
    ''' Execute the comb sort algorithm '''
    raise NotImplementedError()


ALGS = {
    'b': (bubble_sort, 'Bubblesort'),
    'i': (insertion_sort, 'Insertionsort'),
    's': (selection_sort, 'Selectionsort'),
    'm': (merge_sort, 'Mergesort'),
    'h': (heap_sort, 'Heapsort'),
    'q': (quick_sort, 'Quicksort'),
    'e': (shell_sort, 'Shellsort'),
    'c': (comb_sort, 'Combsort')
}


def get_algs():
    ''' Return the'''
    return ALGS

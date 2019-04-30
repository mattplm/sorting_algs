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
    for i in range(len(table)-1):
        min_idx = i
        for j in range(i+1, len(table)):
            if table[j] < table[min_idx]:
                min_idx = j
                yield table
        _swap(table, min_idx, i)
        yield table


def merge_sort(table, start=0, end=None):
    ''' Execute the merge sort algorithm '''
    if end is None:
        end = len(table) - 1
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(table, start=start, end=mid)
    yield from merge_sort(table, start=mid + 1, end=end)
    yield from merge(table, start, mid, end)
    yield table


def merge(table, start, mid, end):
    ''' Helper function for merge_sort '''
    i_start = start
    i_mid = mid + 1
    merged = []
    while i_start <= mid and i_mid <= end:
        if table[i_start] < table[i_mid]:
            merged.append(table[i_start])
            i_start += 1
        else:
            merged.append(table[i_mid])
            i_mid += 1
    # Append the rest of the array from left to right
    merged.extend(table[i_start:mid+1])
    merged.extend(table[i_mid:end+1])
    for i, val in enumerate(merged):
        table[start + i] = val
        yield table


def quick_sort(table, start=0, end=None):
    ''' Execute the quick sort algorithm '''
    if end is None:
        end = len(table) - 1
    if start >= end:
        return

    pivot = table[end]
    pivot_i = start

    for i in range(start, end):
        if table[i] < pivot:
            _swap(table, i, pivot_i)
            pivot_i += 1
        yield table
    _swap(table, end, pivot_i)
    yield table
    yield from quick_sort(table, start, pivot_i - 1)
    yield from quick_sort(table, pivot_i + 1, end)


def heap_sort(table):
    ''' Execute the heap sort algotihm '''
    raise NotImplementedError()


def shell_sort(table):
    ''' Execute the shell sort algorithm '''
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(table):
            tmp = table[i]
            j = i
            while j >= gap and table[j-gap] > tmp:
                table[j] = table[j - gap]
                yield table
                j -= gap
            table[j] = tmp
            yield table
            i += 1


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

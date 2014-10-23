#!/usr/bin/env python

import glob
import sys
import math
import copy

'''
    Insertion Sort.
    
    Parameters
    ----------
    data: list
        List of values to be sorted.
        
    Returns
    -------
    sorted list
'''
def insertion_sort(data):
    # traverse the entire array
    for i in range(1, len(data)):
        key = data[i]
        j = i
        
        # traverse the sorted portion of the array looking for elements that are smaller than or equal to the key
        while(j > 0 and key <= data[j-1]):
            # move element j - 1 to the right to make room for the key
            data[j] = data[j - 1]
            j -= 1
            
        # insert key in the appropriate place
        data[j] = key
        
    return data
    
'''
    Quick Sort.

    Parameters
    ----------
    data: list
        List of values to be sorted.
        
    Returns
    -------
    sorted list
'''
def quick_sort(data):    
    # recursive case: array size greater than 1
    if(len(data) > 1):
        # calculate the pivot by partitioning
        pivot = partition(data)
        
        # omit the pivot and recursively call quick_sort()
        left = quick_sort(data[:pivot])
        right = quick_sort(data[pivot+1:])
        
        # combine the left and right partitions along with the pivot
        left.append(data[pivot])
        left.extend(right)
        
        return left
    # base case: return array of size 1
    else:
        return data

'''
    This is the partition step of Quick Sort.

    Parameters
    ----------
    data: list
        List of values for which we want to determine the pivot value.
        
    Returns
    -------
    int
'''
def partition(data):
    # set the pivot to be the element at the start index
    pivot = data[0]
    h = 0
    
    # start k at 1 and switch values that are less than the pivot
    for k in range(1, len(data)):
        if(data[k] < pivot):
            h += 1
            swap(data, h, k)

    # put the pivot in its new position
    swap(data, 0, h)
    
    # return the new position of the pivot
    return h

'''
    This is the swap step of Quick Sort.
    
    Parameters
    ----------
    data: list
        The list we're sorting.
    i: int
        The index of the first value.
    j: int
        The index of the second value.
'''
def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    
'''
    Merge Sort.
    
    Parameters
    ----------
    data: list
        List of values to be sorted.
        
    Returns
    ----------
    sorted list
'''
def merge_sort(data):
    # store the size of the array passed into merge_sort for later use (reduces operation count)
    data_len = len(data)
    
    # recursive case: array size greater than 1
    if(data_len > 1):
        start = 0
        
        # find the midpoint
        middle = int(math.floor(data_len / 2))
        
        # split the array into two halves and recursively call merge_sort()
        left = merge_sort(data[:middle])
        right = merge_sort(data[middle:])
        
        # finally, merge the sorted lists and return the result
        return merge(left, right)
    # base case: return an array of one element
    else:
        return data

'''
    This is the merge step of Merge Sort.
    
    Parameters
    ----------
    left: list
        The left half of the list, minus the pivot.
    right: list
        The right half of the list, minus the pivot.
    
    Returns
    ----------
    list
'''
def merge(left, right):
    # temporary array to hold the sorted result
    result = []
    
    # while loop that cycles through the left and right halves fully and sorts one by one
    while(len(left) > 0 or len(right) > 0):
        # if there are elements left in both the left and right halves, find out which element is greater and append the lesser element
        if(len(left) > 0 and len(right) > 0):
            if(left[0] <= right[0]):
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        # if there is an element left in only the left half, copy it to the result and delete that element from the left subarray
        elif(len(left) > 0):
            result.append(left[0])
            left = left[1:]
        # if there is an element left in only the right half, copy it to the result and delete that element from the right subarray
        elif(len(right) > 0):
            result.append(right[0])
            right = right[1:]
    # return the merged array
    return result

'''
    Driver function that gets all the files in the input/ directory, runs each of the three sorting algorithms, and prints the output.
'''
def main():
    # need to increase the system's recursion limit for Quick Sort
    sys.setrecursionlimit(10000)
    
    # generate list of input files
    file_list = glob.glob('./input/*')
    
    # need three copies of the data for the three different sorting algorithms
    insertion_raw_data = []
    quick_raw_data = []
    merge_raw_data = []
    
    for file in file_list:
        # open file for reading
        data = open(file, 'r')
        
        # store each element in the temp list
        temp = []
        for element in data:
            temp.append(int(element))
            
        # deep copy to ensure we don't have references
        insertion_raw_data.append(copy.deepcopy(temp))
        quick_raw_data.append(copy.deepcopy(temp))
        merge_raw_data.append(copy.deepcopy(temp))
        
    print '##############################'
    print '#       Insertion Sort       #'
    print '##############################\n'
    for data in insertion_raw_data:
        print 'Input size: {}'.format(len(data))
        print insertion_sort(data)
        print ''
        
    print '##############################'
    print '#         Quick Sort         #'
    print '##############################\n'
    for data in quick_raw_data:
        print 'Input size: {}'.format(len(data))
        print quick_sort(data)
        print ''
        
    print '##############################'
    print '#         Merge Sort         #'
    print '##############################\n'
    for data in merge_raw_data:
        print 'Input size: {}'.format(len(data))
        print merge_sort(data)
        print ''
    
if __name__ == '__main__':
    main()
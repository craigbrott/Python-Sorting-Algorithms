import glob
import sys
import math
import copy

#need to increase the system's recursion limit for Quick Sort
sys.setrecursionlimit(10000)

## read in data files

#generate list of files
fileList = glob.glob("./input/*")

#need three copies of the data for the three different sorting algorithms
fileDataInsertion = []
fileDataQuick = []
fileDataMerge = []

for file in fileList:
    #open file for reading
    data = open(file, "r")
    
    #store the data in temp as an array
    temp = []
    for element in data:
        temp.append(int(element))
    
    #append the temp array to fileData (deep copy to ensure we don't have references)
    fileDataInsertion.append(copy.deepcopy(temp))
    fileDataQuick.append(copy.deepcopy(temp))
    fileDataMerge.append(copy.deepcopy(temp))

## define sorting algorithms

## Insertion Sort

#Insertion Sort
def insertionSort(data):
    #get the global counters ready
    global comparisonsI
    global operationsI
    
    #traverse the entire array
    for i in range(1, len(data)):
        operationsI += 1
        
        #store the key to be used in the following while loop
        key = data[i]
        operationsI += 1
        
        #counter j is initialized to the value of i
        j = i
        operationsI += 1
        
        #traverse the sorted portion of the array looking for elements that are smaller than or equal to the key
        comparisonsI += 1

        #need a this comparison flag to check if the while loop triggered
        comparisonFlag = False
        while(j > 0 and key <= data[j-1]):
            comparisonFlag = True
            comparisonsI += 1
            operationsI += 2
            
            #move element j-1 to the right to make room for the key
            data[j] = data[j - 1]
            operationsI += 2
            
            j -= 1
            operationsI += 1
            
        if comparisonFlag:
            comparisonsI -= 1
            
        #insert key in the appropriate place
        data[j] = key
        operationsI += 1
    return data
    
## Quick Sort
    
#Quick Sort
def quickSort(data):
    #get the global counters ready
    global comparisonsQ
    global operationsQ
    
    #recursive case: array size greater than 1
    operationsQ += 2
    if(len(data) > 1):
        #calculate the pivot by partitioning
        pivot = partition(data)
        operationsQ += 1
        
        #omit the pivot and recursively call quickSort()
        left = quickSort(data[:pivot])
        right = quickSort(data[pivot+1:])
        operationsQ += 5
        
        #combine the left and right partitions along with the pivot
        left.append(data[pivot])
        left.extend(right)
        operationsQ += 2
        
        return left
    #base case: return array of size 1
    else:
        return data

#Partition
def partition(data):
    #get the global counters ready
    global comparisonsQ
    global operationsQ
    
    #set the pivot to be the element at the start index
    pivot = data[0]
    h = 0
    operationsQ += 2
    
    #start k at 1 and switch values that are less than the pivot
    for k in range(1, len(data)):
        comparisonsQ += 1
        operationsQ += 1
        if(data[k] < pivot):
            h += 1
            operationsQ += 1
            
            swap(data, h, k)
    #put the pivot in its new position
    swap(data, 0, h)
    
    #return the new position of the pivot
    return h

#Swap
def swap(data, i, j):
    #get the global counters ready
    global comparisonsQ
    global operationsQ
    
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    operationsQ += 3
    
## Merge Sort

#Merge Sort
def mergeSort(data):
    #get the global counters ready
    global comparisonsM
    global operationsM
    
    #store the size of the array passed into mergeSort for later use (reduces operation count)
    dataLen = len(data)
    operationsM += 1
    
    #recursive case: array size greater than 1
    operationsM += 1
    if(dataLen > 1):
        start = 0
        operationsM += 1
        
        #find the midpoint
        middle = int(math.floor(dataLen / 2))
        operationsM += 3
        
        #split the array into two halves and recursively call mergeSort()
        left = mergeSort(data[:middle])
        right = mergeSort(data[middle:])
        operationsM += 2
        
        #finally, merge the sorted lists and return the result
        return merge(left, right)
    #base case: return an array of one element
    else:
        return data

#Merge
def merge(left, right):
    #get the global counters ready
    global comparisonsM
    global operationsM
    
    #temporary array to hold the sorted result
    result = []
    operationsM += 1
    
    #while loop that cycles through the left and right halves fully and sorts one by one
    while(len(left) > 0 or len(right) > 0):
        operationsM += 2
        #if there are elements left in both the left and right halves, find out which element is greater and append the lesser element
        operationsM += 2
        if(len(left) > 0 and len(right) > 0):
            comparisonsM += 1
            if(left[0] <= right[0]):
                operationsM += 1

                result.append(left[0])
                left = left[1:]
                operationsM += 2
            else:
                result.append(right[0])
                right = right[1:]
                operationsM += 2
        #if there is an element left in only the left half, copy it to the result and delete that element from the left subarray
        elif(len(left) > 0):
            operationsM += 1

            result.append(left[0])
            left = left[1:]
            operationsM += 2
        #if there is an element left in only the right half, copy it to the result and delete that element from the right subarray
        elif(len(right) > 0):
            operationsM += 1
            
            result.append(right[0])
            right = right[1:]
            operationsM += 2
    #return the merged array
    return result
    
## call sorting algorithms for each array

print "##############################"
print "#       Insertion Sort       #"
print "##############################\n"
for data in fileDataInsertion:
    #set up counter variables for insertion sort
    comparisonsI = 0
    operationsI = 0
    print insertionSort(data)
    print "input size: ", len(data)
    print "total comparisons: ", comparisonsI
    print "total operations: ", operationsI
    print "\n"

print "##############################"
print "#         Quick Sort         #"
print "##############################\n"
for data in fileDataQuick:
    #set up counter variables for quick sort
    comparisonsQ = 0
    operationsQ = 0
    print quickSort(data)
    print "input size: ", len(data)
    print "total comparisons: ", comparisonsQ
    print "total operations: ", operationsQ
    print "\n"

print "##############################"
print "#         Merge Sort         #"
print "##############################\n"
for data in fileDataMerge:
    #set up counter variables for merge sort
    comparisonsM = 0
    operationsM = 0
    print mergeSort(data)
    print "input size: ", len(data)
    print "total comparisons: ", comparisonsM
    print "total operations: ", operationsM
    print "\n"
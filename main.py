#Damir Zababuryn
import random
import time
import statistics

operationsBinary = 0
operationsLinear = 0
operationsBinaryIterative = 0

#Binary Search Recursive function
#operations = every math calculation
def binary_search(nums, key, lower, upper):
    global operationsBinary

    #first it checks whether it's the first time we going through the loop
    #if true add +1 to operations, if false nothing

    operationsBinary += 1
    if lower > upper:
        return -1

    #ads +1 to opeartions because it calculates the index value
    index = (lower + upper) // 2
    operationsBinary += 1

    #for each comparison add plus 1, if it passes to the next stage add extra one
    #because the number of operations increased
    if nums[index] == key:
        operationsBinary += 1
        return index
    elif lower == upper:
        operationsBinary += 2
        return -1
    elif nums[index] < key:
        operationsBinary += 3
        return binary_search(nums, key, index + 1, upper)
    else:
        operationsBinary += 3
        return binary_search(nums, key, lower, index - 1)

#Linear Search
def LinearSearch (numbers, key):
    global operationsLinear
    operationsLinear = 0
    for i in range(len(numbers)):
        operationsLinear += 1
        if (numbers[i] == key):
            operationsLinear += 1
            return i + 1
    return -1

#Binary Search Iterative
def BinarySearchIterative(numList,key):
    global operationsBinaryIterative
    #3 math operations here
    low = 0
    high = len(numList) - 1
    mid = 0
    operationsBinaryIterative += 3

    while low <= high:
        mid = (high + low) // 2
        operationsBinaryIterative += 2

        if numList[mid] < key:
            low = mid + 1
            operationsBinaryIterative += 2
        elif numList[mid] > key:
            high = mid - 1
            operationsBinaryIterative += 3
        else:
            operationsBinaryIterative += 3
            return mid + 1
    return -1


if __name__ == '__main__':
    #creates global vars to count operations
    totalOperationsBinary = 0
    totalOperationsBinaryIterative = 0
    totalOperationsLinear = 0
    operationsLinearList = []
    operationsBinaryList = []
    operationsBinaryIterativeList = []

    numList = []
    # filling the list with random numbers
    random.seed(10)
    for i in range(1000):
        number = random.randint(0, 10000)
        numList.append(number)

    # sorting list in an ascending order
    numList.sort()
    print(numList)
    print("------------------------------------------------------")
    print()

    #reset seed to random again, and creates a list of random keys
    random.seed()
    keysList = []
    for i in range (0, 100):
        random.seed(i)
        keysList.append(random.randint(0,10000))
    print("List of keys for this specific iteration")
    print(keysList)
    print("------------------------------------------------------")
    print()

    # loop for Binary Recursive
    start_time = time.process_time()
    for i in range(0,100):
        binary_search(numList, keysList[i], 0, len(numList) - 1)
        operationsBinaryList.append(operationsBinary)
        totalOperationsBinary += operationsBinary
        operationsBinary = 0
    print("Time taken for binary Recursive methods:", (time.process_time() - start_time) * 1000, "seconds * 1000")
    print("List of number of operations for each binary recursive search")
    print(operationsBinaryList)
    strTotalOperationsBinary = str(totalOperationsBinary)
    print()
    print("Total number of operations for binary recursive search: " + strTotalOperationsBinary)
    print("Average number of operations in Binary Recursive method: " + str(totalOperationsBinary / 100))
    print("Standard deviation of Binary Recursive method: " + str(statistics.stdev(operationsBinaryList)))
    print("------------------------------------------------------")
    print()


    #loop for binary iterative
    start_time = time.process_time()
    for i in range (0,100):
        BinarySearchIterative(numList, keysList[i])
        operationsBinaryIterativeList.append(operationsBinaryIterative)
        totalOperationsBinaryIterative += operationsBinaryIterative
        operationsBinaryIterative = 0
    print("Time taken for binary Iterative methods:", (time.process_time() - start_time) * 1000, "seconds * 1000")
    print("List of number of operations for each binary iterative search")
    print(operationsBinaryIterativeList)
    print()
    strTotalOperationsBinaryIterative = str(totalOperationsBinaryIterative)
    print("Total number of operations for binary recursive search: " + strTotalOperationsBinaryIterative)
    print("Average number of operations in Binary Recursive method: " + str(totalOperationsBinaryIterative / 100))
    print("Standard deviation of Binary Recursive method: " + str(statistics.stdev(operationsBinaryIterativeList)))
    print("------------------------------------------------------")
    print()

    #loop for linear search
    start_time = time.process_time()
    for i in range(0, 100):
        LinearSearch(numList, keysList[i])
        operationsLinearList.append(operationsLinear)
        totalOperationsLinear += operationsLinear
        operationsLinear = 0
    print("Time takenfor Linear methods:", (time.process_time() - start_time) * 1000, "seconds * 1000")
    print("List of number of operations for each linear search")
    print(operationsLinearList)
    strTotalOperationsLinear = str(totalOperationsLinear)
    print("Total number of operations for linear search: " + strTotalOperationsLinear)
    print("Average number of operations in Linear method: " + str(totalOperationsLinear / 100))
    print("Standard deviation of Linear method: " + str(statistics.stdev(operationsLinearList)))
    print("------------------------------------------------------")
    print()




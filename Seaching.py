def LinearSearch(arr,k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return-1

def BinarySearch(arr,i):
    leftIndex = 0
    rightIndex = len(arr) - 1
    midIndex = 0

    while leftIndex<=rightIndex:
        midIndex = (leftIndex + rightIndex)//2
        midNo = arr[midIndex]
        if midNo == k:
            return midIndex
        if midNo<k:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex - 1
    return -1
        
def BinarySearchRecursive(arr,k,leftIndex,rightIndex):
    if rightIndex < leftIndex:
        return-1
    midIndex = (leftIndex + rightIndex)//2
    if midIndex >= len(arr) or midIndex<0:
        return -1
    midNo = arr[midIndex]

    if midNo == k:
        return midIndex
    if midNo<k:
        leftIndex = midIndex + 1
    else:
        rightIndex = midIndex - 1

    return BinarySearchRecursive(arr,k,leftIndex,rightIndex)

if __name__ == '__main__':
    arr = [12,14,15,90,34]
    k = 90
    sol = BinarySearchRecursive(arr,k,0,len(arr))
    print(sol)
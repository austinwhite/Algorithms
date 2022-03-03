# Time: O(log(n)) where n is the length of array
# Space: O(log(n)) where n is the length of array

def binarySearch(array, target, start=0, end=0):
    return binarySearchHelper(array, target, 0, len(array) - 1)
	
def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target < potential_match:
        return binarySearchHelper(array, target, left, middle - 1)
    elif target > potential_match:
        return binarySearchHelper(array, target, middle + 1, right)
    else:
        return middle

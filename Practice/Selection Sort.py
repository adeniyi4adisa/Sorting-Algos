"""
We define a class called SelectionSort to encapsulate the sorting functionality.

In the class constructor (__init__ method), we accept an array arr as a parameter and initialize it as an instance variable.

The sort method performs the selection sort algorithm. It takes the arr and performs the necessary comparisons and swaps to sort the array in ascending order.

We use the length of the array (n) to determine the number of iterations needed. We traverse the array from the first element to the second-to-last element (n - 1 times).

Within the outer loop, we initialize a variable min_index with the current index i. This represents the index of the minimum element in the unsorted part of the array.

In the inner loop, we search for the minimum element by comparing each element starting from the next index (i + 1) with the current minimum element (self.arr[min_index]). If a smaller element is found, we update min_index with the index of the new minimum element.

After the inner loop completes, we have found the minimum element in the unsorted part of the array.

We then swap the found minimum element (self.arr[min_index]) with the first element of the unsorted part (self.arr[i]). This ensures that the smallest element is moved to its correct position in the sorted part of the array.

The outer loop continues, and the process is repeated for the remaining unsorted part of the array until the entire array is sorted.

After the sorting process is complete, the sorted array is stored in the arr instance variable.

Finally, we create an instance of the SelectionSort class, passing an example array ([64, 34, 25, 12, 22, 11, 90]). We call the sort method on the instance and then print the sorted array.

"""

class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)

        # Traverse through all array elements
        for i in range(n - 1):

            # Find the minimum element in the unsorted part of the array
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element of the unsorted part
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
ss = SelectionSort(arr)
ss.sort()
print("Sorted array:", ss.arr)

"""
We define a class called BubbleSort to encapsulate the sorting functionality.

In the class constructor (__init__ method), we accept an array arr as a parameter and initialize it as an instance variable.

The sort method performs the bubble sort algorithm. It takes the arr and performs the necessary comparisons and swaps to sort the array in ascending order.

We use the length of the array (n) to determine the number of iterations needed. We traverse the array n-1 times, as the largest element will already be in place after each iteration.

Within the outer loop, we have an inner loop that iterates n-i-1 times. This is because the largest i elements will be in their correct positions after each iteration.

Inside the inner loop, we compare adjacent elements. If the current element is greater than the next element, we swap them using a tuple assignment.

After the sorting process is complete, the sorted array is stored in the arr instance variable.

Finally, we create an instance of the BubbleSort class, passing an example array ([64, 34, 25, 12, 22, 11, 90]). We call the sort method on the instance, and then print the sorted array.
"""

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)

        # Traverse through all elements
        for i in range(n - 1):

            # Last i elements are already in place, so the inner loop will run i times less each iteration
            for j in range(n - i - 1):

                # Compare adjacent elements
                if self.arr[j] > self.arr[j + 1]:
                    # Swap if the current element is greater than the next element
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bs = BubbleSort(arr)
bs.sort()
print("Sorted array:", bs.arr)

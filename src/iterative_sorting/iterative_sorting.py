# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # Add a loop with that iterates over the list stopping at second to last
    # index because the last number will not need to be compared because it
    # will already have been replaced with the largest.
    for i in range(0, len(arr)-1):
        # assign the current index as the min_index to be compared against
        # with the following indexes in the inner loop
        min_index = i
        # add an additional loop to compare agaist min_index it will find the
        # smaller smallest value if one exist.
        for j in range(i+1, len(arr)):
            # the i+1 is important so that we are comparing the min_index t
            # numbers that follow after i since the indexes before have alread
            # been resolved
            if arr[j] < arr[min_index]:
                min_index = j
            # compare the current value of index j to the set min_index if its
            # smaller reassign the value to the current index j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            # check to see if the value actually changed if so swap the two
            # values.

    return arr
    # TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

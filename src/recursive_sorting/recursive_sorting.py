# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    output = []
    while len(arrA) and len(arrB):
        if arrA[0] <= arrB[0]:
            less_arrA = arrA.pop(0)
            output.append(less_arrA)
        else:
            less_arrB = arrB.pop(0)
            output.append(less_arrB)
    while len(arrA):
        less_arrA = arrA.pop(0)
        output.append(less_arrA)
    while len(arrB):
        less_arrB = arrB.pop(0)
        output.append(less_arrB)
    return output


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    left, right = arr[:middle], arr[middle:]
    sorted_left, sorted_right = merge_sort(left), merge_sort(right)
    return merge(sorted_left, sorted_right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left, right = arr[start: mid], arr[mid:end]
    f_counter, s_counter = 0, 0
    for i in range(start, end):
        if s_counter >= len(right) or (f_counter < len(left) and left[f_counter] < right[s_counter]):
            arr[i] = left[f_counter]
            f_counter = f_counter+1
        else:
            arr[i] = right[s_counter]
            s_counter = s_counter+1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if r - l > 1:
        mid = int((l+r)//2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

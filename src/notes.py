

'''bigocheatsheet.com'''
# import math
# arr = [6, 3, 4, 2, 5, 8, 0, 7, 1, 9, 12, 11, 10, 13, 14, 17, 16, 15, 18, 19]


# def selection_sort(arr):
#     ''' this method iterates through each index and compares its value
#     to all other values and assigns the smallest value to variable j
#     Selection sort is not a fast sorting algorithm because it uses nested
#     loops to sort. Should only be used with small data sets the O
#     classification would be O(n^2). Small datasets can be defined as less than
#     10000 records to sort. '''
#     for num in range(0, len(arr)-1):
#         # here we loop over each item in the array stopping at the 2nd to the last
#         # item in the list.
#         min_index = num
#         # this assigns the current iteration as the minimum till its proven not to
#         # be the smallest in the comparison when the entire array is compared against
#         # it in the second loop
#         for compare_num in range(num+1, len(arr)):
#             # in this loop we start at the index after the index above so we dont
#             # recompare the min_index to itself and we check every following index
#             # with the min_index to see if there is an even smaller value
#             if arr[compare_num] < arr[min_index]:
#                 min_index = compare_num
#                 # We compare each index after the min_index to see if there is a
#                 # smaller value when a smaller value occurs it becomes the
#                 # min_index and is compared against for the rest of the array
#                 # until a smaller value is found or the end of the loop is reached
#         if min_index != num:
#             arr[num], arr[min_index] = arr[min_index], arr[num]
#             # We check the min index to see if it is not the current num we were
#             # comparing the inner loop too and if its not we reassign the num
#             # index with whats in the min_index. We then put the num value we were
#             # comparing against and assign it to the index where the smaller numbr
#             # was found the above command does this swap simultaneously so an
#             # additional place holder is not needed.
#     print(arr)
#     return arr


# selection_sort(arr)


# # Linear (sequential) search checks each item in array until it reaches the desired search parameter
# # num = input("Enter a number:")
# # for a in arr:
# #     print(f"trying {a}")
# #     if a == int(num):
# #         print(f"{a} is our number")
# #         break
# # middle = len(arr)/2
# ''' runtime complexity
# O(c) is Constant Time

# O(login) is Logarithmic Time

# O(n) is Linear Time

# O(nlogn) is Log-linear Time

# O(n^c) is quadratic time

# O(c^n) is exponential time


# '''


# # def binary_search(arr, target):
# #     low = 0
# #     high = len(arr)-1
# #     while low <= high:
# #         mid = int((low + high)/2)
# #         if target < arr[mid]:
# #             high = mid - 1
# #         elif target > arr[mid]:
# #             low = mid + 1
# #         else:
# #             return mid


# # print(binary_search(arr, 5))

# def foo(n):
#     sq_root = int(math.sqrt(n))
#     # this is only implemented once and is O(1)
#     for i in range(0, sq_root):
#         # this would require looping equal to the square root of the
#         # parameter that is passed in  O(sqrt(n))
#         print(i)

#     # the print is ran only one time per iteration and is O(1) according
#     # lecture
#     # The reason functionally its considered O(1) is when determining run
#     # the implementation occurs i the loop and line by line is understood
#     # as (O(1)) in first math operation line then the for loop will cause
#     # rest function to run the sqrt of n times and line for line in
#     # in determining the run time is O(1)*O(sqrt(n))*O(1)


# print(foo(25))
# # so to find the runtime of this operation where 25 is passed as the n
# # paramater then it would be O(1)*O(sqrt(25))*O(1) which in this case
# # runtime would equal 5

# def bar(n):
#     s = 0  # O(1)
#     for i in range(n):  # O(n)
#         for j in range(n):  # O(n)
#             s += i * j  # O(1)
#             print(s)  # O(1)
#     return(s)  # O(1)
# # there are two occurences of O(n), one on each loop so the operation
# # occur n times in for i then for j would complete a loop for each
# # occurence of i.For example If n = 5 then i would iterate 5 times
# # and for each iteration Thus O(n^2)
# print(bar(25))
# # run time is 575
# def baz(n):
#     s = 0  # O(1)
#     for i in range(n):  # O(n)
#         for j in range(int(math.sqrt(n))):  # O(sqrt(n))2 or O(n*.5)
#             s += i * j  # O(1)
#     return s
# # this will result  in O(n^1)+O(n^.5) = O(n^1.5)
# print(baz(10))
#
# input = [1, 2, 3]


# def crossAdd(input):
#     answers = []
#     for i in range(0, len(input)):
#         going_up = input[i]
#         going_down = input[len(input)-1-i]
#         answers.append(going_up + going_down)
#     return answers
# # in the cross add function we go over a loop just once so it can be determined by O(n)
# print(crossAdd(input))


# arr = [4, 8, 3, 8, 9, 4, 6, 1, 2]


# def find(needle, hatstack):
#     for i in range(0, len(hatstack)):
#         if int(hatstack[i]) == int(needle):
#             return True


# print(find(2, arr))

# in worst case scenario this would be O(n) assuming it reaches the last element before finding the needle
# arr = [4, 6, 3, 7, 4, 3, 2, 4, 5, 6]


# def makeTuples(arr):
#     answer = []
#     for i in range(0, len(arr)):
#         for j in range(0, len(arr)):
#             answer.append(arr[i] + arr[j])
#     return answer


# print(makeTuples(arr))

# this would be an O(n^2) because ever index  of outer loop of arr is compared agaist every index of an innerloop of arr


# def basicRecursion(max, current):
#     if current > max:
#         return
#     print(current)
#     basicRecursion(max, current+1)


# basicRecursion(5, 1)

#  an example of simple recursion and would not be used in real world projects

# arr = [55, 3, 666, 34, 778, 323]


# def fibonacci(n):
#     n = float(n)
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# for i in range(1, 20):
#     print(fibonacci(i))


# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n-1)


# print(factorial(10))
# arr = [23, 56, 74, 22, 75, 32, 3, 67, 63]


# def merge_sort(nums):
#     if len(nums) < 2:
#         return nums
#     middle = len(nums)//2
#     left, right = nums[:middle], nums[middle:]
#     sorted_left, sorted_right = merge_sort(left), merge_sort(right)
#     return merge(sorted_left, sorted_right)


# def merge(left, right):
#     output = []
#     while len(left) and len(right):
#         if left[0] <= right[0]:
#             less_left = left.pop(0)
#             output.append(less_left)
#         else:
#             less_right = right.pop(0)
#             output.append(less_right)
#     while len(left):
#         less_left = left.pop(0)
#         output.append(less_left)
#     while len(right):
#         less_right = right.pop(0)
#         output.append(less_right)
#     return output


# print(merge_sort(arr))
arr1 = [1, 5, 8, 9]
arr2 = [2, 3, 7, 10]

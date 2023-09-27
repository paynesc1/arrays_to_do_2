# Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
# array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
# def reverse(arr):
#     left = 0
#     right = len(arr)-1
#     while left < right:
#         temp = arr[left]
#         arr[left] = arr[right]
#         arr[right] = temp
#         left += 1
#         right -= 1
#     return arr
# print(reverse([1,2,3,4,5]))


# Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
# change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.

# def rotateArr(arr, shiftBy):
#     return arr[shiftBy:] + arr[:shiftBy]
# print(rotateArr([1,2,3,4,5],-1))


# Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.
# def secretCode(arr,min,max):
#     return arr[min:max]
# print(secretCode([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],3, 8))




# Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].
# def concat(arr1, arr2):
#     return arr1+arr2
# print(concat(['a','b'],[1,2]))




# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.

# def removeNegatives(arr):
#     i = len(arr)-1
#     #iterate through arr
#     while i > 0:
#         if arr[i]<0:
#             arr.pop(i)
#         i-=1
#     #pop neg vals
#     return arr
# print(removeNegatives([1,-1,2,-2,3,-3,4]))



# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.
# def removeNegatives(arr):
#     i = 0
#     while i < len(arr):
#         if arr[i]<0:
#             arr.pop(i)
#         i+=1
#     return arr
# print(removeNegatives([-1,1,-2,2,-3,3]))


# Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.
# def sec_last(arr):
#     return arr[len(arr)-2]
# print(sec_last([42,"true",4,"Kate",7]))

import math

# Return the second-largest element of an array. Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.
# def sec_largest(arr):
#     largest = 0
#     second_largest
#     for i in arr:
#         if i > largest:
#             largest = i
# print(sec_largest([42,1,4,math.pi,7]))


# Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.
# def nth_last(arr, val):
#     return arr[len(arr)- val]

# print(nth_last([5,2,3,6,4,9,7],3))





# Liam has "N" number of Green Belt stickers for excellent Python projects. Given arr and N, return the Nth-largest element, where (N-1) elements are larger. Return null if needed.
#reorder array from smallest to largest
# def nth_largest(arr, val):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1]=key
#     print(arr)
#     if val > len(arr)-1:
#         return None
#     else:
#         print(arr.reverse())
#         return arr[val]
# print(nth_largest([1,5,20,100,3,7],2))


# In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?

# You will be given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]
# def inter_sums(arr):
#     sum = 0
#     #iterate through the list
#     for i in range(10):
#     #add values into sum variable
#         sum = sum + arr[i]
#     arr.insert(10,sum)
#     #at tenth element add the sum to list
#     return arr
# print(inter_sums([1,2,1,2,1,2,1,2,1,2,1,2,1,2]))


# Create a function that changes a given array to list each original element twice, retaining original order. Convert [4,"Ulysses",42,false] to [4,4,"Ulysses","Ulysses",42,42,false,false].
# def duplicate(lst):
#     length = len(lst)
#     i=0
#     while i < length:
#         lst.insert(i+1,lst[i])
#         i+=2
#         length+=1
#     return lst
# print(duplicate([4,"Ulysses",42,'false']))

# Create a standalone function that accepts two arrays and combines their values sequentially into a new array, at alternating indices starting with first array. Extra values from either array should be included afterward. Given [1,2] and [10,20,30,40], return new array containing [1,10,2,20,30,40].
# def combine(lst1,lst2):
#     new_lst = []
#     for i in lst1:
#         new_lst.append(i)
#         for j in lst2:
#             new_lst.append(j)
#     return new_lst
# print(combine([1,2],[10,20,30,40]))

#return average value of an array of unsorted numbers:
def average(lst):
    sum=0
    #iterate through list
    for i in lst:
        sum=sum+i
    return sum/len(lst)
    #add values into sum variable
    #return sum divided by length of list
print(average([7,6,9,8,10,1,3,2,5,4]))
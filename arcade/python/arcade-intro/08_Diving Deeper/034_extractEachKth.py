
def extractEachKth(inputArray, k):
   return [x for i, x in enumerate(inputArray) if (i + 1) % k != 0]
   
print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = input("Enter a alphabet to check the existence of it in a array: ")
if linearsearch(arr,x) == -1:
    print("Element does not exit")
else:
    print("element found at index "+str(linearsearch(arr,x)))
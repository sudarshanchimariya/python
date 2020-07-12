def bubbleSort(nlist):
    for number in range(len(nlist)-1,0,-1):
        for i in range(number):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [4,56,33,47,7,46,49,25,90]
bubbleSort(nlist)
print("Bubble Sorted list:\n",nlist)
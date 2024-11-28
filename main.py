L = [4,5,1,3,7,10]
print("Oringinal list:", L)
count = 0
for i in L:
    count += 1
avg = count/len(L)
print("Sum", count)
print("average", avg)
L.sort()
print("Sorted list:", L)
print("Smallest element is", L[0])
print("Largest element is", L[-1])
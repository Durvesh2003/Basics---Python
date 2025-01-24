# 16.Write a Python program to Merge Two Sorted Lists?

L1 = [10,2,45,23,11,45]
L1.sort()
L2 = [15,13,2,34,11,54]
L2.sort()
i = 0
j = 0
merged_list = []

while i< len(L1) and j< len(L2):
    if L1[i] < L2[j]:
        merged_list.append(L1[i])
        i = i+1
    else:
        merged_list.append(L2[j])
        j =j+1
while i < len(L1):
    merged_list.append(L1[i])
    i += 1
while j <len(L2):
    merged_list.append(L2[j])
    j += 1
print ("Merged list is : ", merged_list)



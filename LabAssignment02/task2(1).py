def merge(a, b):
    merged = []
    lindx = 0
    rindx = 0

    while lindx < len(a) and rindx < len(b):
        if a[lindx] <= b[rindx]:
            merged.append(a[lindx])
            lindx += 1
        else:
            merged.append(b[rindx])
            rindx += 1
    while lindx < len(a):
        merged.append(a[lindx])
        lindx += 1
    while rindx < len(b):
        merged.append(b[rindx])
        rindx += 1
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = merge_sort(arr[:mid])
        a2 = merge_sort(arr[mid:])

        merged = merge(a1, a2)
    return merged 

with open("input2(1).txt", "r") as input1:
  with open("output2(1).txt", "w+") as output1:
    N = int(input1.readline())
    strlist1 = input1.readline()
    list1 = [int(i) for i in strlist1.split(" ")]
    M = int(input1.readline())
    strlist2 = input1.readline()
    list2 = [int(i) for i in strlist2.split(" ")]
    list1.extend(list2)
    result = merge_sort(list1)
    output1.writelines(f"{result}")
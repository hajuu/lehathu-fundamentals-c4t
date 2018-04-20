def selection_sort(list):
    list_len=len(list)
    for i in range(list_len):
        min=i
        for j in range(i+1,list_len):
            if list[min]>list[j]:
                min=j
        if min!=i:
            list[i],list[min]=list[min],list[i]
    return list

print(selection_sort([4,8,1,3,2,9,5,7,6]))

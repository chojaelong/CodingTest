def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in array:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

def bubble_sort(array):
    length = len(array)
    
    for _ in range(length - 1):
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

def insert_sort(array):   
    for i in range(1, len(array)):
        num = array[i]
        j = i
        
        while j > 0 and array[j - 1] > num:
            array[j] = array[j - 1]
            j -= 1
        array[j] = num
    
    return array
                

array = [5, 3, 1, 2, 4]
#print(array)
#quick = quick_sort(array)
#print(quick)
#bubble = bubble_sort(array)
#print(bubble)
insert = insert_sort(array)
print(insert)
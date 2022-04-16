def merge_arrays(a1, a2, arr):
    
    i = 0
    j = 0
    k = 0

    while i<len(a1) and j<len(a2):
        
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            k+=1
            i+=1

        else:
            arr[k] = a2[j]
            k+=1
            j+=1
    
    while i<len(a1):
        arr[k] = a1[i]
        k+=1
        i+=1
    
    while j<len(a2):
        arr[k] = a2[j]
        k+=1
        j+=1

def merge_sort(arr):

    '''Merge Sort using recursion'''
    
    # O(nlog(n)) Time Complexity & O(n) Space Complexity
        
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr) // 2
    
    a1 = arr[0:mid]
    a2 = arr[mid:]

    merge_sort(a1)
    merge_sort(a2)
    merge_arrays(a1, a2, arr)


if __name__ == '__main__':
    print('Please enter list elements separated by a space. Optionally end with a -1, which wont count towards list data.')
    input = [ele for ele in input().split(' ')]
    unsorted = []
    for ele in input:
        if ele == str(-1):
            break
        elif ele.strip() == '':
            continue
        else:
            unsorted.append(int(ele))

    merge_sort(unsorted)
    print('Sorted List')
    print(unsorted)
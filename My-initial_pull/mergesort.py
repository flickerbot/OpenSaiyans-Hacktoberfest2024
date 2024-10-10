def merge_sort(A, p, r, threshold=10):
    if p >= r:
        return
    if r - p + 1 <= threshold:
        insertion_sort(A, p, r)
    else:
        q = (p + r) // 2
        merge_sort(A, p, q, threshold)
        merge_sort(A, q + 1, r, threshold)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    
    i = j = 0
    k = p
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def insertion_sort(A, p, r):
    for i in range(p + 1, r + 1):
        key = A[i]
        j = i - 1
        while j >= p and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

# Example usage
A = [12, 11, 13, 5, 6, 7]
merge_sort(A, 0, len(A) - 1)
print("Sorted array is:", A)


def union(A, B):
    result = A[:]
    for x in B:
        if x not in result:
            result.append(x)
    return result


def intersection(A, B):
    result = []
    for x in A:
        if x in B and x not in result:
            result.append(x)
    return result

def difference(A, B):
    result = []
    for x in A:
        if x not in B:
            result.append(x)
    return result



A = list(map(int, input("Enter elements of Set A separated by space: ").split()))
B = list(map(int, input("Enter elements of Set B separated by space: ").split()))

print("Set A:", A)
print("Set B:", B)

print("Union (A ∪ B):", union(A, B))
print("Intersection (A ∩ B):", intersection(A, B))
print("Difference (A - B):", difference(A, B))
print("Difference (B - A):", difference(B, A))

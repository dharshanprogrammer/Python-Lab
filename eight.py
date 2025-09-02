def find_largest():

    n=int(input("Enter A Number Of Elements"))
    arr=[]
    largest=arr[0]
    for i in range(0,n):
        N=int(input("Enter The  Element"))
        arr.append(N)

    for i in range(0,n):
        if largest >= arr[i]:
            continue
        largest=arr[i]

    print("Largest Number :",largest)

find_largest()
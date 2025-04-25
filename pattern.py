n = 5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end="")
    print()

# largest element in an array 



arr = [1,2,5,8,8,85,6,8,6565565,8,65,6654646465]
def large_num():
    largest_num = arr[0]
    for i in range(len(arr)):
        if(arr[i] > largest_num):
            largest_num=arr[i]
    return largest_num

print(large_num())
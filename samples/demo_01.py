arr = [3, 8, 7, 4, 3, 0, 21, 33, 45, 67]

for i in range(1, len(arr)):
    for j in range(0, len(arr)-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# for i in range(len(arr)-1, 0, -1):
#     for j in range(0, i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print(arr)





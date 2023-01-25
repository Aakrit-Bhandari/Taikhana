# 1
# 3 3
# 3 6 9 
# 1 4 7 
# 2 8 9
# column 2 25
def lar_sum_col(arr):
    n = len(arr)
    m = len(arr[0])
    max_sum = -1
    max_index = -1
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += arr[i][j]
        if sum>max_sum:
            max_sum = sum
            max_index = j
    return max_sum,max_index
def lar_sum_row(arr):
    n = len(arr)
    m= len(arr[0])
    max_sum =-1
    max_index=-1
    for i in range(len(arr)):
        sum = 0
        for ele in arr[i]:
            sum+=int(ele)
        if sum>max_sum:
            max_sum=sum
            max_index = i
    return max_sum,max_index

n = input().split()
a,b = int(n[0]),int(n[1])
arr = [[int(i) for i in input().split()]for j in range(a)]
lar_col_sum,lar_col_index= lar_sum_col(arr)
lar_row_sum,lar_row_index = lar_sum_row(arr)
if lar_row_sum>lar_col_sum:
    print("row ",lar_row_index,lar_row_sum)
else:
    print("column ",lar_col_index,lar_col_sum)
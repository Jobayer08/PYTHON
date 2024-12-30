def sum(n):
    if n==1:
        return 1
    return n+ sum(n-1)
print(sum(5))
def pri(j,l):
    if l==len(j):
        return 
    print(j[l])
    return pri(j,l+1)
list1=[1,2,3,4,5,6,7,8]
pri(list1,0)

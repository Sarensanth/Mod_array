def modArray(array,base):
    result=0
    for i in range(len(array)):
        result=(result*10+array[i])%base
    return result

array=list(map(int, input().split()))
base=int(input())
print(modArray(array,base))
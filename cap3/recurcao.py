def regressiva(i):
    print(i)
    if(i <= 1):
        return
    else:
        return regressiva(i-1)
    
regressiva(10)

#soma
lista = [2,1,3,4,5]
def soma(arr):
    if(not arr):
        return 0
    return arr[0] + soma(arr[1:])

print(soma(lista))

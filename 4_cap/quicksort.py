def quicksort(arr):
    if len(arr) < 2: # arrays com dois ou menos elementos ja estao ordenados
        return arr
    else: #caso recurssivo
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo] #subarray com elementos menores que pivo
        maiores = [i for i in arr[1:] if i > pivo] #subarray com elementos maiores que pivo
        return quicksort(menores) + [pivo] + quicksort(maiores)
    


print(quicksort([4,5,6,3,2,8,96,4]))
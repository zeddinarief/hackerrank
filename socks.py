def sockMerchant(n, ar):
    if n != len(ar) or n > 100:
        return "Total socks not match"
    
    ar.sort()
    pair = 0
    
    if n == 1:
        return pair
    
    for i in range(n-1):
        if ar[i] == ar[i+1]:
            ar[i], ar[i+1] = "-", "-"
            pair += 1
            
    return pair


arr = [2, 4, 2, 4, 4, 5, 8, 5, 6]
n = len(arr)

result = sockMerchant(n, arr)

print(result)
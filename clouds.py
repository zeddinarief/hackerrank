# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    arr = c
    jump = 0
    state = True
    pos = 0
    while(state):
        # check if not finish yet
        if pos < len(arr) - 2:
            # check if the current position + 2 = 0    
            if arr[pos+2] == 0:
                pos += 2
                jump += 1
            else:
                pos += 1
                jump += 1
        else:
            if pos == len(arr) - 2:
                pos += 1
                jump += 1
            
            state = False
        
    return jump
    
arr_cloud = [0, 1, 0, 0, 0, 1, 0]
print(jumpingOnClouds(arr_cloud))

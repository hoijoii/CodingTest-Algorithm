import time
temp = [[2, 15, 3, 23], 
[2, 28, 4, 25],
[4, 12, 6, 5],
[5, 2, 5, 31], 
[6, 3, 6, 15],
[6, 15, 9, 3], 
[6, 15, 9, 27],
[7, 14, 9, 1], 
[9, 14, 12, 24],
[10, 5, 12, 31]]*10000

garden=[]

start = time.time()
garden.append(sorted(temp, key=lambda x:[x[2], x[3]])[-1])
  
end = time.time()

print(end-start, ' sec')
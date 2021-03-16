import time
start_time = time.time()




dictionary = {}
f_x = [11, 41, 47, 61]
n = int(input())
i = 0
for element in range(n):
    key = int(input())
    if key in dictionary:
        print(dictionary[key])
    else:
        dictionary[key] = f(key)
        print(dictionary[key])







print("time elapsed: {:.2f}s".format(time.time() - start_time))
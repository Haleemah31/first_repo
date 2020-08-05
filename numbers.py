# for i in range (10):
#     print (i*10)


# for i in range (10):
#     print (i)

# for i in range (100, 2100, 100):
#     print (i)


# for i in range (20,520, 20)
#     print (i, i/2, i/2/2, i/2/2/5),20):

# for i in range (8):
#     print (i, abs(i-8))

# IMPORT TIME
# import time
# for i in range (60):
#     time.sleep (1)
#     print ( abs (i-60))

import time

minute = 3
seconds = minute * 60

for i in reversed(range(seconds)):
    print(int(i/60), i%60, sep= ":")
    time.sleep(1)

    for i in reversed(range(minute)):
        for j in reversed(range(60)):
            print(i,j, sep = ":")
        time.sleep(1)
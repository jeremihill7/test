import time

s = 0
m = 0
h = 0

while True:
    print(h, ":", m, ":", s)
    time.sleep(0.001)
    if s == 59:
        s = 0
        if m == 59:
            m = 0
            if h == 23:
                h = 0
            else:
                h += 1    
        else:
            m +=1    
    else:
        s += 1

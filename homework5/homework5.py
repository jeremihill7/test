def my_range(start=1, finish=1, step=1):    
    result = []
    while start == finish:
        result.append(start)
    if start <=finish:
        start += step
        result.append(start)
    else:
        start -= step
        result.append(start)    
    return result

print(my_range(10, 2, 1))      


#for i in range(0, 10 + 1, 1):
    #print(i)
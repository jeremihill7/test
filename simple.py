def my_range(finish, start=1, step=1):  
    if step < 0:
        return "Error: step < 0"
    else:
        result = [start]
        while start != finish:
            if start < finish:
                start += step
            else: 
                start -= step
            
            result.append(start)
        
        return result

print(my_range(2, 5))

def my_range(finish, start=None, step=1):
   result = []
   if finish:
      if finish > 0:  # if finish > 0 and finish == 1:
         result = [1]
         while len(result) != finish or finish != 1:
            result.append(result[-1] + step)
      
         return result
   else:
      return result

print(my_range(4))      



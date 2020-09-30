def binary_search(list,low,high,val):
     if high<low:
          return None
     else:
          midval=low-((high-low)//2)

          if list[midval]>val:
               return binary_search(list,low,midval-1,val)
          elif list[midval]<val:
               return binary_search(list,midval-1,high,val)
          else:
               return midval
list=[5,3,2,1,4,7]
print(binary_search(list,0,5,1))


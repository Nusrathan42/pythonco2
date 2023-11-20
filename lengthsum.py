list1=[1,2,3,4,5,6]
list2=[0,9,8,7,6,2]
if len(list1)==len(list2):
   print(f"a.the lists have the same length")
else:
    print(f"a.the lists have different length")
      
print(f"b.sum of list1:{sum(list1)} & sum of list2:  {sum(list2)}")
if sum(list1)==sum(list2):
    print("the lists sum to the same value.")
else:
    print("the lists donot sum to the same value.")
common_values=set(list1) & set(list2)
if common_values:
                  print(f"c.common values in both lists:{common_values}")
else:
    print("c.there are no common values in both lists.")
    

#a=['c','d','e','f']
#for i in range (len(a)):
 #   print("i like",a[i])
#for i in range(2022,2050+1,4):
 #   print(i)
y1=int(input("enter starting year:"))
y2=int(input("enter ending year:"))
if y1>y2:
    print("end year must be greater than or equal to start year")
else:
    print(f"leap years from {y1} to {y2}")
    for year in range(y1,y2+1):
      if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print(year)

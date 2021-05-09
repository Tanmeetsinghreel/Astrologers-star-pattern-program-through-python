#take a integer type variable as input which will defines the lenght of the traingle
#now declare another boolean variable. when the value of boolean is 1(true) the star pattern
#will print or if the value of the boolean is 0(false) then it print reverse pattern

# if True(1) then print
"""

*
**
***
****

# if False(0) then print

****
***
**
*

"""
a = int(input("enter how many lines you want to print\n"))
b = bool(int(input("enter any number for star pattern or press 0 for reversed star pattern\n")))# bolean means either 0 or 1
#here agar input 0 hoga to false or 1 ya koi bi number hoga to true
c = 1# declare a variable
if b== True:
    while(c <= a):# (1 <= 5)
        print("*" * c)# "*" * 1,2__and so on
        c = c + 1# here c value increase by 1
else:
    while(c <= a):# (1 <= 5)
     print("*" * a)# "*" * 5,4__and so on
     a = a - 1# here a value decrease by 1

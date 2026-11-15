# print ("Hello World") 
# print ("Hello World") 
# print ("Hello World") 
# print ("Hello World") 
# print ("Hello World") 
# print ("Hello World") 

#---------------------------------------------------------------------

# print (True or False)
# print (True and False)
# print (not True or False) #ถ้าแล้ว
# print ((not True or False) and (not False or True)) #ดังนั้น

#---------------------------------------------------------------------

# p = 1212
# h = 4545

# print(p*h) 

#---------------------------------------------------------------------

# print("Hello", input("your name:"))

#---------------------------------------------------------------------

# print("A - Hello, World!")

# print("Hello, Leagues of Code!")

#---------------------------------------------------------------------

# print(type("Hi"))

# print(5 == 5) #เปรียบเทียบผลลัพธ์=False


#---------------------------------------------------------------------
# เขียนโค้ดตาม PEP8

#---------------------------------------------------------------------

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# print (a + b + c)


# apple = int(input("apple:"))
# students = int(input("students:"))
# print (apple // students)



# n = int(input())
# print( n + 1)


# apple = int(input())
# students = int(input())
# print (apple // students)

# a = int(input())
# b = int(input())
# print (b*(a*3))

# a = int(input())
# b = int(input())

# print(a * 3 ** b)

# a = int(input())
# print(a // 60)
# print (a % 60)

#---------------------------------------------------------------------

# conditions

# mem = input("Are you a member? (Y/N)")
# if mem == "Y":
#     v = input("Is your membership VIP?: (Y/N)")
#     if v == "Y":
#             price = int(input("Enter price: "))
#             if price >= 5000:
#                  print("20percent discount, ", "new price:", (price * 8/10) )
#             else:
#                   print("15percent discount, ", "new price:", (price * 8.5/10) )
#     else:
#         price = int(input("Enter price: "))
#         if price >= 3000:
#             print("10percent discount, ", "new price:", (price * 9/10) )
#         else:
#              print("5percent discount, ", "new price:", (price * 9.5/10) )

# else:
#      price = int(input("Enter price: "))
#      print("No discount, your total price is", price)

# print("Thank you!")

#---------------------------------------------------------------------

time = int(input("Time: (min) "))

if time <= 120:
    print("FREE")
elif time >= 121 and time <= 180:
    if (time%60) != 0:
        time = time+60
        print("20Bath per hour", "total price = ", (time//5060)*20, "baht")
    else:
        print("20Bath per hour", "total price = ", (time//5060)*20, "baht")
elif time >= 181 and time <= 300:
    if (time%60) != 0:
        time = time+60
        print("50Bath per hour", "total price = ", (time//60)*50, "baht")
    else:
        print("50Bath per hour", "total price = ", (time//60)*50, "baht")
else:
    if (time//1440) >= 1 and (time%1440) != 0:
        time = time+1440
        print(time)
    else:
        print(".")
print("THANK YOU !!")



#------------------------------------------- 3d = 3000, 
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
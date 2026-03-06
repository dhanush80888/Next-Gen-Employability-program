# for i in range(1,15):
#     print(i)

#even
# i=1
# while(i<=10):
#     if(i%2==0):
#         print(i)
#     i+=1
    
#odd    
# i=1
# while(i<=10):
#     if(i%2==1):
#         print(i)
#     i+=1

# name="hello"
# for i in name:
#     print(i)
    
# name=['dhanush','tarun','abdul','basavaraj']
# for n in name:
#     print(n)

# name={'dhanush':18,'tarun':89,'abdul':56,'basavaraj':34}
# for n in name:
#     print(name[n])

# print(name.keys())

# for i in range(1,15):
#     if(i==11):
#         break
#     print(i,end="   ")


# def sqr(n):
#     return n**2
# def cube(n):
    
    
    
#     return n**3
    
# print(f'{sqr(5)} , {cube(5)}')


#Exception Handling 

a="Dhanush"
# try:
#     print(a[10])
# except:
#     print("Index error")
    
# print(a[1])

try:
    print(a.append("kumar"))
except (IndexError, AttributeError):
    print("I am Exeption handling")
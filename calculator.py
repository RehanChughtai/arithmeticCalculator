    #First  number/
#second number\
#operator/

num1=int(input("Enter first number:"))
print(num1)
print("------------------")
num2=int(input("Enter second number:"))
print(num2)
print("------------------")
op=input("Enter operator[+ - * / %]:")
print(op)
print("------------------")
print(num1,op,num2)
resulr=0
if op =='+':
   result=num1+num2
elif op =='-':
   result=num1-num2
elif op =='*':
   result=num1*num2
elif op =='/':
   result=num1/num2
elif op =='%':
   result=num1%num2
else:
   print("Invalid operator!!")
print("-------------RESULT-------------")
print(num1,op,num2,'=',result)
print(result)
print("------------end-------------")

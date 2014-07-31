a=input("Enter a value:")
b=input( "Enter another value:")

def div(a,b):
    try:
       return a/b
    except ZeroDivisionError as exp:
       return 0
s=div(a,b)
print s

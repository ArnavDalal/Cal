n = input(("Enter a number: "))
m = input(("Enter your second number: "))
o = input(('''Please write the operation you want to perform: (!Please write the operation in lower case only|)
OPERATIONS:
add
subtract
multiply
divide
___________________________________________________
'''))
#Operations
if o == "divide":
    print(n+" divided by", m+" is", int(n)/int(m))
    input(("Please press ENTER to close this program/App."))
    
if o == "multiply":
    
    print(n+" multiplied by", m+" is", int(n)*int(m))
    input(("Please press ENTER to close this program/App."))
    
if o == "subtract":
    
    print(n+" subtracted from", m+" is", int(n)-int(m))
    input(("Please press ENTER to close this program/App."))

if o == "add":
    print(n+" added to", m+" is", int(n)+int(m))
    input(("Please press ENTER to close this program/App."))
    
operazione = str(input("Enter an operation [*,+,-,/] : "))
operazioni = ["+","-","/","*"]
userinput = int(input("First number: "))
userinput1 = int(input("Second number: "))

if operazione == operazioni[0]:
 print(userinput + userinput1)
 input("Press a botton for exit:")
 exit()
 
elif operazione == operazioni[1]:
 print(userinput-userinput1)
 input("Press a botton for exit:")
 exit()
 
elif operazione == operazioni[2]:
 print(userinput/userinput1)
 input("Press a botton for exit:")
 exit()
 
elif operazione == operazioni[3]:
 print(userinput*userinput1)
 input("Press a botton for exit:")
 exit()
 
else:
 print("Error")
 input("Press a botton for exit:")
 exit()

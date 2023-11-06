number= int(input ("How many terms the user wants to print? "))  
  
# First two terms  
num1 = 0  
num2 = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if number <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
# if there is only one term, it will return n_1  
elif number == 1:  
    print ("The Fibonacci sequence of the numbers up to", number, ": ")  
    print(num1)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < number:  
        print(num1)  
        nth = num1 + num2  
       # At last, we will update values  
        num1 = num2  
        num2 = nth  
        count += 1  



import math  
num = float(input("Enter a number: "))
 

if num > 0:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
else:
    sqrt_result = "Undefined (number must be >= 0)"
    log_result = "Undefined (number must be > 0)"
 
sine_result = math.sin(num)  
print("Square Root: ",sqrt_result)
print("Natural Logarithm (ln): ",log_result)
print("Sine (in radians): ",sine_result)
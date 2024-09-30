# Mathematical Operations
print(7-3)
print(3*3)
print(6/3)  # FLoating point number
print(6//3)   # Integer
print(2**3)   # Power
print(6%5)  

# Operations follow PEMDAS(left to right)
# ()
# **
# * OR /
# + OR -
print(3*3+3/3-3)
print(3*(3+3)/3-3)

# bmi
bmi = 84/1.65**2
print(bmi)
print(int(bmi)) # Flooring
print(round(bmi))   # Rounding
print(round(bmi,2)) # Rounding to the closest two digits

score=0
# User scores a point
score+=1
print(score)

# f-strings
print("Your score is" + str(score))
score=0
height=1.8
is_winning=True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
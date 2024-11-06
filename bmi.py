def calculate_bmi(height,weight):
    print("Height=",height)
    print("Weight=",weight)
    BMI = weight/(height **2)
    print("BMI=",round(BMI,2))
    print("Weightclass Classification:",end="")
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI>25:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")  
        return 0                      


result=calculate_bmi(weight=57,height=1.73)  
print("result=",result) 
result=calculate_bmi(weight=97,height=1.63)
print("result=",result) 
result=calculate_bmi(weight=37,height=1.89)
print("result=",result) 

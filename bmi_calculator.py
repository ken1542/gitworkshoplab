name1="carl"
height1_m1=5
weight_kg1=78

name2="ken"
height_m2=10
weight_kg2=56

def bmi_calculator(name,height_m,weight_kg):
    bmi=weight_kg/(height_m**2)
    print("bmi:")
    print(bmi)
    if bmi<25:
        return name + "is not overweight"
    else:
        return name + "is overweight"
    
    result1=bmi_calculator(name1,height1_m1,weight_kg1)
    result2=bmi_calculator(name2,height_m2,weight_kg2)
    
    print(result1)
    print(result2)
    

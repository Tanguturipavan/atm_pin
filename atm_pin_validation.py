'''
       ATM_PIN_VALIDATION:

'''

def atm_pin_validation():
    pincode = input("Enter ATM PIN Code: ")
    
    if len(pincode) == 4 or len(pincode) == 6:
        if pincode.isdigit():
          return "Valid PIN Code" 
        else:
            return "Invalid PIN Code"
    else:
        return "Invalid PIN Code"

result =atm_pin_validation()
print(result)

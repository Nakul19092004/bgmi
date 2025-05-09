def AND(a, b): 
    return 1 if (a + b) >= 2 else 0   
 
def OR(a, b): 
    return 1 if (a + b) >= 1 else 0   
 
def NOT(a): 
    return 1 if a == 0 else 0         
 
def XOR_gate(): 
    print("\nXOR Gate:") 
    print("Note: XOR is a non-linearly separable function and requires multiple neurons.") 
     
    for a in [0, 1]: 
        for b in [0, 1]: 
            not_a = NOT(a) 
            not_b = NOT(b) 
            a_and_not_b = AND(a, not_b) 
            not_a_and_b = AND(not_a, b) 
            xor_result = OR(a_and_not_b, not_a_and_b) 
            print(f"{a} XOR {b} = {xor_result}") 
 
XOR_gate()

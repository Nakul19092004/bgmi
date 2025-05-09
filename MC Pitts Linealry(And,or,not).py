def AND_gate(): 
    w1 = float(input("Enter weight w1 for AND gate: "))       
    w2 = float(input("Enter weight w2 for AND gate: "))       
    threshold = float(input("Enter threshold for AND gate: "))    
 
    print("\nAND Gate:") 
    print("0 AND 0 =", 1 if (w1*0 + w2*0) >= threshold else 0) 
    print("0 AND 1 =", 1 if (w1*0 + w2*1) >= threshold else 0) 
    print("1 AND 0 =", 1 if (w1*1 + w2*0) >= threshold else 0) 
    print("1 AND 1 =", 1 if (w1*1 + w2*1) >= threshold else 0) 
 
def OR_gate(): 
    w1 = float(input("Enter weight w1 for OR gate: "))    
    w2 = float(input("Enter weight w2 for OR gate: "))    
    threshold = float(input("Enter threshold for OR gate: "))
 
    print("\nOR Gate:") 
    print("0 OR 0 =", 1 if (w1*0 + w2*0) >= threshold else 0) 
    print("0 OR 1 =", 1 if (w1*0 + w2*1) >= threshold else 0) 
    print("1 OR 0 =", 1 if (w1*1 + w2*0) >= threshold else 0) 
    print("1 OR 1 =", 1 if (w1*1 + w2*1) >= threshold else 0) 
 
def NOT_gate(): 
    w = float(input("Enter weight w for NOT gate: "))     
    threshold = float(input("Enter threshold for NOT gate: ")) 
 
    print("\nNOT Gate:") 
    print("NOT 0 =", 1 if (w * 0) >= threshold else 0) 
    print("NOT 1 =", 1 if (w * 1) >= threshold else 0) 
 
AND_gate() 
OR_gate() 
NOT_gate() 

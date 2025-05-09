import numpy as np 
import matplotlib.pyplot as plt 
 
# Sigmoid activation function 
def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) 
 
# Derivative of sigmoid 
def sigmoid_derivative(x): 
    return x * (1 - x) 
 
# Initialize inputs and weights 
Xi = [ 
    np.array([1, -2, 0, -1]),  
    np.array([0, 1.5, -0.5, -1]),  
    np.array([-1, 1, 0.5, -1]) 
] 
d = np.array([-1, -1, 1]) 
w = np.array([1, -1, 0, 0.5])  # Initial weights 
alpha = 0.1  # Learning rate 
errors = []  # Store errors for visualization 
print("Initial Weights:", w) 
 
# Training loop using Delta Learning Rule with Sigmoid Activation 
for i in range(len(d)): 
    x = Xi[i]  # Select input vector 
    net_input = np.dot(w, x) 
    y = sigmoid(net_input)  # Compute output using sigmoid 
    error = d[i] - y  # Compute error 
    y_derivative = sigmoid_derivative(y)  # Compute derivative of sigmoid 
    delta_w = alpha * error * y_derivative * x  # Compute weight adjustment 
    w += delta_w  # Update weights 
    errors.append(abs(error))  # Store absolute error for plotting 
 
     
    print(f"Iteration {i+1}:") 
    print("Input:", x) 
    print("Net Input:", net_input) 
    print("Output (Sigmoid):", y) 
    print("Error:", error) 
    print("Weight Update:", delta_w) 
    print("Updated Weights:", w) 
    print("----------------------------------") 
print("Final Weights:", w) 
 
# Plot error reduction over iterations 
plt.plot(range(1, len(d) + 1), errors, marker='o', linestyle='-', 
color='r') 
plt.xlabel('Iteration') 
plt.ylabel('Absolute Error') 
plt.title('Error Reduction Over Iterations') 
plt.grid() 
plt.show() 

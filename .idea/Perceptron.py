import numpy as np
#initialize the sigmoid function (activation function) here
#and use the exp() method from numpy
def sigmoid(x): 
    return 1 / (1+np.exp(-x))

#initialize the training data set
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

#initialize the weights
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3,1)) - 1
print("random numbers")
print(synaptic_weights)


#back propagation method
for i in range(20000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    
    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    
    synaptic_weights += adjustments
    
print("Weights:")    
print(synaptic_weights)

print("Result:")
print(outputs)
import random, matplotlib.pyplot as plt 

x_length = []
sample_function_ensemble = []
steps = 500 #Number of steps
sample_functions_amount = 150 #Number of sample functions

for i in range(sample_functions_amount):
    x0 = 0
    list = []
    for j in range(steps):
        list.append(x0)
        x = random.uniform(0, 1.0)
        if x>0.5:
            k = 1
        elif x<0.5:
            k = -1
        else:
            k = 0
        x0 = x0 + k
    sample_function_ensemble.append(list)

for i in range(len(sample_function_ensemble[0])):
    x_length.append(i) #Get length of x

for y in sample_function_ensemble:
    plt.plot(x_length, y) #Plot

plt.title('Random Walk with %d steps and %d sample functions' % (steps, sample_functions_amount))
plt.show()
import random, matplotlib.pyplot as plt
import statistics, math, numpy

x_length = []
sample_function_ensemble = []
steps = 500 #Number of steps
sample_functions_amount = 150 #Number of sample functions

for i in range(sample_functions_amount):
    x0 = 0
    list = []
    for j in range(steps):
        list.append(x0)
        x = random.random()
        if x>0.5:
            k = 1
        elif x<0.5:
            k = -1
        else:
            k = 0
        x0 = x0 + k
    sample_function_ensemble.append(list)

mean = [] #Mean for all t
sd = [] #SD for all t
neg_sd = []

for j in range(len(sample_function_ensemble[0])):
    ensemble_on_t = []
    for i in sample_function_ensemble:
        ensemble_on_t.append(i[j])
    mean_on_t = statistics.mean(ensemble_on_t) #Get mean on time t
    sd_on_t = math.sqrt(statistics.variance(ensemble_on_t)) #Get sd/var on time t
    neg_sd_on_t = numpy.negative(sd_on_t)
    mean.append(mean_on_t)
    sd.append(sd_on_t)
    neg_sd.append(neg_sd_on_t)

max_val = numpy.max(sample_function_ensemble) #Get highest point reached
min_val = numpy.min(sample_function_ensemble) #Get lowest point reached
print('Max:',max_val,'\tMin:', min_val)
print('Average mean:', statistics.mean(mean))
print('Standard Deviation at end: \u00B1',sd_on_t)

for i in range(len(sample_function_ensemble[0])):
    x_length.append(i) #Get length of x/time

for y in sample_function_ensemble:
    plt.plot(x_length, y, linewidth = 0.5) #Plot

plt.plot(mean, linewidth = 2, color = 'red')
plt.plot(sd, linewidth = 2, color = 'black')
plt.plot(neg_sd, linewidth = 2, color = 'black')
plt.xticks(numpy.arange(0, steps+10, step=steps/10))
plt.title('Random Walk with %d steps and %d sample functions' % (steps, sample_functions_amount))
plt.show()
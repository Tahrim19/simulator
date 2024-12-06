## MG --- exponential/uniform
import random
import math

# Input values
a = float(input("Enter min value - a: "))  # Minimum value for service time
b = float(input("Enter max value - b: "))  # Maximum value for service time
totalPatients = int(input("Enter total patients: "))  # Total number of patients
lamb = 1/float(input("Enter lambda: "))

# exponential distribution CDF 
def exponential_cdf(x , lamb):
    if x < 0:
        return 0
    else:
        return 1 - math.exp(-lamb * x)


# ## Generate table
# print("sno. |  CP  |  CP(L) |   CP Range  | min# b/w arrival  |  Service Time  |  Inter-Arrival Time  | ")

# Generate table header
print(f"{'sno.':3} | {'CP':11} | {'CP(L)':12} | {'CP Range':20} |{'min#'}| {'Service Time':15} | {'Inter-Arrival Time':18} |")

previous_cp = 0
cp_values = []  # List to store CP values for each patient

for i in range(totalPatients):
    # Generate a random service time for each patient
    serviceTime = round(a + (b - a) * random.random())
    
    # Calculate cumulative probability (CP)
    cp = exponential_cdf(i, lamb)
    
    # Calculate CP(L) which starts from 0 and accumulates CP[i-1]
    cp_l = previous_cp
    previous_cp = cp  # Update for next iteration

    # Calculate min# between arrival
    min_no = i

    # CP Range
    cp_range = f"{cp_l:0.6f} -> {cp:0.6f}"
    
    # Add the CP value to the list for later use in inter-arrival time calculation
    cp_values.append(cp)

    # For the first patient, inter-arrival time is 0
    if i == 0:
        inter_arrival_time = 0
    else:
        # Generate a random number for inter-arrival time between 0 and 1
        random_inter_arrival = random.random()
        
        # Find the range in which the random number falls
        for j in range(len(cp_values) - 1):
            if random_inter_arrival >= cp_values[j] and random_inter_arrival < cp_values[j + 1]:
                # Inter-arrival time is the range index - 1
                inter_arrival_time = j
                break
    
    # Print the result for each patient
    print(f"{i + 1:3d} | {cp:12.6f} | {cp_l:12.6f} | {cp_range} | {min_no}  | {serviceTime:15d} | {inter_arrival_time:18d} | ")

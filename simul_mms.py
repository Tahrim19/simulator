import math
import random

# Input values
lamb = float(input("Enter lambda (λ): "))  # Average arrival rate
mu = float(input("Enter mu (μ): "))        # Average service time
num = int(input("Enter number of patients: "))  # Total number of patients
server=int(input("Enter number of server: "))
# Poisson cumulative probability function
def poisson_cumulative(lamb, k):
    cumulative_prob = 0
    for x in range(k + 1):
        while True:
            prob = (math.exp(-lamb) * lamb**x) / math.factorial(x)
            if(prob<=1):
                break
        cumulative_prob += prob
    return cumulative_prob

# Generate random service times for patients
service_times = []
for _ in range(num):
    while True:
        random_number = random.random()  # Generate a random number between 0 and 1
        service =int( round(-mu * math.log(random_number), 1))
        if service >= 1:
            break
    service_times.append(service)



# Initialize the previous cumulative probability
previous_cp = 0
ranges = []  # List to store the ranges and corresponding MIN values

# Display the table and create the ranges
print("\nPatient Details Table:")
print(f"{'Patient #':<10}{'Service Time':<15}{'CP Lookup':<15}{'CP':<15}{'MIN':<5}{'IA RANGE':<25}")

cp_array=[]
for i, service_time in enumerate(service_times, start=1):
    cp_val = poisson_cumulative(lamb, i-1)  # Calculate cumulative probability up to i-1
    min_val = i - 1  # MIN will range from 0 to num-1
    range_val = f"{previous_cp:.6f} - {cp_val:.6f}"  # Format range as 0 - 0.0007
    ranges.append((previous_cp, cp_val, min_val))  # Store the range and MIN value
    cp_array.append(cp_val)
  
    # Print the patient's details including Inter-Arrival Time (IA)
    print(f"{i:<10}{service_time:<15}{previous_cp:<15.6f}{cp_val:<15.6f}{min_val:<5}{range_val:<25}")

    # Update previous_cp for the next patient
    previous_cp = cp_val

# Generate inter-arrival times for patients
inter_arrival = [0]
for _ in range(1, num):
    while True:
        random_number = random.random()  # Generate a random number between 0 and 1
        IA = round(random_number, 1)
        if IA < cp_array[-1]:
            break
    inter_arrival.append(IA)


print(f"{'IA Final':<10}{'Arrival':<10}")

# Now check for which range the IA lies in and calculate the Arrival time
arrival = 0  # Initialize arrival time for the first patient
arrival_time = []

# Iterate through inter-arrival times and assign IA Final and calculate arrival times
for ia_value in inter_arrival:
    ia_final = "Out of Range"  # Default if IA is outside the range

    # Iterate through the ranges and find where the IA falls
    for lower, upper, min_val in ranges:
        if lower <= ia_value < upper:
            ia_final = min_val
            break  # Exit the loop once the range is found

    if ia_final == "Out of Range":
        raise ValueError("IA value is out of all specified ranges!")

    # Update arrival time by adding IA value to the previous arrival time
    arrival += ia_final
    arrival_time.append(arrival)


    
    # Display the result with the IA Final and the Arrival time
    print(f"{ia_final:<15}{arrival:<15}")
# Initialize lists for start time, completion time, turnaround time, and waiting time
Start_Time = [0] * num
Finish_Time = [0] * num
Turnaround_Time = [0] * num
Waiting_Time = [0] * num
Response_Time = [0] * num

# Server availability tracking
server_availability = [0] * server  # Stores the time when each server becomes available
server_tasks = [[] for _ in range(server)]  # To track tasks for each server

# Sort processes by arrival time (if not already sorted)
process_order = sorted(range(num), key=lambda i: arrival_time[i])

# Calculate start time, completion time, etc.
for i in process_order:
    # Assign server in a prioritized sequential manner
    assigned_server = -1
    for s in range(server):
        if server_availability[s] <= arrival_time[i]:
            assigned_server = s
            break
    if assigned_server == -1:
        # If all servers are busy, assign to the first server to become available
        assigned_server = min(range(server), key=lambda x: server_availability[x])

    # Start time is the later of server availability and patient arrival
    Start_Time[i] = max(server_availability[assigned_server], arrival_time[i])
    
    # Completion time is the start time + service time
    Finish_Time[i] = Start_Time[i] + service_times[i]
    
    # Turnaround time is completion time - arrival time
    Turnaround_Time[i] = Finish_Time[i] - arrival_time[i]
    
    # Response time is start time - arrival time
    Response_Time[i] = Start_Time[i] - arrival_time[i]
    
    # Waiting time is turnaround time - service time
    Waiting_Time[i] = Turnaround_Time[i] - service_times[i]
    
    # Update server availability
    server_availability[assigned_server] = Finish_Time[i]
    
    # Append the task to the server's task list (for Gantt chart)
    server_tasks[assigned_server].append((Start_Time[i], Finish_Time[i], i))  # (start time, finish time, process)

# Print the results
print("\nP\tAT\tService\tST\tET\tTAT\tWT")
for i in range(num):
    print(f"P{i}\t{arrival_time[i]}\t{service_times[i]}\t{Start_Time[i]}\t{Finish_Time[i]}\t{Turnaround_Time[i]}\t{Waiting_Time[i]}")

# Print Separate Gantt Charts for Each Server
print("\nGantt Charts for Each Server:")
for s in range(server):
    print(f"\nServer {s+1}:")
    current_time = 0
    print("|", end="")
    for task in server_tasks[s]:
        start, finish, process = task
        
        # Add idle time if there's a gap between current_time and task start time
        if start > current_time:
            idle_time = start - current_time
            for _ in range(idle_time):
                print(" IDLE |", end="")
        
        # Add the process execution time
        for _ in range(finish - start):
            print(f" P{process} |", end="")
        
        # Update current time to the finish time of the task
        current_time = finish
    print("|")

# Performance Metrics
util = sum(Finish_Time) - sum(Start_Time)
ser = sum(service_times)
ta = sum(Turnaround_Time)
rt = sum(Response_Time)
wt = sum(Waiting_Time)

avg_ta = ta / num
avg_rt = rt / num
avg_ser = ser / num
avg_wt = wt / num

utilization = util / (server * max(Finish_Time))  # Divide by total server time
print("\n")
print(f"Server Utilization: {utilization:.2f}")
print(f"Avg Wait Time: {avg_wt:.2f}")
print(f"Avg Response Time: {avg_rt:.2f}")
print(f"Avg Turn Around Time: {avg_ta:.2f}")
print(f"Avg Service Time: {avg_ser:.2f}")

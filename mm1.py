import math
def MM1(mean_interarrival, mean_service):
    lam = 1 / mean_interarrival  # Arrival rate (lambda)
    meu = 1 / mean_service       # Service rate (mu)
    rho = mean_service / mean_interarrival  # Utilization rate (rho)
    if rho>=1:
        raise(Exception("Cannot be greater than 1"))
    # Calculating metrics
    number_in_queue = rho ** 2 / (1 - rho)
    wait_in_queue = number_in_queue / lam
    wait_in_system = wait_in_queue + (1 / meu)
    number_in_system = wait_in_system * lam
    proportion = 1 - rho
    
    # Printing results with formatted strings
    print(f"Number in queue = {number_in_queue}")
    print(f"Wait in queue = {wait_in_queue}")
    print(f"Wait in system = {wait_in_system}")
    print(f"Number in system = {number_in_system}")
    print(f"Proportion of time server is idle = {proportion}")

# Taking input from the user
mean_interarrival = float(input("Enter mean interarrival: "))
mean_service = float(input("Enter mean service: "))
MM1(mean_interarrival, mean_service)

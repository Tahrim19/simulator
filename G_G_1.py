# import math

# def GG1(lamda, mu, variance_interarrival, variance_service):
#     p = mu / lamda
#     Ca2 = variance_interarrival / (lamda**2)
#     Cs2 = variance_service / (mu**2)
#     Lq = ((p**2)*(1+Cs2)*(Ca2 + ((p**2)*Cs2))) / (2*(1-p) * (1 + ((p**2)*Cs2))) 
#     Wq = Lq / (1/lamda)
#     Ws = Wq + (1/(1/mu))
#     Ls = (1/lamda) * Ws
#     idle = 1 - p
    
#     return p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle

# lamda = float(input("Enter the value for λ (arrival rate): "))
# mu = float(input("Enter the value for mean service time (µ): "))
# variance_interarrival = float(input("Enter the variance of interarrival time: "))
# variance_service = float(input("Enter the variance of service time: "))

# p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle= GG1(lamda, mu, variance_interarrival, variance_service)

# print(f"Utilization factor (p): {p}")
# print(f"Coefficient of variation of service time (Cs^2): {Cs2:.3f}")
# print(f"Coefficient of variation of arrival process (Ca^2): {Ca2:.3f}")
# print(f"Average number in the queue (Lq): {Lq:.3f}")
# print(f"Average wait in the queue (Wq): {Wq:.3f} minutes")
# print(f"Average number in the system (Ls): {Ls:.3f}")
# print(f"Average wait in the system (Ws): {Ws:.3f} minutes")
# print(f"Proportion of time service is (idle): {idle:.2f}")



import math

def GG1(lamda, mu, variance_interarrival, variance_service):
    p = mu / lamda
    Ca2 = variance_interarrival / (lamda**2)
    Cs2 = variance_service / (mu**2)
    Lq = ((p**2)*(1+Cs2)*(Ca2 + ((p**2)*Cs2))) / (2*(1-p) * (1 + ((p**2)*Cs2))) 
    Wq = Lq / (1/lamda)
    Ws = Wq + (1/(1/mu))
    Ls = (1/lamda) * Ws
    idle = 1 - p
    
    return p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle

def get_distribution_parameters(parameter_type):
    print(f"\nEnter parameters for the {parameter_type} time distribution.")
    distribution_type = input("Choose the distribution type (Gamma, Uniform, Normal): ").strip().lower()
    
    if distribution_type == "gamma":
        mean = float(input(f"Enter the mean {parameter_type} time for Gamma distribution: "))
        variance = float(input(f"Enter the variance of {parameter_type} time for Gamma distribution: "))
        
    elif distribution_type == "uniform":
        min_value = float(input(f"Enter the minimum {parameter_type} time for Uniform distribution: "))
        max_value = float(input(f"Enter the maximum {parameter_type} time for Uniform distribution: "))
        mean = (min_value + max_value) / 2
        variance = ((max_value - min_value) ** 2) / 12
        # mean = float(input(f"Enter the mean {parameter_type} time for Uniform distribution: "))
        # variance = float(input(f"Enter the variance of {parameter_type} time for uniform distribution: "))
        
    elif distribution_type == "normal":
        mean = float(input(f"Enter the mean {parameter_type} time for Normal distribution: "))
        variance = float(input(f"Enter the standard deviation of {parameter_type} time for Normal distribution: "))
        # variance = std_dev ** 2
    
    else:
        print("Invalid distribution type. Please choose either Gamma, Uniform, or Normal.")
        return None, None

    return mean, variance

def main():
    # Get inter-arrival parameters
    mean_interarrival, variance_interarrival = get_distribution_parameters("inter-arrival")
    if mean_interarrival is None:
        print("Exiting due to invalid inter-arrival input.")
        return
    
    # Get service parameters
    mean_service, variance_service = get_distribution_parameters("service")
    if mean_service is None:
        print("Exiting due to invalid service input.")
        return
    
    # Calculate arrival rate (λ) and service rate (μ)
    lamda = mean_interarrival
    mu = mean_service

    # Call GG1 with obtained values
    p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle = GG1(lamda, mu, variance_interarrival, variance_service)

    if p >= 1:
        print("\nSystem is overloaded (p >= 1). Infinite queue and wait times expected.")
        return
    
    # Print results
    print(f"\nPerformance Metrics for G/G/1 Queue:")
    print(f"Utilization factor (p): {p:.3f}")
    print(f"Coefficient of variation of service time (Cs^2): {Cs2:.3f}")
    print(f"Coefficient of variation of arrival process (Ca^2): {Ca2:.3f}")
    print(f"Average number in the queue (Lq): {Lq:.3f}")
    print(f"Average wait in the queue (Wq): {Wq:.3f} minutes")
    print(f"Average number in the system (Ls): {Ls:.3f}")
    print(f"Average wait in the system (Ws): {Ws:.3f} minutes")
    print(f"Proportion of time service is idle: {idle:.3f}")

# Run the main function
if __name__ == "__main__":
    main()


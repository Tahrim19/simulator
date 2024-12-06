import math

def GGs(lamda, mu, variance_interarrival, variance_service, s):
    # Utilization factor per server
    p = lamda / (s * mu)
    Ca2 = variance_interarrival / (1 / lamda ** 2)
    Cs2 = variance_service / (1 / mu ** 2)
    
    # Adjusted coefficient of variation and parameters
    Lq = ((p * 2) * (1 + Cs2) * (Ca2 + (p * 2) * Cs2)) / (2 * (1 - p) * (1 + (p ** 2) * Cs2)) if p < 1 else float('inf')
    Wq = Lq / lamda
    Ws = Wq + (1 / mu)
    Ls = lamda * Ws
    idle = 1 - p if p < 1 else 0
    
    return p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle

def get_distribution_parameters(parameter_type):
    print(f"\nEnter parameters for the {parameter_type} time distribution.")
    distribution_type = input("Choose the distribution type (Gamma, Uniform, Normal): ").strip().lower()
    
    if distribution_type == "gamma":
        mean = float(input(f"Enter the mean {parameter_type} time for Gamma distribution: "))
        variance = float(input(f"Enter the variance of {parameter_type} time for Gamma distribution: "))
        
    elif distribution_type == "uniform":
        min_val = float(input(f"Enter the minimum {parameter_type} time for Uniform distribution: "))
        max_val = float(input(f"Enter the maximum {parameter_type} time for Uniform distribution: "))
        mean = (min_val + max_val) / 2
        # variance = float(input(f"Enter the variance of {parameter_type} time for Uniform distribution: "))
        variance = ((max_val - min_val) ** 2) / 12
        
    elif distribution_type == "normal":
        mean = float(input(f"Enter the mean {parameter_type} time for Normal distribution: "))
        variance = float(input(f"Enter the variance of {parameter_type} time for Normal distribution: "))
    
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
    lamda = 1 / mean_interarrival
    mu = 1 / mean_service

    # Get number of servers (s)
    s = int(input("Enter the number of servers: "))
    if s <= 0:
        print("Invalid number of servers. Must be at least 1.")
        return
    
    # Call G/G/s with obtained values
    p, Cs2, Ca2, Lq, Wq, Ws, Ls, idle = GGs(lamda, mu, variance_interarrival, variance_service, s)

    # Check for overload and avoid printing further metrics
    if p >= 1:
        print("\nSystem is overloaded (p >= 1). Infinite queue and wait times expected.")
        return

    # Print results if system is stable
    print(f"\nPerformance Metrics for G/G/{s} Queue:")
    print(f"Utilization per server (p): {p:.2f}")
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
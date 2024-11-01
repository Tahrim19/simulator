def get_user_input():
    inter_arrival_time = float(input("Enter the inter-arrival time: "))
    lambda_rate = 1 / inter_arrival_time  

    service_distribution = input("Enter the service time distribution (e.g., 'normal', 'gamma', 'uniform'): ")

    if service_distribution == 'normal':
        mean_service_time = float(input("Enter the mean service time: "))
        std_dev_service_time = float(input("Enter the standard deviation of service time: "))
        mu = 1 / mean_service_time  
        return lambda_rate, mu, 'normal', mean_service_time, std_dev_service_time

    elif service_distribution == 'uniform':
        a = float(input("Enter the minimum service time (a): "))
        b = float(input("Enter the maximum service time (b): "))
        mean_service_time = (a + b) / 2
        mu = 1 / mean_service_time  
        return lambda_rate, mu, 'uniform', a, b
    
    elif service_distribution == 'gamma':
        k = float(input("Enter the shape parameter (k): "))
        theta = float(input("Enter the scale parameter (θ): "))
        mean_service_time = k * theta
        mu = 1 / mean_service_time  
        return lambda_rate, mu, 'gamma', k, theta

    else:
        raise ValueError("Unsupported distribution type.")

def calculate_queue_parameters(lambda_rate, mu, service_distribution, *params):
    # Get the number of servers from the user
    s = int(input("Enter the number of servers (s): "))
    rho = lambda_rate / (s * mu)
    
    if rho >= 1:
        raise ValueError("Utilization factor cannot be 1 or greater. Please adjust λ or the number of servers.")

    if service_distribution == 'normal':
        mean_service_time, std_dev_service_time = params
        sigma_s2 = std_dev_service_time ** 2

    elif service_distribution == 'gamma':
        k, theta = params
        mean_service_time = k * theta
        sigma_s2 = k * (theta ** 2)

    elif service_distribution == 'uniform':
        a, b = params
        mean_service_time = (a+b)/2
        sigma_s2 = ((b - a) ** 2) / 12

    else:
        raise ValueError("Unsupported distribution type.")

    # Calculate performance metrics
    L = lambda_rate * mean_service_time + (lambda_rate ** 2 * sigma_s2) / (2 * s * (1 - rho))
    W = L / lambda_rate
    L_q = L - lambda_rate / mu
    W_q = L_q / lambda_rate
    idle_time = 1 - rho

    return L, W, L_q, W_q, idle_time, rho

def main():
    user_inputs = get_user_input()
    lambda_rate, mu, service_distribution, *params = user_inputs
    
    L, W, L_q, W_q, idle_time, server_utilization = calculate_queue_parameters(lambda_rate, mu, service_distribution, *params)

    print(f"\nPerformance Metrics for M/G/s Queue:")
    print(f"Average number of customers in the system (L): {L:.4f}")
    print(f"Average time a customer spends in the system (W): {W:.4f}")
    print(f"Average number of customers in the queue (Lq): {L_q:.4f}")
    print(f"Average time a customer spends waiting in the queue (Wq): {W_q:.4f}")
    print(f"Time the server was idle: {idle_time:.2f}")
    print(f"Utilization factor (U): {server_utilization:.4f}")

if __name__ == "__main__":
    main()

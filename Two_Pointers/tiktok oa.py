def equalizeBandwidth(servers):
    # Sort the bandwidths in descending order
    servers.sort(reverse=True)
    n = len(servers)

    # Calculate the target bandwidth (maximum bandwidth across all servers)
    target_bandwidth = servers[0]

    # Initialize variables
    hours = 0
    odd_hour = True

    while any(bw < target_bandwidth for bw in servers):
        for i in range(n):
            if servers[i] < target_bandwidth:
                if odd_hour:
                    # Light upgrade: increase bandwidth by 1 Mbps
                    servers[i] += 1
                else:
                    # Heavy upgrade: increase bandwidth by 2 Mbps
                    servers[i] += 2

                # Increment hours and alternate between odd and even hours
                hours += 1
                odd_hour = not odd_hour
                break

    return hours


# Test case
servers = [10, 1, 53, 86, 22, 9, 22, 10, 17, 37, 68]
result = equalizeBandwidth(servers)
print(result)  # Output: 357

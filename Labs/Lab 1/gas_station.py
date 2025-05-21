import heapq

# Function to calculate the minimum number of refueling stops


def min_stops(D, M, S):
    S.append(D)  # Add the destination as the final "gas station"
    num_stops = 0
    current_fuel = M
    prev_station = 0
    max_heap = []  # Use negatives to simulate a max-heap with heapq

    for i in range(len(S)):
        distance = S[i] - prev_station

        # Refuel if we can't reach the next station
        while current_fuel < distance:
            if not max_heap:
                return -1  # Destination is not reachable

            # Refuel from the largest available fuel station
            current_fuel -= heapq.heappop(max_heap)
            num_stops += 1

        current_fuel -= distance

        # Push available fuel amount to heap (simulate max-heap using negative values)
        if i < len(S) - 1:
            heapq.heappush(max_heap, -(M - current_fuel))

        prev_station = S[i]

    return num_stops


if __name__ == "__main__":
    # Input
    D = int(input("Enter the total distance (D): "))
    M = int(input("Enter the maximum fuel range (M): "))
    S = list(map(int, input(
        "Enter the distances of the gas stations separated by spaces: ").split()))

    # Output
    result = min_stops(D, M, S)
    if result != -1:
        print(f"Minimum number of stops: {result}")
    else:
        print("Destination is not reachable.")

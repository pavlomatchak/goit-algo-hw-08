import heapq

def cable_costs(cable_lengths):
    total_cost = 0
    heapq.heapify(cable_lengths)

    while len(cable_lengths) > 1:
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        new_cable = cable1 + cable2
        total_cost += new_cable
        heapq.heappush(cable_lengths, new_cable)

    return total_cost

cable_lengths = [3, 8, 2, 15]
result = cable_costs(cable_lengths)
print(f"Витрати: {result}")

def min_chocolate_break_cost(test_cases):
    results = []
    for _ in range(test_cases):
        m, n = map(int, input().split())
        x_cuts = [int(input()) for _ in range(m-1)]
        y_cuts = [int(input()) for _ in range(n-1)]
        x_cuts.sort(reverse=True)
        y_cuts.sort(reverse=True)
        total_cost = 0
        x_count = 0
        y_count = 0
        while x_cuts or y_cuts:
            if not y_cuts or (x_cuts and x_cuts[0] > y_cuts[0]):
                total_cost += x_cuts.pop(0) * (y_count + 1)
                x_count += 1
            else:
                total_cost += y_cuts.pop(0) * (x_count + 1)
                y_count += 1
        results.append(total_cost)
    return results
test_cases = int(input())
results = min_chocolate_break_cost(test_cases)
for result in results:
    print(result)

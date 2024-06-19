def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# Take input from user
weights = list(map(int, input("Enter the weights separated by spaces: ").split()))
values = list(map(int, input("Enter the values separated by spaces: ").split()))
capacity = int(input("Enter the maximum capacity: "))
max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)

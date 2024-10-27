def min_coins(coins, target_amount):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0 
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target_amount] if dp[target_amount] != float('inf') else -1

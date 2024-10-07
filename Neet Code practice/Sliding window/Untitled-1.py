#Buy and Sell Crypto Aadil Rashid 8/29/24



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        # Initialize pointers and variables
        left = 0
        max_profit = 0
        
        # Iterate through the prices with the right pointer
        for right in range(1, len(prices)):
            # Update minimum price seen so far
            min_price = min(prices[left:right])
            # Calculate potential profit if selling on the current day
            current_profit = prices[right] - min_price
            # Update maximum profit
            max_profit = max(max_profit, current_profit)
            
            # Move the left pointer to maintain the sliding window
            if prices[right] < prices[left]:
                left = right
        
        return max_profit
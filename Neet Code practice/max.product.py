#max product

def maxProduct(nums):
    if not nums:
        return 0

    # Initialize the variables
    max_product = nums[0]
    min_product = nums[0]
    global_max_product = nums[0]
    
    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        num = nums[i]
        
        # Store the current max_product before updating
        temp_max = max_product
        
        # Update the max_product and min_product
        max_product = max(num, num * temp_max, num * min_product)
        min_product = min(num, num * temp_max, num * min_product)
        
        # Update the global maximum product
        global_max_product = max(global_max_product, max_product)
    
    return global_max_product



nums1 = [2, 3, -2, 4]
print(maxProduct(nums1))
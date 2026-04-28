class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using dict for O(n)
        # Simply put, we go through the array only O(n)
        # because we add the number first time, and don't 
        # have to compare to all to all

        # Using this dict to track our seen
        seen = {}

        # Track length with a var for simplicty cuz im stupid
        x = len(nums)

        # This loop goes through once, and adds to the dict
        # The if checks if the number was already added

        # CORRECTIONS TO LOGIC, 
        # Add to dict AFTER check - IMPORTANT
        # OTHERWISE WE RETURN TRUE INDEFINITELY
        for i in range(x):
            #print(nums[i])
            
            if nums[i] in seen:
                return True
            seen[nums[i]] = i   # Adding to dictionary from the key
            #seen[i] = nums[i]  # THIS IS WRONG WAY, ABOVE IS CORRECTED
        
        return False          # Necessary fall back, cuz getting here means it failed all prior checks
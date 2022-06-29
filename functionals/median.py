
def median(*nums: tuple) -> int:
    """Returns the mid-object of the supplied list."""
    ltype = len(nums)%2
    mid_obj = len(nums)//2

    if ltype != 0:
        return nums[len(nums)//2]
    else:
        return (nums[mid_obj] + nums[mid_obj - 1])/2

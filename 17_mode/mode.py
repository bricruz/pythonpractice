def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # most = None
    dict = {}
    for num in set(nums):
        dict[num] = nums.count(num)

    most = list(dict.keys())[0]

    for k in dict:
        if dict[k] > most:
            most = k
    
    return most
    

print(mode([1,2,1]))
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
    counts = {}

    for num in nums:
        counts[num] = nums.count(num)

    count_nums = list(counts.values())

    for num in count_nums:
        count_indx = count_nums.index(num)

        if num > count_indx + 1:
            return counts[num]
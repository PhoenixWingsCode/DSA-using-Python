def longest_subarray_with_limit(nums, limit):
    from collections import deque
    max_dq = deque()  # stores elements in decreasing order
    min_dq = deque()  # stores elements in increasing order

    left = 0
    max_length = 0

    for right in range(len(nums)):
        # Trigger based on current element
        while max_dq and nums[right] > max_dq[-1]:
            max_dq.pop()
        max_dq.append(nums[right])

        while min_dq and nums[right] < min_dq[-1]:
            min_dq.pop()
        min_dq.append(nums[right])

        # Trigger left pointer movement when current window invalid
        while max_dq[0] - min_dq[0] > limit:
            if max_dq[0] == nums[left]:
                max_dq.popleft()
            if min_dq[0] == nums[left]:
                min_dq.popleft()
            left += 1  # Trigger left pointer to move

        max_length = max(max_length, right - left + 1)

    return max_length
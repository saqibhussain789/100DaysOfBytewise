def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [list(intervals[0])]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(list(current))
    return merged

# Test the function
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
print("Merged intervals:", merge_intervals(intervals))

# Function to take input from user
def input_intervals():
    n = int(input("Enter the number of intervals: "))
    intervals = []
    for _ in range(n):
        start, end = map(int, input("Enter the start and end of the interval separated by space: ").split())
        intervals.append((start, end))
    return intervals

# Take input from user and test the function
intervals = input_intervals()
print("Merged intervals:", merge_intervals(intervals))

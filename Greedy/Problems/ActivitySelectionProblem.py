def activity_selection(activities):
    # Sort activities based on their end times
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # The first activity always gets selected
    selected_activities = [sorted_activities[0]]
    
    # Track the end time of the last selected activity
    last_end_time = sorted_activities[0][1]
    
    # Iterate through the sorted activities
    for i in range(1, len(sorted_activities)):
        # If the start time of the current activity is greater or equal to the end time of the last selected activity
        if sorted_activities[i][0] >= last_end_time:
            selected_activities.append(sorted_activities[i])
            last_end_time = sorted_activities[i][1]
    
    return selected_activities

# Example usage
activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
selected = activity_selection(activities)
print("Selected activities:", selected)

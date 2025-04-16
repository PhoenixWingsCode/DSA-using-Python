import heapq

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Initialize result array and a time slot array
    result = [None] * n
    slot = [False] * n
    
    # Iterate through all given jobs
    for job in jobs:
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.id
                break
    
    # Filter out None values and return the job sequence
    return [job_id for job_id in result if job_id is not None]

# Example usage
jobs = [Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27), Job(4, 1, 25), Job(5, 3, 15)]
n = 3  # Number of time slots
sequence = job_sequencing(jobs, n)
print("Job sequence:", sequence)

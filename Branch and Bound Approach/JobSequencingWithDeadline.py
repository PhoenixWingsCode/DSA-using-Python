class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadline(jobs):
    # Sort jobs by decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    result = [None] * n  # To store the result (sequence of jobs)
    slot = [False] * n   # To keep track of free time slots

    # Iterate through all given jobs
    for job in jobs:
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break

    # Filter out None values and return the job sequence
    return [job_id for job_id in result if job_id is not None]

# Example usage
jobs = [
    Job('Job1', 2, 100),
    Job('Job2', 1, 19),
    Job('Job3', 2, 27),
    Job('Job4', 1, 25),
    Job('Job5', 3, 15)
]

sequence = job_sequencing_with_deadline(jobs)
print("Job sequence to maximize profit:", sequence)

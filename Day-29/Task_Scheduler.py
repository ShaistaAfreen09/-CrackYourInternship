class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        jobs = list(counts.values())
        largest_job = max(jobs)
        num_largest_jobs = jobs.count(largest_job)
        res = (max(jobs) - 1) * (n + 1) + num_largest_jobs
        res = max(res, len(tasks))
        return res
        
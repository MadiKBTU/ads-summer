import heapq


priority_queue = []

heapq.heappush(priority_queue, (2, 'task 2'))
heapq.heappush(priority_queue, (1, 'task 1'))
heapq.heappush(priority_queue, (3, 'task 3'))

print("Peek:", priority_queue[0])

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Processing {task} with priority {priority}")
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
import queue


def read_command(command):
    return command.split(' ')

def enqueue(queue, element):
    queue.put(element)

def dequeue(queue):
    return queue.get()

def get_front(q):
    return q.queue[0] if q.qsize() > 0 else None

    
n = int(input())
ops = []
for item in range(n):
    ops.append(input())

q = queue.Queue()

for raw_command in ops:
    parsed_command =  read_command(raw_command)
    
    command = int(parsed_command[0])

    if command == 1:
        enqueue(q,parsed_command[1])
    elif command == 2:  
        dequeue(q)
    elif command == 3:
        print(get_front(q))

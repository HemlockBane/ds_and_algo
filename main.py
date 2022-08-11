
import re
from typing import List
from lists.patterns import two_pointers as tp
from lists import study_questions
from lists.patterns import sliding_window as sw
from queues.implementation.queue_with_stacks import QueueWithStacks
from sorting_algorithms import basic_sorting_algo
from stacks.study_questions import is_valid


queue = QueueWithStacks()
queue.enqueue("Ray")
queue.enqueue("Brian")
queue.enqueue("Eric")

print(queue.length())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.length())















# Stacks and Queues
A stack is a First In Last Out(FILO) data structure that knows the value on top and which is the next value. A Queue is a First In First Out(FIFO) data structure that knows what values are at the front and rear.

## Challenge
Stack and a Queue Implementation

## Approach & Efficiency
All methods have a Time of O(1) because none of them depend on the size of the stack/queue or inputs given to them. Space has O(1) for all except push in stack class and enqueue in queue which have O(n) because they depend on the size of the input given to them

## API

Stack:
  - is_empty: returns a boolean if the stack is empty or not
  - peek: returns the top value
  - push: adds a value to the top
  - pop: removes a value from the top

Queue:
  - is_empty: returns a boolean if the queue is empty or not
  - enqueue: adds a value to the end of the queue
  - dequeue: removes a value from the front of the queue
  - peek: returns the front value



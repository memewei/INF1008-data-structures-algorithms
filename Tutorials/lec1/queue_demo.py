from queue import Queue

aQueue = Queue()
aQueue.enqueue("apple")
aQueue.print()
aQueue.enqueue("pear")
aQueue.enqueue("grape")
aQueue.print()
aQueue.dequeue()
aQueue.print()
aQueue.enqueue("banana")
aQueue.print()
aQueue.dequeue()
aQueue.print()

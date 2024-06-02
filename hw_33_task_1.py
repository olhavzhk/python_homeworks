import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(Counter.rounds):
            Counter.counter += 1


t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(Counter.counter)

# Despite the potential for race conditions, I see 200000 every time I run the cose due to:
#
# Processor and OS Scheduling:
# On some systems, the threading and process scheduling might consistently result in the threads running
# without interference in the specific context of this simple test.
# This could be due to the relatively low contention and short duration of the operation.
#
# GIL (Global Interpreter Lock):
# In CPython, which is the most common implementation of Python,
# the Global Interpreter Lock (GIL) prevents multiple native threads from executing Python bytecodes at once.
# This can effectively serialize the thread execution in this case, mitigating race conditions.
# However, this is an implementation detail of CPython and should not be relied upon.

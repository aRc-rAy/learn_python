import threading
import time

def producer():
    for i in range(1, 6):
        print(f"Producing item {i}")
        yield i  # Yielding instead of returning allows data flow in a thread
        time.sleep(1)

def consumer(gen):
    for item in gen:
        print(f"Consuming item {item}")
        time.sleep(2)

# Run producer and consumer in separate threads
producer_gen = producer()
print(f"list of gens are : {producer_gen}")
print(f"list of gens are : {next(producer_gen)}")
t1 = threading.Thread(target=consumer, args=(producer_gen,))
t1.start()
t1.join()

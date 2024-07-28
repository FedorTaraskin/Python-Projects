import time

def cpu_benchmark():
    start_time = time.time()
    
    # Perform a CPU-intensive task
    result = 0
    for i in range(10**6):
        result += i
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"CPU benchmark completed in {execution_time} seconds")

if __name__ == "__main__":
    cpu_benchmark()
input()
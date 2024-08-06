import numba
import time

def compute_without_numba(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

@numba.jit(cache=True)
def compute_with_numba(n: int) -> int:
    result = 0
    for i in range(n):
        result += i ** 2
    return result

n = 1000000

start_time = time.time()
compute_without_numba(n)
compute_without_numba(n)
end_time = time.time()
print(f"Time without Numba: {end_time - start_time} seconds")

start_time = time.time()
compute_with_numba(n)
compute_with_numba(n)
end_time = time.time()
print(f"Time with Numba: {end_time - start_time} seconds")
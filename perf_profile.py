from algo import run_algo
from contextlib import contextmanager
import time

# Pick your items from this list. (Makes the df length to the power of 10
items_list = [
    0,  # 1 row input
    1,  # 10 row input
    2,  # 100 row input
    3,  # 1,000 row input
    4,  # 10,000 row input
    5,  # 100,000 row input
    # 6,  # 1,000,000 row input
    # 7,  # 10,000,000 row input
]


@contextmanager
def track_elapsed_time():
    """
    Track the time taken to run a function
    """
    start = time.time()
    try:
        yield None
    finally:
        elapsed = round((time.time() - start), 4)
        print(f"Completed in: {elapsed} seconds ")


@track_elapsed_time()
def safe_run_algo(factor):
    print(f"--> Running for factor {factor}")
    try:
        return run_algo(factor)
    except Exception as e:
        print("Something went wrong, error with:", e)
        return None


def run_for_item():
    print("Starting performance profiling")
    results = [safe_run_algo(item) for item in items_list]
    print("Performance profiling complete")
    return results


if __name__ == "__main__":
    run_for_item()

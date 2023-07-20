# Python Code Profiling

_How efficient is the code ?_

This project creates a mock algorithm, and showcases several tools that can be used to profile
the code to understand its impact on CPU and RAM.


## Setup

To create a virtual env and install the packages:

```shell script
virtualenv venv -p python3.7 # 3.7 is not really necessary, but can be used
source venv/bin/activate
pip install -r req.txt
```

You can also use pipenv as a package manager to build a virtual environment

```shell script
pipenv install
```

## Project Structure

- `algo.py`: Contains the functions to the mock algorithm
- `tests.py`: Contains tests for the algo functions
- `perf_profiling.py`: Contains simple logic to run the algorithm with different 
input values, used as the means of entry for the profiling scripts.

## Profiling Commands

Use these commands to profile your code.

#### Standard Python Timing

Check how long it takes for each input variable

```shell script
python -m perf_profile.py
```


#### Total CPU Profiling

Complete `cpython` based profile, coupled with `snakeviz` for visualisation. Shouldn't be used 
with a `@profile` decorator

```shell script
bash cpu_profile.sh
```


#### Total MEM Profiling 

Creates a graph based on memory usage. Can be used with a `@profile` decorator

```shell script
bash mem_graph.sh
```

#### Function Based CPU Profiling 

Profiles every function for CPU usage line by line. Should be used with a `@profile` decorator.

```shell script
bash cpu_profile_by_line.sh
```

#### Function Based MEM Profiling 

Profiles every function for MEM usage line by line. Should be used with a `@profile` decorator.

```shell script
bash mem_profile_by_line.sh
```

## Tests

To run tests:

```shell script
pytest --cov tests.py
```


# Make sure to add the @profile decorator to the functions as needed before running this script
script_path=$(pwd)/perf_profile.py
python -m memory_profiler $script_path

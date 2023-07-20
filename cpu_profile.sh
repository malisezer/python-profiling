# Runs the profiler script, and saves the results
timestamp=$(date +%s)
echo "Running profiler with ID: $timestamp"
script_path=$(pwd)/perf_profile.py
result_path=$(pwd)/results/cpu-profile-$timestamp.stats
if python -m cProfile -o $result_path $script_path ; then
  echo "Results Saved: $result_path"
  snakeviz $result_path
fi

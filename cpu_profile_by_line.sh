# Make sure to add the @profile decorator to the functions as needed before running this script
timestamp=$(date +%s)
echo "Running profiler with ID: $timestamp"
script_path=$(pwd)/perf_profile.py
result_path=$(pwd)/results/cpu-line-profile-$timestamp.txt
kernprof -l -v $script_path
python -m line_profiler $script_path.lprof > $result_path
rm $script_path.lprof

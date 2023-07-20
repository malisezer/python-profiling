timestamp=$(date +%s)
echo "Running mem graph with ID: $timestamp"
script_path=$(pwd)/perf_profile.py
result_path=$(pwd)/results/mem_graph_$timestamp.dat

if mprof run -o $result_path $script_path; then
  echo "Results Saved: $result_path"
  mprof plot $result_path --backend MacOSX
fi

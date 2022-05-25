# live data viewer graph
# to be ran on raspberry pi unix system with google chrome installed
DIR="$(dirname $(readlink -f $0))"
google-chrome --allow-file-access-from-files "file://${DIR}/local_file_monitor.html?data_dir=${DIR}"

# live data viewer graph
# to be ran on raspberry pi unix system with google chrome installed
DIR="$(dirname $(readlink -f $0))"
RASPBERRY_DIR="/home/pi/Documents/Wireless_Gateway/MAG"
chromium-browser --allow-file-access-from-files "file:///${DIR}/local_file_monitor.html?data_dir=${RASPBERRY_DIR}"

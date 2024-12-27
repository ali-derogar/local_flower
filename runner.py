import subprocess
import sys
import time
import webbrowser
from source.flower_csv_result_getter import Flower

index = "flower2"  # You can change this to "flower" if needed

def fetch_and_process_data():
    flower = Flower(
        authorization="Basic YWRtaW46YXZEVEB0T0x4MXRjQitWTWh4c1lBVlltZz0=",
        url="http://5.181.158.56:64626/tasks"
    )

    result = flower.get_flower_sorted_result()
    if result:
        result = flower.clean_result_data(result)
        flower.save_result_to_json(result)

def start_http_server():
    subprocess.Popen([sys.executable, '-m', 'http.server', '8000'])
    
def open_browser():
    url = f"http://0.0.0.0:8000/source/{index}.html"
    webbrowser.open(url)

if __name__ == "__main__":
    fetch_and_process_data()
    start_http_server()
    open_browser()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Server stopped.")

import speedtest as st
import requests
from datetime import datetime, timezone, timedelta
from time import gmtime, strftime
from dateutil import tz
from pytz import timezone

def get_new_speeds():
    try:
        speed_test = st.Speedtest()
        speed_test.get_best_server()
        server=speed_test.get_best_server()

        # Get ping (miliseconds)
        ping = speed_test.results.ping
        # Perform download and upload speed tests (bits per second)
        download = speed_test.download()
        upload = speed_test.upload()

        # Convert download and upload speeds to megabits per second
        download_mbs = round(download / (10**6), 2)
        upload_mbs = round(upload / (10**6), 2)

        now_utc = datetime.now(timezone('UTC'))
        date_today = now_utc.astimezone(timezone('America/Santiago')).strftime("%Y/%m/%d %T")
        date= now_utc.astimezone(timezone('America/Santiago')).strftime("%Y/%m/%d")

        return (date_today,ping, download_mbs, upload_mbs,date,server["sponsor"])
    except Exception as e:
        print("An error occurred while running the speed test:", e)
        return None

new_speeds = get_new_speeds()
if new_speeds is not None:
    params=new_speeds
    data={
        "Datetime":new_speeds[0],
        "Ping":new_speeds[1],
        "Download":new_speeds[2],
        "Upload":new_speeds[3],
        "Fecha":new_speeds[4],
        "Server":new_speeds[5]
    }
    response = requests.post("http://127.0.0.1:8000/",json=data)
    print(response.status_code)
else:
    print("No se pudo realizar conexión")
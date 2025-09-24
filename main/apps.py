from django.apps import AppConfig
import sys
import threading
import time
import urllib.request
import ssl
import certifi


def ping_server():
    """Pings the server to keep it alive."""
    url = "https://acm-django.onrender.com"
    ping_interval_seconds = 300
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    while True:
        try:
            with urllib.request.urlopen(url, context=ssl_context) as response:
                if response.getcode() == 200:
                    print(f"Successfully pinged {url}. Status code: 200")
                else:
                    print(f"Ping to {url} failed with status code: {response.getcode()}")
        except Exception as e:
            print(f"An error occurred while pinging {url}: {e}")
        
        time.sleep(ping_interval_seconds)

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # def ready(self):
    #     if 'runserver' in sys.argv:
    #         ping_thread = threading.Thread(target=ping_server)
    #         ping_thread.daemon = True
    #         ping_thread.start()

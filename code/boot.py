import keys
import time
import network
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)
    while not wlan.isconnected ():
        print("Waiting for connection...")
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print("\nConnected to Wifi on {}!".format(ip))
    
do_connect()
import network
import time
import sys

wlan = network.WLAN (network.STA_IF)

wlan.active(False)
time.sleep(1)
wlan.active(True)

#ssid = "OPPO F17"
#psk = "testingesp32"

try:
    #wlan.connect(ssid,psk)
    #if wlan.isconnected() == True:
        #print(wlan.ifconfig())
    wlan = network.WLAN (network.STA_IF)

    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    

    networks = wlan.scan()
    print (networks)
except Exception as e:
    print(f"Error > {e}")
    
sys.exit()
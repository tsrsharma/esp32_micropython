import network
import time
import urequests as requests
import sys

# method to connect with Wi-Fi
def connect_wifi(ssid, psk, timeout):
    try:
        # object for wi-fi (station mode)
        
        wlan = network.WLAN(network.STA_IF)
        
        # restart the wlan driver
        
        wlan.active(False)
        time.sleep(1)
        wlan.active(True)
        
        # connect with wi-fi
        
        wlan.connect(ssid, psk)
        t = 0
        print("Connecting...")
        
        # connect with wi-fi with timeout
        
        while wlan.isconnected() == False and timeout-t > 0:
            print("*", end="")
            t += 1
            time.sleep(1)
        if wlan.isconnected() == True:
            print("\nConnection established")
            print("The IP addr of ESP device is: ",wlan.ifconfig()[0])
            return wlan 
        else:
            print("\nCoudnt not connect")
    except Exception as e:
        print(f"Error in wifi connection > {e}")
        sys.exit()


# method to connect with webpage and read data using get method

def read_webpage(wlan):
    try:
        # ensure the wi-fi connection
        
        if wlan.isconnected() == True:
            # get response form the webpage
            
            req = requests.get("https://example.com")
            
            # check the sttaus code
            # for successfull request the status code is 200
            
            print("Request succesfull" if req.status_code == 200 else "Request failed")
            
            # print the result in text format
            
            print(req.text)
            req.close()
        else:
            print("check your wi-fi connection")
    except Exception as e:
        print(f"Error in reading webpage > {e}")
        sys.exit()

if __name__ == "__main__":
    wlan = connect_wifi("hPhone", "testingesp32", 10)
    read_webpage(wlan)
    sys.exit()
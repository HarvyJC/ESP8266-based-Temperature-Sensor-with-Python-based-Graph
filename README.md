# ESP8266-based-Temperature-Sensor-with-Python-based-Graph

***
I used KebabLord's esp2python as a base of my code, both Arduino and Python. 
His work can be found [here](https://github.com/KebabLord/esp2python).
I adjusted his ESP_MICRO.h code to my work, specifically the IP.
Just change both (192, 168, 22, 21) to the IP address you want to use. 
I used 192.168.22.21 so that it doesn't interfere with other devices in my network. 
Be sure that when you adjust the Arduino code, you also adjust the url in the Python code.

````
Arduino (ESP_MICRO.h):
WiFi.config(IPAddress(192, 168, 22, 21), IPAddress(192, 168, 22, 21), IPAddress(255, 255, 255, 0));

Python:
url = "http://192.168.22.22"
````

I suggest you go to his Github to better understand how his code works.

***

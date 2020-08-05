import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
import urllib.request, os, time

url = "http://192.168.22.22"

def get_data():
   global data

   n = urllib.request.urlopen(url).read()
   n = n.decode("utf-8")
   
   data = n

def sensor_run():
    print('Sensor running.')
    print('Temperature data can be seen in the graph title.')

    x = []
    y = []
    z = []

    index = count()

    while True:
        fig = plt.gcf()
        fig.canvas.set_window_title('Temperature Graph')

        global x_sorted

        def animate(i):
            get_data()
            data1 = float(data.replace('\n', ''))

            x.append(next(index))
            y.append(data1)
                
            x_sorted = sorted(y)

            plt.cla()
            plt.plot(x, y)
            plt.title('Low: ' + str(x_sorted[0]) + ' C ' + 
                  '     Current: ' + str(data1) + ' C ' + 
                  '     High: ' + str(x_sorted[len(y) - 1]) + ' C')
            plt.xlabel('Time')
            plt.ylabel('Temperature')

        ani = FuncAnimation(fig, animate)
        plt.show()


def sensor_check():
    try:
        sensor_run()
    except(urllib.error.URLError):
        print('Sensor is either not running or not connected to the network.')
        input('Press any key to exit.')
        exit()

print('Checking sensor...')
sensor_check()
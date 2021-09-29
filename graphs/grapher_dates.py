import matplotlib.pyplot as plt
from iptracker import Thread

Thread.initialize()

threads = []

mon = 0
monAverage = 0
monMedian = []

tue = 0
tueAverage = 0
tueMedian = []

wed = 0
wedAverage = 0
wedMedian = []

thu = 0
thuAverage = 0
thuMedian = [] 

fri = 0
friAverage = 0
friMedian = [] 

sat = 0
satAverage = 0
satMedian = [] 

sun = 0
sunAverage = 0
sunMedian = [] 

for thread in Thread.threads:
    if thread.getDay() == "Mon":
        monAverage += thread.ips
        mon += 1
        monMedian.append(thread.ips) 

    if thread.getDay() == "Tue":
        tueAverage += thread.ips
        tue += 1
        tueMedian.append(thread.ips) 

    if thread.getDay() == "Wed":
        wedAverage += thread.ips
        wed += 1
        wedMedian.append(thread.ips) 

    if thread.getDay() == "Thu":
        thuAverage += thread.ips
        thu += 1
        thuMedian.append(thread.ips) 

    if thread.getDay() == "Fri":
        friAverage += thread.ips
        fri += 1
        friMedian.append(thread.ips) 

    if thread.getDay() == "Sat":
        satAverage += thread.ips
        sat += 1
        satMedian.append(thread.ips) 

    if thread.getDay() == "Sun":
        sunAverage += thread.ips
        sun += 1
        sunMedian.append(thread.ips) 

monAverage = 0 if mon == 0 else monAverage/mon
tueAverage = 0 if tue == 0 else tueAverage/tue
wedAverage = 0 if wed == 0 else wedAverage/wed
thuAverage = 0 if thu == 0 else thuAverage/thu
friAverage = 0 if fri == 0 else friAverage/fri
satAverage = 0 if sat == 0 else satAverage/sat
sunAverage = 0 if sun == 0 else sunAverage/sun

monMedian.sort()
monMedian = monMedian[int(len(monMedian)/2)]  
tueMedian.sort()
tueMedian = tueMedian[int(len(tueMedian)/2)]  
wedMedian.sort()
wedMedian = wedMedian[int(len(wedMedian)/2)]  
thuMedian.sort()
thuMedian = thuMedian[int(len(thuMedian)/2)]  
friMedian.sort()
friMedian = friMedian[int(len(friMedian)/2)]  
satMedian.sort()
satMedian = satMedian[int(len(satMedian)/2)]  
sunMedian.sort()
sunMedian = sunMedian[int(len(sunMedian)/2)]  

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

fig, host = plt.subplots()
sub = host.twinx()

p1 = host.bar(days,
         [mon, tue, wed, thu, fri, sat, sun],
         color='Red',
         label="# of threads")
host.set_xlabel("Day")
host.set_ylabel("# of threads")
host.yaxis.label.set_color("Red")

host.set_ylim(bottom=0)
host.set_yticks(host.get_yticks()[::2])


p2, = sub.plot(days,
         [monAverage, tueAverage, wedAverage, thuAverage, friAverage, satAverage, sunAverage],
         label="Average ips")
sub.set_ylabel("ips")
sub.set_ylim(bottom=0)


p3, = sub.plot(days,
         [monMedian, tueMedian, wedMedian, thuMedian, friMedian, satMedian, sunMedian],
         label="Median ips",
         color="green")

host.tick_params(axis='y', colors="Red")

lns = [p1, p2, p3]
host.legend(handles=lns, loc='best')

host.set_title("Thread data per day")
if __name__ == '__main__':
    plt.show()

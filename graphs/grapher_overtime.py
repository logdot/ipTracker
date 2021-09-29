import matplotlib.pyplot as plt
from iptracker import Thread

Thread.initialize()

ips = Thread.getAllIps()
ids = Thread.getAllIds()
replies = Thread.getAllReplies()
RoI = [i / j for i, j in zip(replies, ips)]

smoothIps = []
for i in range(0, len(ips)):
    bot = 0
    cur = 0
    top = 0

    bot = ips[i-1] if i-1 >= 0 else 0
    cur = ips[i]
    top = ips[i+1] if i+1 < len(ips) else 0

    smoothIps.append((bot + cur + top)/3)

ids = [str(t)[:] for t in ids]

fig, sub2 = plt.subplots()
sub1 = sub2.twinx()
host = sub2.twinx()

sub2.set_facecolor('gray')

sub1.spines.right.set_position(("axes", 1.06))

p1, = host.plot(ids, ips, color="yellow", label="# of ips", zorder=5)
p2, = sub1.plot(ids, replies, color='red', label="# of replies", zorder=10)
p3 = sub2.bar(ids, RoI, color='green', label="Replies/ips", zorder=0)

host.set_xlabel('Post ids')
host.set_ylabel('Ip #')
sub1.set_ylabel('Reply #')
sub2.set_ylabel('Replies/ips')

host.set_ylim(bottom=0)
sub1.set_ylim(bottom=0, top=1550)
sub2.set_ylim(bottom=0, top=30)

host.set_xlim(0, len(ids)-1)

yticks = list(range(0, 1600, 100))
yticks.append(1550)

print(yticks)
host.set_yticks(range(0, 275, 25))
sub1.set_yticks(yticks)

lns = [p1, p2, p3]
host.legend(handles=lns, loc='best')

fig.autofmt_xdate()
host.set_title('Thread data overtime')

plt.subplots_adjust(left=0.038, bottom=0.07, top=0.955)

#sub2.annotate('2hu', xy=(0,10), xytext=(0, 10), xycoords='data', horizontalalignment='left')
#sub2.text(1, 12, "round", ha="center", va="center", rotation=0, size=15,
#        bbox=dict(boxstyle="round,pad=0.3", fc="cyan", ec="b", lw=2))

if __name__ == '__main__':
    plt.show()

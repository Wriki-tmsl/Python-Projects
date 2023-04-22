
from math import radians
import pylab as pl
import numpy as np
def decdeg2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return int(mult*deg)%360, int(mult*mnt)%360, int(mult*sec)%360
n=int(input("Enter Degrees: "))
o=int(input("Enter Minutes: "))
q=int(input("Enter Seconds: "))
s=n+o/60+q/3600
d=s+133+20/60
b=360-d
p=b+180
c=d+180
k=s-30

theta = [radians(s),radians(d),radians(b),radians(p),radians(c),radians(k)]
beta = [decdeg2dms(s),decdeg2dms(d),decdeg2dms(b),decdeg2dms(p),decdeg2dms(c),decdeg2dms(k)]
n=np.ones(6)
ax = pl.subplot(111, polar=True)
ax.scatter(theta,n)
for i, txt in enumerate(beta):
    ax.annotate(txt, (theta[i], n[i]))
pl.show()
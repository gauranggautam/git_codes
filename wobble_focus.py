import numpy as np, matplotlib.pyplot as plt, matplotlib.ticker as mticker
import time, os, AMC
from snAPI.Main import *

# === CONFIG ===
wobble_speed = 0.01         # 
wobble_size = 2          # ± range from current focus
# === AMC Init ===
amc = AMC.Device('amc100num-a01-0248.local')
amc.connect()
for a in [1]: amc.control.setControlOutput(a, True); amc.control.setControlMove(a, True)
f_now = amc.move.getPosition(1) / 1000

wobble_range= np.arange(f_now-wobble_size,f_now+wobble_size+wobble_speed,wobble_speed)
rev_wobble_range= np.arange(f_now+wobble_size,f_now+wobble_size+wobble_speed,wobble_speed)
while True:
    for f in wobble_range:
        amc.move.setControlTargetPosition(1, int(f * 1000))
        time.pause(wobble_speed)
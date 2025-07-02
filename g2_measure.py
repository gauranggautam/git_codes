from snAPI.Main import *
#import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
from datetime import datetime
import time
import pandas as pd
import os
import sys

Detectors=2   # 1. For Exciletas_Ch(1,2) 2. For MPDs_Ch(3,4)

#initialize device
sn = snAPI(libType=LibType.MH)
sn.closeDevice()

sn.getDeviceIDs()
if sn.getDevice(0):
    sn.setLogLevel(LogLevel.Device, False)
    sn.setLogLevel(LogLevel.Api, False)
    print(f'MH Device : ({sn.deviceConfig["ID"]}) detected, initializing...')
    sn.initDevice(MeasMode.T2)
    if Detectors==1:
        a,b=1,2
        sn.loadIniConfig(r'C:\Users\iq-qfl\Documents\Gaurang\Codes\user_configs_snAPI\Exciletas_MH.ini')
    elif Detectors==2:
        a,b=3,4 
        sn.loadIniConfig(r'C:\Users\iq-qfl\Documents\Gaurang\Codes\user_configs_snAPI\MPDs_MH.ini') 
    
    # Get initial count rates

    cnts = sn.getCountRates()
    cntss = cnts[a] + cnts[b]
    sn.device.setOflCompression(0)

    # Measure time in seconds
    mt = 600 #in seconds
    succ=False
    sv=True

    #File saving
    output_dir = r'.\PlotBasic\Output\g2data_m' #Output directory
    dtnow= datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    
    ptuo= f'g2data_{mt:.0f}s_{dtnow}.ptu' #Change output file name cahnge 'g2data'
    g2_filename= os.path.join(output_dir, ptuo)
    sn.setPTUFilePath(g2_filename)
    details_filename = os.path.join(output_dir, f"g2details_{mt:.0f}s_{dtnow}.txt")
    print(f'Filename identifier : {ptuo}, proceeding...')
    #Parameters for g2
    d= binsize = 200           #in ps
    c= windowsize = 100000     #in ps
 
    sn.correlation.setG2Parameters(a, b, c, d)
        
    #Start measurement
    print(f'Starting a measurement for {mt} s, proceeding...')
    sn.correlation.measure(int(mt*1000), savePTU=True)
    start_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #Tracking for g2details
    elapsed_time_list = []
    ch1_counts = []
    ch2_counts = []
    total_counts = []
    timestamps = []
    g2_zero_values = []
    
    start_time=time.time()
    
    #Graphing 
    plt.ion()
    fig, axes = plt.subplots(2, 1, figsize=(10,10))
    
    with open(details_filename, 'w') as file:
        file.write(f"# Measurement Details\n")
        file.write(f"# Channel = {a}, Channel 2 = {b}, Windows Size = {c} ps, Bin Width = {d} ps\n")
        file.write(f"# Measurement Time (mt) = {mt} s\n")
        file.write(f"# Measurement Start Time: {start_timestamp}\n")
        file.write("#\n")
        file.write("# Current Time | Elapsed Time (s) | Channel 1 Counts | Channel 2 Counts | Total Counts | g2(0)\n")

        while True:
            time.sleep(2)
            finished = sn.correlation.isFinished()
            g2, lagtimes = sn.correlation.getG2Data()
            lagtimes_ns=np.array(lagtimes)*1e9
            time.sleep(1)
            g2_zero=np.min(g2)
            #Current count rates
            cnts=sn.getCountRates()
            cntss=cnts[a]+cnts[b]
            elapsed_t=time.time()-start_time
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            #Store data
            timestamps.append(current_time)
            elapsed_time_list.append(elapsed_t)
            ch1_counts.append(cnts[a])
            ch2_counts.append(cnts[b])
            total_counts.append(cntss)
            g2_zero_values.append(g2_zero)
            file.write(f"{current_time},{elapsed_t:.2f},{cnts[a]},{cnts[b]},{cntss},{g2_zero:.2f}\n")
            
            #Clear previous plots
            axes[0].clear()
            axes[1].clear()
            
            #Print information on screen
            #print(f'Total counts : ch1 ({cnts[a]}) + ch2 ({cnts[b]}) = {cntss}')
            c_perecent=(elapsed_t*100)/mt

            #PLotting g2
            time.sleep(1)
            axes[0].plot(lagtimes_ns, g2, label=f'{os.path.basename(g2_filename)}', linewidth=0.5)
            axes[0].set_xlabel('Time delay(ns)')
            axes[0].set_ylabel('g2(t)')
            axes[0].set_title(f'g2(t) Correlation (BinWidth = {d} ps & WindowSize = {int(c/1000):.0f} ns) g2(0)={g2_zero: .1f}')
            axes[0].legend(loc='upper right')
            axes[0].set_ylim(0, None)
            
            #Plotting timetrace
            axes[1].plot(elapsed_time_list, ch1_counts, label="Channel 1", color='b', linewidth=0.5,linestyle='--', marker='o')
            axes[1].plot(elapsed_time_list, ch2_counts, label="Channel 2", color='r', linewidth=0.5, linestyle='--', marker='s')
            axes[1].set_xlabel('Elapsed Time (s)')
            axes[1].set_ylabel('Count Rate')

            if elapsed_t<mt:
                axes[1].set_title(f'Time trace : {c_perecent: .0f}% done (Run-time = {elapsed_t: .0f} / {mt: .0f} s)')
            else: 
                axes[1].set_title(f'Time trace : Completed (Total Run-time = {mt: .0f} s)')
            axes[1].legend(loc='upper right')
            axes[1].set_xlim(0, None)
            axes[1].set_ylim(0, None)
            plt.pause(1) 
            if finished:
                end_time = time.time()
                succ=True
                break
        end_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total_runtime = end_time - start_time        
        #Footer information
        file.write("#\n")
        file.write(f"# Measurement End Time: {end_timestamp}\n")
        file.write(f"# Total Runtime: {total_runtime:.2f} s\n")
        if succ:
            file.write(f"# Completion = {succ} \n")        
        if sv:
            figpath = os.path.join(output_dir, f'g2plot_{mt}s_{dtnow}'+'.png')
            try:
                fig.savefig(figpath)
                print(f"Figure saved as {figpath}")
            except Exception as e:
                print(f"Error saving figure: {e}")
        sn.closeDevice(0)
        plt.ioff()
        plt.show()
else:
    print(f'MH Device not detected, Try closing all devices!')
    sn.closeDevice(0) 
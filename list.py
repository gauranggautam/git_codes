import matplotlib.pyplot as plt
from datetime import datetime

sweeps_filename = ['TG5_SweepX+Vgg_Vg1=0_Vg2=0_Vb=0_20250607-164406',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=10_Vb=0_20250607-213321',
'TG5_SweepX+Vgg_Vg1=10_Vg2=-10_Vb=0_20250607-215416',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_20250607-221330',
'TG5_SweepX+Vgg_Vg1=10_Vg2=10_Vb=0_20250607-223417',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_20250607-221330']
prefix = "C:\Data\Emile/20250606"

plt.figure()
fig, axes = plt.subplot(2,3)
for file in sweeps_filename:
    full_file = f'{prefix}\{file}*' 
    print(full_file)
    m=readfile(full_file)
    
    axes.pcolor(m[0], m[1],m[2])
    axes.colorbar()
    axes.title(file)
    fig.savefig(f'{full_file[:-1]}_.png')


import matplotlib.pyplot as plt
from datetime import datetime

sweeps_filename = ['TG5_SweepX+Vgg_Vg1=0_Vg2=0_Vb=0_20250607-164406',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=10_Vb=0_',
'TG5_SweepX+Vgg_Vg1=10_Vg2=-10_Vb=0_',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_',
'TG5_SweepX+Vgg_Vg1=10_Vg2=10_Vb=0_',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_']
prefix = "C:\Data\Emile/20250606"

for file in sweeps_filename:
    full_file = f'{prefix}\{file}*' 
    print(full_file)
    m=readfile(full_file)
    plt.figure()
    plt.pcolor(m[0], m[1],m[2])
    plt.colorbar()
    plt.title(file)
    plt.savefig(f'{full_file[:-1]}_.png')


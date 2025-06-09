import matplotlib.pyplot as plt
from datetime import datetime




#sweeps_filename = ['TG5_SweepVg2+Y_Vg1=-10_Vgg=0_Vb=0_',
'TG5_SweepVg2+Y_Vg1=10_Vgg=0_Vb=0_',
'TG5_SweepVg1+Y_Vg2=-10_Vgg=0_Vb=0_',
'TG5_SweepVg1+Y_Vg2=10_Vgg=0_Vb=0_',
'TG5_SweepVb+Y_Vg2=-2.5_Vg1=10_Vgg=0_',
'TG5_SweepVb+Y_Vg2=-10_Vg1=10_Vgg=0_',
'TG5_SweepVb+Y_Vg1=-2.5_Vg2=10_Vgg=0_',
'TG5_SweepVb+Y_Vg1=-10_Vg2=10_Vgg=0_']
#prefix = "C:\Data\Emile/20250606"

#sweeps_filename = ['TG5_SweepX+Vgg_Vg1=0_Vg2=0_Vb=0_20250607-164406',
#'TG5_SweepX+Vgg_Vg1=-10_Vg2=10_Vb=0_20250607-213321',
#'TG5_SweepX+Vgg_Vg1=10_Vg2=-10_Vb=0_20250607-215416',
#'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_20250607-221330',
#'TG5_SweepX+Vgg_Vg1=10_Vg2=10_Vb=0_20250607-223417']
#prefix = "C:\Data\Emile/20250606"


fig, axes = plt.subplots(3,2)
i=j=0
for file in sweeps_filename:
    full_file = f'{prefix}\{file}*' 
    print(full_file)
    m=readfile(full_file)
    print((i,j))
    axes[i,j].pcolor(m[0], m[1],m[2])
    #fig.colorbar(ax=axes[i,j])
    axes[i,j].set_title(file)
    

    if j == 1:
        i+=1
        j = 0
    else:
        j+=1
fig.savefig(f'{prefix}/banane_.png')

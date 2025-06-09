import matplotlib.pyplot as plt

sweeps_filename = ['TG5_SweepX+Vgg_Vg1=0_Vg2=0_Vb=0_.txt',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=10_Vb=0_.txt',
'TG5_SweepX+Vgg_Vg1=10_Vg2=-10_Vb=0_.txt',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_.txt',
'TG5_SweepX+Vgg_Vg1=10_Vg2=10_Vb=0_.txt',
'TG5_SweepX+Vgg_Vg1=-10_Vg2=-10_Vb=0_.txt']
prefix = r"C:\Data/Emile/20250606/"

for file in sweeps_filename:
    full_file = f'{prefix}{file}*' 
    m=readfile(full_file)
    plt.pcolor(m[0], m[1],m[2])
    plt.colorbar()
    plt.title()
    figure();pcolor(m[0], m[1],m[2]));colorbar();

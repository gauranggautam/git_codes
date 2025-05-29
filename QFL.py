import os
def plot_spectrum(input, compare=False, fig=55,id='Plot'):
    filename = input
    v=readfile(os.path.join(input_dir, filename),encoding='latin1',multi_sweep='force')
    #Compare mode
    if compare:
        figure(fig)
        ax=plt.gca()
    else:
        fig, ax = plt.subplots()
    spectr=plot(v[1],v[2],label=f'{id}_{os.path.basename(filename)}')
    ax.set_xlim(min(v[1]),max(v[1]))
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Counts (Arb.)')
    ax.grid=True
    if compare:
        ax.set_title(f'PL Spectrum compare')
        ax.legend(loc='upper right')
    else:
        ax.set_title(os.path.basename(filename))
#Ongoing+plot PLmap        
def plot_plmap(input, mode='custom', flog=False, xi=0, yi=2, zi=6):

    filename=input
    v=readfile(filename,encoding='latin1',multi_sweep='force')
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('viridis')
    if mode == 'apd':
        x_index, y_index, z_index = 0, 2, 6
    elif mode == 'spec' :
        x_index, y_index, z_index = 0, 2, 5
    elif mode == 'specw' :
        x_index, y_index, z_index = 0, 2, 8
    else:
        x_index, y_index, z_index = xi,yi,zi

    
    if flog:
        plmap=pcolor(v[x_index],v[y_index],log10(v[z_index]),cmap=cmap)
    else:
        plmap=pcolor(v[x_index],v[y_index],v[z_index],cmap=cmap)
    
    cbar = fig.colorbar(plmap, ax=ax)
    cbar.set_label('Log10 Counts')
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.set_xlabel('X (in um)')
    ax.set_ylabel('Y (in um)')
    ax.set_title(os.path.basename(filename))

#Polarization (not done)
def plot_polarization(input, polar=True, mode='custom', flog=False, xi=0, yi=1):
    filename=input
    v=readfile(filename,encoding='latin1',multi_sweep='force')
    
    if mode == 'apd':
        x_index, y_index= 0, 4
    elif mode == 'spec' :
        x_index, y_index= 0, 5
    elif mode == 'specw' :
        x_index, y_index= 0, 6
    else:
        x_index, y_index= xi,yi
        
    x, y = v[x_index],v[y_index]-min(v[y_index])
    if polar:       
        fig= plt.figure()
        ax=fig.add_subplot(111, polar=True)
        ax.scatter(x, y, label=f'{filename}', color='blue', linewidth= 0.5)
        plt.legend(loc='lower left')
        ax.set_title('Polarization dependance')
    else:
        x, y = np.radians(data[:, x_index]),data[:,y_index]-np.min(data[:,y_index])   
        x, y = data[:, x_index], y       
        fig= plt.figure()
        ax=fig.add_subplot()
        ax.plot(x, y, label=f'{filename}', color='blue')
        ax.set_xlabel('Theta (deg)')
        ax.set_ylabel('Counts (Arb.)')
        ax.set_title('Polarization dependance')
        plt.legend()
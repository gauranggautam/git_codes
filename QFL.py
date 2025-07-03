import os
import matplotlib.pyplot as plt
import numpy as np  # Needed for np.radians and np.min

def plot_spectrum(input, compare=False, fig=11, id='Plot'):
    """
    Plot a PL spectrum from a given data file.

    Parameters:
    - input (str): Path to the input data file.
    - compare (bool): If True, overlays plot on an existing figure.
    - fig (int): Figure number to use when compare is True.
    - id (str): Label identifier for the plot legend.
    """
    filename = input
    v = readfile(os.path.join(input_dir, filename), encoding='latin1', multi_sweep='force')
    if compare:
        figure(fig)
        ax = plt.gca()
    else:
        fig, ax = plt.subplots()
    spectr = plot(v[1], v[2], label=f'{id}_{os.path.basename(filename)}')
    ax.set_xlim(min(v[1]), max(v[1]))
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Counts (Arb.)')
    ax.grid = True
    if compare:
        ax.set_title('PL Spectrum compare')
        ax.legend(loc='upper right')
    else:
        ax.set_title(os.path.basename(filename))


def plot_plmap(input, mode='custom', flog=False, xi=0, yi=2, zi=6, id='Plot'):
    """
    Plot a PL map using pcolor.

    Parameters:
    - input (str): Path to the input data file.
    - mode (str): 'apd', 'spec', 'specw' or 'custom'. Chooses predefined column indices.
    - flog (bool): If True, applies log10 to Z-values.
    - xi, yi, zi (int): Custom column indices for x, y, z.
    - id (str): Identifier used in the plot title.
    """
    filename = input
    v = readfile(filename, encoding='latin1', multi_sweep='force')
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('viridis')

    if mode == 'apd':
        x_index, y_index, z_index = 0, 2, 6
    elif mode == 'spec':
        x_index, y_index, z_index = 0, 2, 5
    elif mode == 'specw':
        x_index, y_index, z_index = 0, 2, 8
    else:
        x_index, y_index, z_index = xi, yi, zi

    if flog:
        plmap = pcolor(v[x_index], v[y_index], np.log10(v[z_index]), cmap=cmap)
    else:
        plmap = pcolor(v[x_index], v[y_index], v[z_index], cmap=cmap)

    cbar = fig.colorbar(plmap, ax=ax)
    cbar.set_label('Log10 Counts' if flog else 'Counts')
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.set_xlabel('X (in um)')

    ax.set_ylabel('Y (in um)')
    ax.set_title(f'{id}_{os.path.basename(filename)}')


def plot_powerd(input, compare=False, fig=66, mode='custom', xi=2, yi=5, id='Plot'):
    """
    Plot power dependence curve.

    Parameters:
    - input (str): Path to the input file.
    - compare (bool): If True, overlays on existing plot.
    - fig (int): Figure number if compare is True.
    - mode (str): 'apd', 'spec', 'specw' or 'custom'.
    - xi, yi (int): Custom column indices.
    - id (str): Identifier for legend label.
    """
    filename = input
    v = readfile(filename, encoding='latin1', multi_sweep='force')

    if mode == 'apd':
        x_index, y_index = 2, 5
    elif mode == 'spec':
        x_index, y_index = 2, 6
    elif mode == 'specw':
        x_index, y_index = 5, 7
    else:
        x_index, y_index = xi, yi

    x, y = v[x_index], v[y_index] - min(v[y_index])

    if compare:
        figure(fig)
        ax = plt.gca()
        ax.plot(x * 1000, y, label=f'{id}_{os.path.basename(filename)}')
        ax.set_title('Power dependence comparison')
        plt.legend(loc='upper left')
    else:
        fig, ax = plt.subplots()
        ax.plot(x * 1000, y)
        ax.set_title(f'Power dependence for {os.path.basename(filename)}')

    ax.set_xlabel('Power (mW)')
    ax.set_ylabel('Counts (a.u.)')
    ax.set_xlim(0, None)
    ax.set_ylim(0, None)

#not done
def plot_polarization(input, polar=True, mode='custom', flog=False, xi=0, yi=1):
    """
    Plot polarization dependence, either in polar or Cartesian coordinates.

    Parameters:
    - input (str): Path to input data file.
    - polar (bool): If True, plots in polar format.
    - mode (str): 'apd', 'spec', 'specw' or 'custom'.
    - flog (bool): Currently unused.
    - xi, yi (int): Custom column indices.
    """
    filename = input
    v = readfile(filename, encoding='latin1', multi_sweep='force')

    if mode == 'apd':
        x_index, y_index = 0, 4
    elif mode == 'spec':
        x_index, y_index = 0, 5
    elif mode == 'specw':
        x_index, y_index = 0, 6
    else:
        x_index, y_index = xi, yi

    x, y = v[x_index], v[y_index] - min(v[y_index])

    if polar:
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.scatter(x, y, label=f'{filename}', color='blue', linewidth=0.5)
        plt.legend(loc='lower left')
        ax.set_title('Polarization dependence')
    else:
        x, y = np.radians(x), y
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.plot(x, y, label=f'{filename}', color='blue')
        ax.set_xlabel('Theta (deg)')
        ax.set_ylabel('Counts (Arb.)')
        ax.set_title('Polarization dependence')
        plt.legend()

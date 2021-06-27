# -*- coding: utf-8 -*-
# author：Kan.Li time:2021-06-26
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import rcParams
import matplotlib.font_manager


def efficiency_calculation(H_SED, re_fixation_efficiency):
    # Calculation of the mass of originally-hosted N in sediments (Mass_N_sed).
    # Parameters used in calculation (See caption of Fig. 10 for reference):
    # average sediment density = 1.64 g/cm3;
    # average sediment porosity = 38.52%;
    # average N concentration of sediments  = 299 ppm N;
    # H_SED: sediment thickness varying from 0 m to 2000 m;
    Mass_N_sed = H_SED * 1.64 * (1 - 0.3852) * 299

    # Calculation of thickness of metamorphosed AOC (H_AOC) required to fix the sedimentary N.
    # Parameters used in calculation (see caption of Fig. 10 for reference):
    # average AOC density = 2.93 g/cm3;
    # average AOC porosity = 12%;
    # average N concentration of subducted AOC = 7 ppm;
    # average N concentration of blueschist obtained in this study = 51 ppm.
    H_AOC = re_fixation_efficiency / 100 * Mass_N_sed / (2.93 * (1 - 0.12) * (51 - 7))

    # print('efficiency', efficiency)
    return H_AOC


def main():
    # set up Times New Roman font
    params = {'font.family': 'serif', 'font.serif': 'Times New Roman', 'font.weight': '400'}
    rcParams.update(params)
    # set up regular font without bold
    del matplotlib.font_manager.weight_dict['roman']
    matplotlib.font_manager._rebuild()

    # initial parameters set up
    x_space = 10
    y_space = 1

    # X-axis represents the sediment thickness incorporated into the melange varying from 0 m to 2000 m.
    x_array = np.arange(0, 2001, x_space)
    print('shape sed', x_array.shape, x_array.shape[0])

    # Y-axis represents the N re-fixation efficiency varying from 0% to 100%.
    y_array = np.arange(0, 101, y_space)
    X, Y = np.meshgrid(x_array, y_array)

    # Vertical bar represents average sediment thickness of subducting slabs of the modern Circumi-Pacific subduction zones
    plt.vlines(794,0,100, alpha=0.4, linewidths=8, colors='grey')
    # Horizontal bar represents the maximum degree of N loss observed in the epidote-blueschist metamorphism
    plt.hlines(40,0,2000, alpha=0.4, linewidths=8, colors='grey')

    # Plotted figure size and dimensions.
    plt.figure(1)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(3.5, 3.5)
    plt.ylim(0, 100)
    plt.xlim(0, 2000)

    # axis major and minor ticks set up
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(500))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_minor_locator(MultipleLocator(100))
    ax.yaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.tick_params(which='major', direction='out', length=5, labelsize=10)
    ax.tick_params(which='minor', direction='out', length=3)
    plt.xlabel('Sediment thickness (m)', fontsize=12)
    plt.ylabel('N re-fixation efficiency (%)', fontsize=12)

    # Plot set up
    C = plt.contour(X, Y, efficiency_calculation(X, Y), [300, 600, 1200, 1800, 2400, 3000, 3600, 4200], colors='black',
                    linewidths=.85, linestyles='dashed')

    manual_locations=[(461,24), (671,33), (927,48), (1137,59), (1318,68), (1471,76), (1622,83), (1762, 89)]
    plt.clabel(C, inline=True, manual=manual_locations, inline_spacing=5, fontsize=8, fmt=r'%dm')
    plt.savefig('fixation-1.pdf', dpi=600, format='pdf', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()









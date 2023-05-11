"""
# plotting.py

Plotting functions for Frequency Response simulation data.
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
from typing import NamedTuple
import matplotlib.pyplot as plt
from collections import namedtuple


BLUE = "#1f77b4"
ORANGE = "#ff7f0e"
GREEN = "#2ca02c"
RED = "#d62728"





def plot_amplitude_linear(data: pd.DataFrame, data_type: str, axis: str, dimm_number: int, markers: bool = False, fill: bool = False, 
        modal_freq: list = None, locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3.) -> plt.Figure:
    """
    Plots amplitude data for a single DIMM.

    ## Parameters
    - `data`: DataFrame containing the data for a single DIMM.
    - `data_type`: Type of data contained in the `data` DataFrame (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data being plotted (e.g. 'x', 'y', 'z')
    - `dimm_number`: Number of the DIMM being plotted (e.g. 1, 2, 3, 4, 5, 6, 7, 8)
    - `markers` (Optional): If `True`, markers will be added to the plot.
    - `fill` (Optional): If `True`, the area under the curve will be filled.
    - `modal_freq` (Optional): If provided, the modal frequencies will be plotted as vertical lines.
    - `locate_peaks` (Optional): If `True`, the peaks will be marked with dotted lines.
    - `locate_modal_freq_with` (Optional): If `markers`, the modal frequencies will be marked
        with markers. If `lines`, the modal frequencies will be marked with vertical lines.
    - `marker_size` (Optional): Size of the markers used to mark data points.
    """
    color = {'x': BLUE, 'y': ORANGE, 'z': GREEN}[axis]
    locate_modal_freq_with = locate_modal_freq_with.lower()
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    min_amplitude = min(data[amplitude_key]) * 0.8
    max_amplitude = max(data[amplitude_key]) * 1.1
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle(f"DIMM {dimm_number} - {data_type.title()} Frequency Response ({axis.title()})", fontweight='bold')
    # ax.set_yscale('log')    # Not needed, this is linear
    ax.plot(data['Frequency'], data[amplitude_key], color=color)
    if markers:
        # color = ax.get_lines()[0].get_color()
        ax.plot(data['Frequency'], data[amplitude_key], 'o', color=color, markersize=marker_size, markerfacecolor=color, markeredgewidth=0.5, markeredgecolor=color)
    ax.set_ylim(min_amplitude, max_amplitude)
    ax.set_xlim(min(data['Frequency']), max(data['Frequency']))
    if locate_peaks:
        max_amplitude_index = data[amplitude_key].idxmax()
        max_amplitude_frequency = data['Frequency'][max_amplitude_index]
        max_amplitude_value = data[amplitude_key][max_amplitude_index]
        ax.hlines(max_amplitude_value, min(data['Frequency']), max_amplitude_frequency, linestyles='dotted', colors='black', linewidth=1.5)
    if fill:
        # color = ax.get_lines()[0].get_color()
        ax.fill_between(data['Frequency'], data[amplitude_key], color=color, alpha=0.1)
    if modal_freq is not None:
        for freq in modal_freq:
            if locate_modal_freq_with == 'lines':
                ax.axvline(freq, color='black', linestyle='dotted', linewidth=1.3)
            if not markers and locate_modal_freq_with == 'markers':
                closest_index = (np.abs(data['Frequency'] - freq)).idxmin()
                closest_amplitude = data[amplitude_key][closest_index]
                ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=color)
    ax.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    ax.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    return fig    # This can be shown on the Streamlit app using st.pyplot(fig) instead of plt.show()





def plot_amplitude_xyz_linear(
        data: pd.DataFrame, data_type: str, dimm_number: int, markers: bool = False, fill: bool = False, modal_freq: list = None, 
        locate_modal_freq_with: str = 'markers', marker_size: float = 3.) -> None:
    """
    Plots amplitudes for a single DIMM, but for all three axes (x, y, z).

    ## Parameters
    - `data`: NamedTuple containing data for all 8 DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `modal_freq` (Optional): If provided, the plot will show the modal frequencies as vertical lines.
    - `locate_modal_freq_with` (Optional): If provided, the modal frequencies will be marked with the given method.
    - `marker_size` (Optional): Size of the markers used to mark the modal frequencies.
    """
    locate_modal_freq_with = locate_modal_freq_with.lower()
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    
    data_x = data.x[dimm_number-1]  # DataFrame
    data_y = data.y[dimm_number-1]  # DataFrame
    data_z = data.z[dimm_number-1]  # DataFrame

    min_amplitude = min(min(data_x[amplitude_key]), min(data_y[amplitude_key]), min(data_z[amplitude_key])) * 0.8
    max_amplitude = max(max(data_x[amplitude_key]), max(data_y[amplitude_key]), max(data_z[amplitude_key])) * 1.1

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle(f"DIMM {dimm_number} - {data_type.title()} Frequency Response (X,Y,Z)", fontweight='bold')

    ax.plot(data_x['Frequency'], data_x[amplitude_key], label='X', color=BLUE, alpha=0.8)
    ax.plot(data_y['Frequency'], data_y[amplitude_key], label='Y', color=ORANGE, alpha=0.8)
    ax.plot(data_z['Frequency'], data_z[amplitude_key], label='Z', color=GREEN, alpha=0.8)

    if markers:
        ax.plot(data_x['Frequency'], data_x[amplitude_key], 'o', color=BLUE, markersize=marker_size, markerfacecolor=BLUE, markeredgewidth=0.5, markeredgecolor=BLUE)
        ax.plot(data_y['Frequency'], data_y[amplitude_key], 'o', color=ORANGE, markersize=marker_size, markerfacecolor=ORANGE, markeredgewidth=0.5, markeredgecolor=ORANGE)
        ax.plot(data_z['Frequency'], data_z[amplitude_key], 'o', color=GREEN, markersize=marker_size, markerfacecolor=GREEN, markeredgewidth=0.5, markeredgecolor=GREEN)

    ax.set_ylim(min_amplitude, max_amplitude)
    ax.set_xlim(min(data_x['Frequency']), max(data_x['Frequency']))

    if modal_freq is not None:
        for freq in modal_freq:
            if locate_modal_freq_with == 'lines':
                ax.axvline(freq, color='black', linestyle='dotted', linewidth=1.3)
            if not markers and locate_modal_freq_with == 'markers':
                closest_index = (np.abs(data_x['Frequency'] - freq)).idxmin()
                closest_amplitude = data_x[amplitude_key][closest_index]
                ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=BLUE)
                closest_index = (np.abs(data_y['Frequency'] - freq)).idxmin()
                closest_amplitude = data_y[amplitude_key][closest_index]
                ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=ORANGE)
                closest_index = (np.abs(data_z['Frequency'] - freq)).idxmin()
                closest_amplitude = data_z[amplitude_key][closest_index]
                ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=GREEN)

    ax.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    ax.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    return fig








def subplot_amplitudes(
        data: NamedTuple, data_type: str, axis: str, markers: bool = False, fill: bool = False, save_as: str = None, modal_freq: list = None, 
        locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3., dpi: int = 600, show: bool = False) -> None:
    """
    Plots amplitude data for all DIMMs. (4x2 subplots).

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data being plotted (e.g. 'x', 'y', 'z')
    - `markers` (Optional): If `True`, markers will be added to the plot.
    - `fill` (Optional): If `True`, the area under the curve will be filled.
    - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
    - `modal_freq` (Optional): If provided, the modal frequencies will be plotted as vertical lines.
    - `locate_peaks` (Optional): If `True`, the peaks will be marked with dotted lines.
    - `locate_modal_freq_with` (Optional): If `markers`, the modal frequencies will be marked with markers. If `lines`, the modal frequencies will be marked with vertical lines.
    - `marker_size` (Optional): Size of the markers used to mark data points.
    - `dpi` (Optional): DPI of the saved image. Only applies if `save_as` is given.
    - `show` (Optional): If True, the plot will be shown. Only applies if `save_as` is given, otherwise the plot will always be shown.
    """
    color = {'x': BLUE, 'y': ORANGE, 'z': GREEN}[axis]
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    df1, df2, df3, df4, df5, df6, df7, df8 = data
    min_amplitude = min(min(df1[amplitude_key]), min(df2[amplitude_key]), min(df3[amplitude_key]), min(df4[amplitude_key]), min(df5[amplitude_key]), min(df6[amplitude_key]), min(df7[amplitude_key]), min(df8[amplitude_key])) * 0.8
    max_amplitude = max(max(df1[amplitude_key]), max(df2[amplitude_key]), max(df3[amplitude_key]), max(df4[amplitude_key]), max(df5[amplitude_key]), max(df6[amplitude_key]), max(df7[amplitude_key]), max(df8[amplitude_key])) * 1.1
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
    fig.suptitle(f"{data_type.title()} Frequency Response ({axis.title()})", fontweight='bold')
    fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1, df2, df3, df4, df5, df6, df7, df8]):
        ax.set_yscale('log')
        ax.plot(df['Frequency'], df[amplitude_key], color=color)
        if markers:
            # color = ax.get_lines()[0].get_color()
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=color, markersize=marker_size, markerfacecolor=color, markeredgewidth=0.5, markeredgecolor=color)
        ax.set_ylim(min_amplitude, max_amplitude)
        ax.set_xlim(min(df['Frequency']), max(df['Frequency']))
        if locate_peaks:
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.hlines(max_amplitude_value, min(df['Frequency']), max_amplitude_frequency, linestyles='dotted', colors='black', linewidth=0.5)
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.vlines(max_amplitude_frequency, min_amplitude, max_amplitude_value, linestyles='dotted', colors='black', linewidth=0.5)
        if fill:
            # color = ax.get_lines()[0].get_color()
            ax.fill_between(df['Frequency'], df[amplitude_key], color=color, alpha=0.1)
        if modal_freq is not None:
            for freq in modal_freq:
                if locate_modal_freq_with == 'lines':
                    ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=color)
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        ax.set_title(f"DIMM{i+1}", fontsize=10)
    ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    return fig





def subplot_amplitudes_linear(
        data: NamedTuple, data_type: str, axis: str, markers: bool = False, fill: bool = False, modal_freq: list = None, 
        locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3.) -> None:
    """
    Plots amplitude data for all DIMMs. (4x2 subplots).

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data being plotted (e.g. 'x', 'y', 'z')
    - `markers` (Optional): If `True`, markers will be added to the plot.
    - `fill` (Optional): If `True`, the area under the curve will be filled.
    - `modal_freq` (Optional): If provided, the modal frequencies will be plotted as vertical lines.
    - `locate_peaks` (Optional): If `True`, the peaks will be marked with dotted lines.
    - `locate_modal_freq_with` (Optional): If `markers`, the modal frequencies will be marked with markers. If `lines`, the modal frequencies will be marked with vertical lines.
    - `marker_size` (Optional): Size of the markers.
    """
    locate_modal_freq_with = locate_modal_freq_with.lower()
    color = {'x': BLUE, 'y': ORANGE, 'z': GREEN}[axis]
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    df1, df2, df3, df4, df5, df6, df7, df8 = data
    min_amplitude = 0
    max_amplitude = max(max(df1[amplitude_key]), max(df2[amplitude_key]), max(df3[amplitude_key]), max(df4[amplitude_key]), max(df5[amplitude_key]), max(df6[amplitude_key]), max(df7[amplitude_key]), max(df8[amplitude_key])) * 1.1
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
    fig.suptitle(f"{data_type.title()} Frequency Response ({axis.title()})", fontweight='bold')
    fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1, df2, df3, df4, df5, df6, df7, df8]):
        ax.plot(df['Frequency'], df[amplitude_key], color=color)
        if markers:
            # color = ax.get_lines()[0].get_color()
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=color, markersize=marker_size, markerfacecolor=color, markeredgewidth=0.5, markeredgecolor=color)
        ax.set_ylim(min_amplitude, max_amplitude)
        ax.set_xlim(min(df['Frequency']), max(df['Frequency']))
        if locate_peaks:
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.hlines(max_amplitude_value, min(df['Frequency']), max_amplitude_frequency, linestyles='dotted', colors='black', linewidth=0.5)
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.vlines(max_amplitude_frequency, min_amplitude, max_amplitude_value, linestyles='dotted', colors='black', linewidth=0.5)
        if fill:
            # color = ax.get_lines()[0].get_color()
            ax.fill_between(df['Frequency'], df[amplitude_key], color=color, alpha=0.15)
        if modal_freq is not None:
            # ax.text(0.5, 0.5, str(modal_freq), transform=ax.transAxes)
            for freq in modal_freq:
                if locate_modal_freq_with == 'lines':
                    ax.axvline(freq, color='black', linestyle='dotted', linewidth=1.3)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=color)
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        ax.set_title(f"DIMM{i+1}", fontsize=10)
    ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    # amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'm/s²'}[data_type]
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    return fig    # This can be shown on the Streamlit app using st.pyplot(fig) instead of plt.show()






def subplot_amplitudes_linear_with_phaseangle(
        data: NamedTuple, data_type: str, axis: str, markers: bool = False, fill: bool = False, save_as: str = None, 
        modal_freq: list = None, locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3.) -> None:
    """
    Plots amplitude data for all DIMMs. (4x2 subplots), and their phase shift on a second y-axis.

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data being plotted (e.g. 'x', 'y', 'z')
    - `markers` (Optional): If `True`, markers will be added to the plot.
    - `fill` (Optional): If `True`, the area under the curve will be filled.
    - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
    - `modal_freq` (Optional): If provided, the modal frequencies will be plotted as vertical lines.
    - `locate_peaks` (Optional): If `True`, the peaks will be marked with dotted lines.
    - `locate_modal_freq_with` (Optional): If `markers`, the modal frequencies will be marked with markers. If `lines`, the modal frequencies will be marked with vertical lines.
    - `marker_size` (Optional): Size of the markers.
    """
    # fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(2, 4, figsize=(18, 9), sharex=True, sharey=True)
    color = {'x': BLUE, 'y': ORANGE, 'z': GREEN}[axis]
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    phaseshift_key = "Phase Angle"
    df1, df2, df3, df4, df5, df6, df7, df8 = data
    min_amplitude = 0
    max_amplitude = max(max(df1[amplitude_key]), max(df2[amplitude_key]), max(df3[amplitude_key]), max(df4[amplitude_key]), max(df5[amplitude_key]), max(df6[amplitude_key]), max(df7[amplitude_key]), max(df8[amplitude_key])) * 1.1
    min_phaseshift = -180
    max_phaseshift = 180
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
    fig.suptitle(f"{data_type.title()} Frequency Response ({axis.title()})", fontweight='bold')
    fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1, df2, df3, df4, df5, df6, df7, df8]):
        # plot amplitude on left y-axis
        ax.plot(df['Frequency'], df[amplitude_key], color=color, linewidth=1.5)
        # plot phase shift on right y-axis
        ax2 = ax.twinx()
        max_phaseshift_value = max(df[phaseshift_key])
        max_phaseshift_scaled = max_phaseshift_value / 5
        ax2.plot(df['Frequency'], df[phaseshift_key].apply(lambda x: x/5 + 175-max_phaseshift_scaled), color=RED, linewidth=1, alpha=0.75)
        ax2.set_ylim(min_phaseshift, max_phaseshift)
        # ax2.set_ylabel(f'Phase Shift  ( $°$ )', fontsize=11, labelpad=10, fontweight='bold', color=RED)
        # set the ticks for the right y-axis to be only 0 and 180
        ax2.set_yticks([-180, 180])
        # disable the tick labels
        ax2.set_yticklabels([])
        ax2.set_xlim(min(df['Frequency']), max(df['Frequency']))

        if markers:
            # color = ax.get_lines()[0].get_color()
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=color, markersize=marker_size, markerfacecolor=color, markeredgewidth=0.5, markeredgecolor=color)
        ax.set_ylim(min_amplitude, max_amplitude)
        ax.set_xlim(min(df['Frequency']), max(df['Frequency']))
        if locate_peaks:
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.hlines(max_amplitude_value, min(df['Frequency']), max_amplitude_frequency, linestyles='dotted', colors='black', linewidth=0.5)
            max_amplitude_index = df[amplitude_key].idxmax()
            max_amplitude_frequency = df['Frequency'][max_amplitude_index]
            max_amplitude_value = df[amplitude_key][max_amplitude_index]
            ax.vlines(max_amplitude_frequency, min_amplitude, max_amplitude_value, linestyles='dotted', colors='black', linewidth=0.5)
        if fill:
            # color = ax.get_lines()[0].get_color()
            ax.fill_between(df['Frequency'], df[amplitude_key], color=color, alpha=0.05)
        if modal_freq is not None:
            for freq in modal_freq:
                if locate_modal_freq_with == 'lines':
                    ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=color)
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        ax.set_title(f"DIMM{i+1}", fontsize=10)
    ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    # amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'm/s²'}[data_type]
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    if save_as is not None:
        if '.png' not in save_as:
            save_as = save_as + '.png'
        plt.savefig(save_as, dpi=900)
    plt.show()
    plt.close()
    






def subplot_amplitudes_xyz(
        data: NamedTuple, data_type: str, markers: bool = False, fill: bool = False, save_as: str = None, modal_freq: list = None, 
        locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3., dpi: int = 600, show: bool = False) -> None:
    """
    Plots amplitude data for all DIMMs. (4x2 subplots).

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
    - `modal_freq` (Optional): If provided, the plot will show vertical lines at the given frequencies.
    - `locate_peaks` (Optional): If `True`, the plot will show horizontal and vertical lines at the location of the peak amplitude.
    - `locate_modal_freq_with` (Optional): If `modal_freq` is provided, this parameter determines how the modal frequencies will be located. If 'markers', the modal frequencies will be located with markers. If 'lines', the modal frequencies will be located with lines.
    - `marker_size` (Optional): Size of the markers used to locate the modal frequencies.
    - `dpi` (Optional): DPI of the saved image. Only applies if `save_as` is given.
    - `show` (Optional): If True, the plot will be shown. Only applies if `save_as` is given, otherwise the plot will always be shown.
    """
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x = data.x
    df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y = data.y
    df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z = data.z
    min_amplitude = min(
        min(df1x[amplitude_key]), min(df2x[amplitude_key]), min(df3x[amplitude_key]), min(df4x[amplitude_key]), min(df5x[amplitude_key]), min(df6x[amplitude_key]), min(df7x[amplitude_key]), min(df8x[amplitude_key]),
        min(df1y[amplitude_key]), min(df2y[amplitude_key]), min(df3y[amplitude_key]), min(df4y[amplitude_key]), min(df5y[amplitude_key]), min(df6y[amplitude_key]), min(df7y[amplitude_key]), min(df8y[amplitude_key]),
        min(df1z[amplitude_key]), min(df2z[amplitude_key]), min(df3z[amplitude_key]), min(df4z[amplitude_key]), min(df5z[amplitude_key]), min(df6z[amplitude_key]), min(df7z[amplitude_key]), min(df8z[amplitude_key]),
    ) * 0.8
    max_amplitude = max(
        max(df1x[amplitude_key]), max(df2x[amplitude_key]), max(df3x[amplitude_key]), max(df4x[amplitude_key]), max(df5x[amplitude_key]), max(df6x[amplitude_key]), max(df7x[amplitude_key]), max(df8x[amplitude_key]),
        max(df1y[amplitude_key]), max(df2y[amplitude_key]), max(df3y[amplitude_key]), max(df4y[amplitude_key]), max(df5y[amplitude_key]), max(df6y[amplitude_key]), max(df7y[amplitude_key]), max(df8y[amplitude_key]),
        max(df1z[amplitude_key]), max(df2z[amplitude_key]), max(df3z[amplitude_key]), max(df4z[amplitude_key]), max(df5z[amplitude_key]), max(df6z[amplitude_key]), max(df7z[amplitude_key]), max(df8z[amplitude_key]),
    ) * 1.2
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
    fig.suptitle(f"{data_type.title()} Frequency Response", fontweight='bold')
    fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x]):
        ax.set_yscale('log')
        ax.plot(df['Frequency'], df[amplitude_key], label='X', color=BLUE, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=BLUE, markersize=marker_size, markerfacecolor=BLUE, markeredgewidth=0.5, markeredgecolor=BLUE)
        if modal_freq is not None:
            for freq in modal_freq:
                if locate_modal_freq_with == 'lines':
                    ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=BLUE)
        ax.set_xlim(min(df['Frequency']), max(df['Frequency']))
        ax.set_ylim(min_amplitude, max_amplitude)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y]):
        ax.plot(df['Frequency'], df[amplitude_key], label='Y', color=ORANGE, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=ORANGE, markersize=marker_size, markerfacecolor=ORANGE, markeredgewidth=0.5, markeredgecolor=ORANGE)
        if modal_freq is not None:
            for freq in modal_freq:
                # if locate_modal_freq_with == 'lines':
                #     ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=ORANGE)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z]):
        ax.plot(df['Frequency'], df[amplitude_key], label='Z', color=GREEN, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=GREEN, markersize=marker_size, markerfacecolor=GREEN, markeredgewidth=0.5, markeredgecolor=GREEN)
        if modal_freq is not None:
            for freq in modal_freq:
                # if locate_modal_freq_with == 'lines':
                #     ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=GREEN)
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        ax.set_title(f"DIMM{i+1}", fontsize=10)
    ax1.legend(loc='best', fontsize=10)
    ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    if save_as is not None:
        if '.png' not in save_as:
            save_as = save_as + '.png'
        plt.savefig(save_as, dpi=dpi)
    else:
        show = True
    if show:
        plt.show()
    plt.close()





def subplot_amplitudes_xyz_linear(
        data: NamedTuple, data_type: str, markers: bool = False, fill: bool = False, modal_freq: list = None, 
        locate_peaks: bool = False, locate_modal_freq_with: str = 'markers', marker_size: float = 3.) -> None:
    """
    Plots amplitude data for all DIMMs. (4x2 subplots).

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `modal_freq` (Optional): If provided, the plot will show the modal frequencies as vertical lines.
    - `locate_peaks` (Optional): If True, the plot will show the peaks of the amplitude data as vertical lines.
    - `locate_modal_freq_with` (Optional): If provided, the modal frequencies will be marked with the given method.
    - `marker_size` (Optional): Size of the markers used to mark the modal frequencies.
    """
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x = data.x
    df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y = data.y
    df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z = data.z
    min_amplitude = min(
        min(df1x[amplitude_key]), min(df2x[amplitude_key]), min(df3x[amplitude_key]), min(df4x[amplitude_key]), min(df5x[amplitude_key]), min(df6x[amplitude_key]), min(df7x[amplitude_key]), min(df8x[amplitude_key]),
        min(df1y[amplitude_key]), min(df2y[amplitude_key]), min(df3y[amplitude_key]), min(df4y[amplitude_key]), min(df5y[amplitude_key]), min(df6y[amplitude_key]), min(df7y[amplitude_key]), min(df8y[amplitude_key]),
        min(df1z[amplitude_key]), min(df2z[amplitude_key]), min(df3z[amplitude_key]), min(df4z[amplitude_key]), min(df5z[amplitude_key]), min(df6z[amplitude_key]), min(df7z[amplitude_key]), min(df8z[amplitude_key]),
    ) * 0.8
    max_amplitude = max(
        max(df1x[amplitude_key]), max(df2x[amplitude_key]), max(df3x[amplitude_key]), max(df4x[amplitude_key]), max(df5x[amplitude_key]), max(df6x[amplitude_key]), max(df7x[amplitude_key]), max(df8x[amplitude_key]),
        max(df1y[amplitude_key]), max(df2y[amplitude_key]), max(df3y[amplitude_key]), max(df4y[amplitude_key]), max(df5y[amplitude_key]), max(df6y[amplitude_key]), max(df7y[amplitude_key]), max(df8y[amplitude_key]),
        max(df1z[amplitude_key]), max(df2z[amplitude_key]), max(df3z[amplitude_key]), max(df4z[amplitude_key]), max(df5z[amplitude_key]), max(df6z[amplitude_key]), max(df7z[amplitude_key]), max(df8z[amplitude_key]),
    ) * 1.2
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
    fig.suptitle(f"{data_type.title()} Frequency Response", fontweight='bold')
    fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x]):
        ax.plot(df['Frequency'], df[amplitude_key], label='X', color=BLUE, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=BLUE, markersize=marker_size, markerfacecolor=BLUE, markeredgewidth=0.5, markeredgecolor=BLUE)
        if modal_freq is not None:
            for freq in modal_freq:
                if locate_modal_freq_with == 'lines':
                    ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=BLUE)
        ax.set_xlim(min(df['Frequency']), max(df['Frequency']))
        ax.set_ylim(min_amplitude, max_amplitude)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y]):
        ax.plot(df['Frequency'], df[amplitude_key], label='Y', color=ORANGE, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=ORANGE, markersize=marker_size, markerfacecolor=ORANGE, markeredgewidth=0.5, markeredgecolor=ORANGE)
        if modal_freq is not None:
            for freq in modal_freq:
                # if locate_modal_freq_with == 'lines':
                #     ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=ORANGE)
    for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z]):
        ax.plot(df['Frequency'], df[amplitude_key], label='Z', color=GREEN, alpha=0.8)
        if markers:
            ax.plot(df['Frequency'], df[amplitude_key], 'o', color=GREEN, markersize=marker_size, markerfacecolor=GREEN, markeredgewidth=0.5, markeredgecolor=GREEN)
        if modal_freq is not None:
            for freq in modal_freq:
                # if locate_modal_freq_with == 'lines':
                #     ax.axvline(freq, color='black', linestyle='dotted', linewidth=0.5)
                if not markers and locate_modal_freq_with == 'markers':
                    closest_index = (np.abs(df['Frequency'] - freq)).idxmin()
                    closest_amplitude = df[amplitude_key][closest_index]
                    ax.plot(freq, closest_amplitude, 'o', color='black', markersize=5, markerfacecolor=(1,1,1,0), markeredgewidth=1, markeredgecolor=GREEN)
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
        ax.set_title(f"DIMM{i+1}", fontsize=10)
    ax1.legend(loc='best', fontsize=10)
    ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
    return fig






# def subplot_amplitudes_xyz(data: NamedTuple, data_type: str, save_as: str = None) -> None:
#     """
#     Plots amplitude data for all DIMMs. (4x2 subplots).

#     ## Parameters
#     - `data`: NamedTuple containing data for all eight DIMMs.
#     - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
#     - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
#     """
#     df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x = data.x
#     df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y = data.y
#     df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z = data.z
#     min_amplitude = min(
#         min(df1x['Amplitude']), min(df2x['Amplitude']), min(df3x['Amplitude']), min(df4x['Amplitude']), min(df5x['Amplitude']), min(df6x['Amplitude']), min(df7x['Amplitude']), min(df8x['Amplitude']),
#         min(df1y['Amplitude']), min(df2y['Amplitude']), min(df3y['Amplitude']), min(df4y['Amplitude']), min(df5y['Amplitude']), min(df6y['Amplitude']), min(df7y['Amplitude']), min(df8y['Amplitude']),
#         min(df1z['Amplitude']), min(df2z['Amplitude']), min(df3z['Amplitude']), min(df4z['Amplitude']), min(df5z['Amplitude']), min(df6z['Amplitude']), min(df7z['Amplitude']), min(df8z['Amplitude']),
#     ) * 0.8
#     max_amplitude = max(
#         max(df1x['Amplitude']), max(df2x['Amplitude']), max(df3x['Amplitude']), max(df4x['Amplitude']), max(df5x['Amplitude']), max(df6x['Amplitude']), max(df7x['Amplitude']), max(df8x['Amplitude']),
#         max(df1y['Amplitude']), max(df2y['Amplitude']), max(df3y['Amplitude']), max(df4y['Amplitude']), max(df5y['Amplitude']), max(df6y['Amplitude']), max(df7y['Amplitude']), max(df8y['Amplitude']),
#         max(df1z['Amplitude']), max(df2z['Amplitude']), max(df3z['Amplitude']), max(df4z['Amplitude']), max(df5z['Amplitude']), max(df6z['Amplitude']), max(df7z['Amplitude']), max(df8z['Amplitude']),
#     ) * 1.2
#     fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(18, 9))
#     fig.suptitle(f"{data_type.title()} Frequency Response", fontweight='bold')
#     fig.subplots_adjust(hspace=0.185, wspace=0.155, top=0.910, bottom=0.090, left=0.055, right=0.980)
#     for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x]):
#         ax.set_yscale('log')
#         ax.plot(df['Frequency'], df['Amplitude'], label='X', alpha=0.8)
#         ax.set_ylim(min_amplitude, max_amplitude)
#     for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y]):
#         ax.plot(df['Frequency'], df['Amplitude'], label='Y', alpha=0.8)
#     for ax, df in zip([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8], [df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z]):
#         ax.plot(df['Frequency'], df['Amplitude'], label='Z', alpha=0.8)
#     for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]):
#         ax.set_title(f"DIMM{i+1}", fontsize=10)
#     ax1.legend(loc='lower right', fontsize=10)
#     ax5.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
#     ax6.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
#     ax7.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
#     ax8.set_xlabel('Frequency  ( $Hz$ )', fontsize=11, labelpad=15, fontweight='bold')
#     amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
#     ax1.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
#     ax5.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=11, labelpad=10, fontweight='bold')
#     if save_as is not None:
#         if '.png' not in save_as:
#             save_as = save_as + '.png'
#         plt.savefig(save_as, dpi=900)
#     plt.show()
#     plt.close()





def plot_peak_amplitudes(data: NamedTuple, data_type: str, axis: str) -> None:
    """
    Plots a bar chart with the peak amplitudes of each DIMM.

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data contained in the `data` NamedTuple (e.g. 'x', 'y', 'z')
    """
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(top=0.890, bottom=0.130, left=0.115, right=0.930)
    df1, df2, df3, df4, df5, df6, df7, df8 = data
    ax.bar(
        [1, 2, 3, 4, 5, 6, 7, 8], 
        [max(df1[amplitude_key]), max(df2[amplitude_key]), max(df3[amplitude_key]), max(df4[amplitude_key]), max(df5[amplitude_key]), max(df6[amplitude_key]), max(df7[amplitude_key]), max(df8[amplitude_key])],
        edgecolor='black', linewidth=1, alpha=0.75,
        )
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
    tick_labels = []
    total_max_amplitude = max(
        max(df1[amplitude_key]), max(df2[amplitude_key]), max(df3[amplitude_key]), max(df4[amplitude_key]), max(df5[amplitude_key]), max(df6[amplitude_key]), max(df7[amplitude_key]), max(df8[amplitude_key]),
    )
    for i, df in enumerate([df1, df2, df3, df4, df5, df6, df7, df8]):
        tick_labels.append(f"DIMM{i+1}\n({df['Frequency'][df[amplitude_key].idxmax()]} $Hz$)")
        ax.text(    # Add the peak amplitude as text above the bar.
            i+1, 
            max(df[amplitude_key]) + (total_max_amplitude * 0.01),
            # f"{round(max(df[amplitude_key]),7)}", 
            f"{max(df[amplitude_key]):.5f}", 
            ha='center', 
            va='bottom', 
            fontsize=9, 
            fontstyle='italic'
        )
    ax.set_xticklabels(tick_labels, fontsize=10)
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=12, labelpad=15, fontweight='bold')
    ax.set_xlabel('DIMM Number', fontsize=12, labelpad=20, fontweight='bold')
    ax.set_title(f'{data_type.title()} Frequency Response - Peak Amplitudes ({axis.title()})', fontsize=14, pad=20, fontweight='bold')
    return fig





def plot_peak_amplitudes_xyz(data: NamedTuple, data_type: str, save_as: str = None, dpi: int = 600, show: bool = False) -> None:
    """
    Plots a bar chart with the peak amplitudes of each DIMM.

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data contained in the `data` NamedTuple (e.g. 'x', 'y', 'z')
    - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
    - `dpi` (Optional): DPI of the saved image. Only applies if `save_as` is given.
    - `show` (Optional): If True, the plot will be shown. Only applies if `save_as` is given, otherwise the plot will always be shown.
    """
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(top=0.890, bottom=0.130, left=0.115, right=0.930)
    df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x = data.x
    df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y = data.y
    df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z = data.z
    x_amplitudes = [max(df1x[amplitude_key]), max(df2x[amplitude_key]), max(df3x[amplitude_key]), max(df4x[amplitude_key]), max(df5x[amplitude_key]), max(df6x[amplitude_key]), max(df7x[amplitude_key]), max(df8x[amplitude_key])]
    y_amplitudes = [max(df1y[amplitude_key]), max(df2y[amplitude_key]), max(df3y[amplitude_key]), max(df4y[amplitude_key]), max(df5y[amplitude_key]), max(df6y[amplitude_key]), max(df7y[amplitude_key]), max(df8y[amplitude_key])]
    z_amplitudes = [max(df1z[amplitude_key]), max(df2z[amplitude_key]), max(df3z[amplitude_key]), max(df4z[amplitude_key]), max(df5z[amplitude_key]), max(df6z[amplitude_key]), max(df7z[amplitude_key]), max(df8z[amplitude_key])]
    sorted_indices = np.argsort(x_amplitudes)[::-1]
    x_amplitudes = np.array(x_amplitudes)[sorted_indices]
    y_amplitudes = np.array(y_amplitudes)[sorted_indices]
    z_amplitudes = np.array(z_amplitudes)[sorted_indices]
    dimm_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])[sorted_indices]
    sum_amplitudes = [sum(x) for x in zip(x_amplitudes, y_amplitudes, z_amplitudes)]    # This is
    # sum_bars = ax.bar(
    #     dimm_numbers,
    #     sum_amplitudes,
    #     # make the color completely transparent but keep the edgecolor
    #     color=[(0.95, 0.95, 0.95, 0)],
    #     # bottom=x_amplitudes + y_amplitudes + z_amplitudes,
    #     edgecolor='black', linewidth=2, alpha=0.75,
    # )
    x_bars = ax.bar(
        dimm_numbers,
        x_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    y_bars = ax.bar(
        dimm_numbers,
        y_amplitudes,
        bottom=x_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    z_bars = ax.bar(
        dimm_numbers,
        z_amplitudes,
        bottom=x_amplitudes + y_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
    tick_labels = []
    total_max_amplitude = max(
        max(x_amplitudes), max(y_amplitudes), max(z_amplitudes),
    )
    dfs = {
        'x': [df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x],
        'y': [df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y],
        'z': [df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z],
    }
    for i, df in enumerate([df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z]):
        tick_labels.append(f"DIMM{i+1}")
        ax.text(
            i+1, 
            max(dfs['z'][i][amplitude_key]) + max(dfs['y'][i][amplitude_key]) + max(dfs['x'][i][amplitude_key]) + ( (max(z_amplitudes)) * 0.002),
            # f"{round(max(df[amplitude_key]),7)}", 
            # f"{max(df[amplitude_key]):.5f}", 
            f"{sum([max(dfs['z'][i][amplitude_key]), max(dfs['y'][i][amplitude_key]), max(dfs['x'][i][amplitude_key])]):.5f}",
            ha='center', 
            va='bottom', 
            fontsize=9, 
            fontstyle='italic'
        )

    ax.legend(
        [x_bars, y_bars, z_bars], 
        ['X', 'Y', 'Z'], 
        fontsize=10, 
        loc='upper right', 
        framealpha=0.8,
    )
    ax.set_xticklabels(tick_labels, fontsize=10)
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=12, labelpad=15, fontweight='bold')
    ax.set_xlabel('DIMM Number', fontsize=12, labelpad=20, fontweight='bold')
    ax.set_title(f'{data_type.title()} Frequency Response - Peak Amplitudes (XYZ)', fontsize=14, pad=20, fontweight='bold')
    if save_as is not None:
        if '.png' not in save_as:
            save_as = save_as + '.png'
        plt.savefig(save_as, dpi=dpi)
    else:
        show = True
    if show:
        plt.show()
    plt.close()






def plot_peak_amplitudes_xyz_alllabels(data: NamedTuple, data_type: str, save_as: str = None) -> None:
    """
    Plots a bar chart with the peak amplitudes of each DIMM.

    ## Parameters
    - `data`: NamedTuple containing data for all eight DIMMs.
    - `data_type`: Type of data contained in the `data` NamedTuple (e.g. 'velocity', 'deformation', 'acceleration')
    - `axis`: Axis of the data contained in the `data` NamedTuple (e.g. 'x', 'y', 'z')
    - `save_as` (Optional): If provided, the plot will be saved as a file with the given name.
    """
    amplitude_key = {'velocity': 'Amplitude', 'deformation': 'Amplitude', 'acceleration': 'Amplitude_g'}[data_type]
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(top=0.890, bottom=0.130, left=0.115, right=0.930)
    df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x = data.x
    df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y = data.y
    df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z = data.z
    x_amplitudes = [max(df1x[amplitude_key]), max(df2x[amplitude_key]), max(df3x[amplitude_key]), max(df4x[amplitude_key]), max(df5x[amplitude_key]), max(df6x[amplitude_key]), max(df7x[amplitude_key]), max(df8x[amplitude_key])]
    y_amplitudes = [max(df1y[amplitude_key]), max(df2y[amplitude_key]), max(df3y[amplitude_key]), max(df4y[amplitude_key]), max(df5y[amplitude_key]), max(df6y[amplitude_key]), max(df7y[amplitude_key]), max(df8y[amplitude_key])]
    z_amplitudes = [max(df1z[amplitude_key]), max(df2z[amplitude_key]), max(df3z[amplitude_key]), max(df4z[amplitude_key]), max(df5z[amplitude_key]), max(df6z[amplitude_key]), max(df7z[amplitude_key]), max(df8z[amplitude_key])]
    sorted_indices = np.argsort(x_amplitudes)[::-1]
    x_amplitudes = np.array(x_amplitudes)[sorted_indices]
    y_amplitudes = np.array(y_amplitudes)[sorted_indices]
    z_amplitudes = np.array(z_amplitudes)[sorted_indices]
    dimm_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])[sorted_indices]
    sum_amplitudes = [sum(x) for x in zip(x_amplitudes, y_amplitudes, z_amplitudes)]    # This is
    # sum_bars = ax.bar(
    #     dimm_numbers,
    #     sum_amplitudes,
    #     # make the color completely transparent but keep the edgecolor
    #     color=[(0.95, 0.95, 0.95, 0)],
    #     # bottom=x_amplitudes + y_amplitudes + z_amplitudes,
    #     edgecolor='black', linewidth=2, alpha=0.75,
    # )
    x_bars = ax.bar(
        dimm_numbers,
        x_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    y_bars = ax.bar(
        dimm_numbers,
        y_amplitudes,
        bottom=x_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    z_bars = ax.bar(
        dimm_numbers,
        z_amplitudes,
        bottom=x_amplitudes + y_amplitudes,
        edgecolor='black', linewidth=0.5, alpha=0.75,
    )
    
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
    tick_labels = []
    total_max_amplitude = max(
        max(x_amplitudes), max(y_amplitudes), max(z_amplitudes),
    )
    # Add the peak amplitude as text above each bar (X, Y, Z)
    for i, df in enumerate([df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x]):
        tick_labels.append(f"DIMM{i+1}")
        ax.text(
            i+1, 
            max(df[amplitude_key]) + (max(x_amplitudes) * 0.002),
            # f"{round(max(df[amplitude_key]),7)}", 
            f"{max(df[amplitude_key]):.5f}", 
            ha='center', 
            va='bottom', 
            fontsize=9, 
            fontstyle='italic'
        )
    dfs = {
        'x': [df1x, df2x, df3x, df4x, df5x, df6x, df7x, df8x],
        'y': [df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y],
        'z': [df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z],
    }
    for i, df in enumerate([df1y, df2y, df3y, df4y, df5y, df6y, df7y, df8y]):
        # tick_labels.append(f'{i+1}')
        ax.text(
            i+1, 
            max(dfs['x'][i][amplitude_key]) + max(dfs['y'][i][amplitude_key]) + ( (max(y_amplitudes)) * 0.002),
            # f"{round(max(df[amplitude_key]),7)}", 
            f"{max(df[amplitude_key]):.5f}", 
            ha='center', 
            va='bottom', 
            fontsize=9, 
            fontstyle='italic'
        )
    for i, df in enumerate([df1z, df2z, df3z, df4z, df5z, df6z, df7z, df8z]):
        # tick_labels.append(f'{i+1}')
        ax.text(
            i+1, 
            max(dfs['z'][i][amplitude_key]) + max(dfs['y'][i][amplitude_key]) + max(dfs['x'][i][amplitude_key]) + ( (max(z_amplitudes)) * 0.002),
            # f"{round(max(df[amplitude_key]),7)}", 
            f"{max(df[amplitude_key]):.5f}", 
            ha='center', 
            va='bottom', 
            fontsize=9, 
            fontstyle='italic'
        )

    ax.legend(
        [x_bars, y_bars, z_bars], 
        ['X', 'Y', 'Z'], 
        fontsize=10, 
        loc='upper right', 
        framealpha=0.8,
    )
    ax.set_xticklabels(tick_labels, fontsize=10)
    amplitude_unit = {'velocity': 'm/s', 'deformation': 'mm', 'acceleration': 'g'}[data_type]
    # amplitude_unit = {'velocity': 'mm/s', 'deformation': 'mm', 'acceleration': 'mm/s²'}[data_type]
    ax.set_ylabel(f'Amplitude  ( ${amplitude_unit}$ )', fontsize=12, labelpad=15, fontweight='bold')
    ax.set_xlabel('DIMM Number', fontsize=12, labelpad=20, fontweight='bold')
    ax.set_title(f'{data_type.title()} Frequency Response - Peak Amplitudes (XYZ)', fontsize=14, pad=20, fontweight='bold')
    if save_as is not None:
        if '.png' not in save_as:
            save_as = save_as + '.png'
        plt.savefig(save_as, dpi=900)
    plt.show()
    plt.close()

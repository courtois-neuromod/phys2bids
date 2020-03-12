# -*- coding: utf-8 -*-
import os
import logging

import matplotlib.pyplot as plt
import numpy as np

LGR = logging.getLogger(__name__)

SET_DPI = 100
FIGSIZE = (18, 10)


def plot_trigger(time, trigger, fileprefix, tr, thr, num_timepoints_expected,
                 figsize=FIGSIZE, dpi=SET_DPI):
    """
    Produces a textfile of the specified extension `ext`,
    containing the given content `text`.

    Parameters
    ----------
    time: numpy ndarray
        time channel
    trigger: numpy ndarray
        trigger channel
    fileprefix: str or path
        A string representing a file name or a fullpath
        to a file, WITHOUT extension
    options: argparse object
        The object produced by `get_parser` in `cli.run.py`
    figsize: tuple
        Desired size of the figure (see `matplotlib`),
        Default is {FIGSIZE}
    dpi: int
        Desired DPI of the figure (see `matplotlib`),
        Default is {SET_DPI}

    Notes
    -----
    Outcome:
    fileprefix + _trigger_time.png:
        Creates new plot `fileprefix_trigger_time.png`.
    """

    def time2ntr(x):
        return x / tr

    def ntr2time(x):
        return x * tr

    thrline = np.ones(time.shape) * thr
    fig = plt.figure(figsize=figsize, dpi=dpi)
    subplot = fig.add_subplot(211)
    subplot.set_title('trigger and time')
    subplot.set_ylim([-0.2, thr * 10])
    subplot.plot(time, trigger, '-', time, thrline, 'r-.', time, time, '-')
    subplot = fig.add_subplot(223)
    subplot.set_xlim([-tr * 4, tr * 4])
    subplot.set_ylim([-0.2, thr * 3])
    subplot.secondary_xaxis('top', functions=(time2ntr, ntr2time))
    subplot.plot(time, trigger, '-', time, time, '-')
    subplot = fig.add_subplot(224)
    subplot.set_xlim([tr * (num_timepoints_expected - 4),
                      tr * (num_timepoints_expected + 4)])
    subplot.set_ylim([-0.2, thr * 3])
    subplot.secondary_xaxis('top', functions=(time2ntr, ntr2time))
    subplot.plot(time, trigger, '-', time, time, '-')
    plt.savefig(fileprefix + '_trigger_time.png', dpi=dpi)
    plt.close()


def plot_all(phys_in, infile, outfile='', dpi=SET_DPI, size=FIGSIZE):
    ch_num = len(phys_in.ch_name)  # get number of channels:
    fig, ax = plt.subplots(ch_num - 1, 1, figsize=size, sharex=True)
    time = phys_in.timeseries[0]  # assume time is first channel
    fig.suptitle(os.path.basename(infile))
    for row, timeser in enumerate(phys_in.timeseries[1:]):
        if timeser.shape != time.shape:
            time_old = np.linspace(0, time[-1], num=timeser.shape[0])
            timeser = np.interp(time, time_old, timeser)
        ax[row].plot(time, timeser)
        ax[row].set_title(f' Channel {row + 1}: {phys_in.ch_name[row + 1]}')
        ax[row].set_ylabel(phys_in.units[row + 1])
        ax[row].xlim = 30 * 60 * phys_in.freq[0]  # maximum display of half an hour
        ax[row].grid()
    ax[row].set_xlabel("seconds")
    if outfile == '':
        outfile = os.path.splitext(os.path.basename(infile))[0] + '.png'
    LGR.info(f'saving channel plot to {outfile}')
    fig.savefig(outfile, dpi=dpi, bbox_inches='tight')

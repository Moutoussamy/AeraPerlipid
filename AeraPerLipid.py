#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Follow the aera per lipid during a MD simulation (NAMD)
"""

__author__ = "Emmanuel Edouard MOUTOUSSAMY"
__version__  = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2020/05"

import sys
import os
import numpy as np
import matplotlib.pyplot as plt



def Convert_Step_to_Time(step,time_step):
    """
    Convert step to time
    :param step: a given step
    :param time_step: the time step used for the sim.
    :return: the time in ns
    """

    time = float(float((step*time_step))/1000000)
    print(time)
    return time


def collect_data(XstFile,nb_lipid):
    """
    collect the X dimension and the Y dimension of the simulation box along the MD simulation. Then calculate
    the aeara per lipid
    :param XstFile: .XST file from NAMD output
    :param nb_lipid: the number of lipid per leaflet
    :return: a list with the aera per lipid
    """
    aera_per_lipid = []
    Time = []

    with open(XstFile) as input_file:
        for line in input_file:
            if "#" not in line:
                line = line.split()
                aera_per_lipid.append((float(line[1])*float(line[5]))/nb_lipid)
                time = Convert_Step_to_Time(int(line[0]),2)
                Time.append(time)


    return aera_per_lipid,Time

if __name__ == '__main__':
    aera_per_lipid = collect_data(sys.argv[1],int(sys.argv[2]))
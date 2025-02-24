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
import matplotlib.pyplot as plt



def Convert_Step_to_Time(step,time_step):
    """
    Convert step to time
    :param step: a given step
    :param time_step: the time step used for the sim.
    :return: the time in ns
    """

    time = float(float((step*time_step))/1000000)

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

def WriteResults(time,aera_per_lipid):
    """
    Write data in a file (aera_per_lipid.dat)
    :param time: list with the time
    :param aera_per_lipid: list of aera per lipid
    :return:
    """
    output = open("aera_per_lipid.dat","w")

    for i in range(len(time)):
        output.write("%f,%f\n"%(time[i],aera_per_lipid[i]))

    output.close()

def PlotAeraPerLipid(time,aera_per_lipid):
    """
    Plot the aera per lipid in function of time
    :param time: Time in ns
    :param aera_per_lipid: aera per lipid
    :return: plot (aera_per_lipid.png)
    """
    plt.plot(time,aera_per_lipid, color="#465C85", linewidth=2)
    plt.xlabel("Time (ns)")
    plt.ylabel(r"Aera per lipid ($\AA$^2)")
    plt.savefig("aera_per_lipid.png", dpi=300, orientation='portrait')

if __name__ == '__main__':
    aera_per_lipid, time = collect_data(sys.argv[1],int(sys.argv[2]))
    WriteResults(time, aera_per_lipid)
    PlotAeraPerLipid(time,aera_per_lipid)

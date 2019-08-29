#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:32:12 2019
Garmin Connect Offline
@author: fusion
"""

import subprocess
import logging
import os

logging.basicConfig(level=logging.DEBUG)

gpx_dir = "/home/fusion/Dokumente/Garmin_files/gpx"
fit_dir = "/home/fusion/Dokumente/Garmin_files/fits"
antfs_acti = "/home/fusion/.config/antfs-cli/3897695517/activities"

def do_nothing():
    pass

def load_fit_files_from_Dev():
    comp = subprocess.run(["antfs-cli"])
    logging.debug(comp.stdout)
    logging.error(comp.stderr)
    logging.debug(comp.returncode)

def convert_files_in_Dir():
    #Path or dev number?
    #path_acti = "/home/fusion/.config/antfs-cli/3897695517/activities"
    for r,d,f in os.walk(gpx_dir):
        do_nothing()
    g_names = []
    for fit in f:
        g_names.append(fit.split('.fit')[0])
    for r,d,f in os.walk(fit_dir):
        do_nothing()
    f_names = []
    for fit in f:
        f_names.append(fit.split('.fit')[0])
    
    for i in g_names:
        try:
            f_names.remove(i)
        except ValueError:
            pass
    #convert it to gpx
    for i in f_names:
        stmp = fit_dir + "/" + i + ".fit"
        dtmp = gpx_dir + "/" + i + ".gpx"
        state = subprocess.run(["gpsbabel","-i", "garmin_fit","-f",stmp,"-o", "gpx","-F",dtmp])
        logging.info(stmp +" -> " + dtmp + "("+str(state.returncode)+")")  

#convert_files_in_Dir()

def copy_files():
    """
    Copies the fit files from antfs dir to fit_dir
    Recognizes converted files, and copies others
    """
    for r,d,f in os.walk(gpx_dir):
        do_nothing()
    gp_names = []
    
    for gp in f:
        tmp = gp.split(".gpx")[0]
        gp_names.append(tmp)
    logging.debug(str(gp_names))
    logging.debug("G-Found")
    ft_names = []
    for r,d,f in os.walk(antfs_acti):
        do_nothing()
    for ft in f:
        tmp = ft.split(".fit")[0]
        ft_names.append(tmp)
    
    dft_names = []
    for r,d,f in os.walk(fit_dir):
        do_nothing()
    for ft in f:
        tmp = ft.split(".fit")[0]
        dft_names.append(tmp)
        
    for i in dft_names:
        try:
            ft_names.remove(i)
        except ValueError:
            pass
    
    logging.debug(str(ft_names))
    logging.debug("Found")
    for i in gp_names:
        try:
            ft_names.remove(i)
        except ValueError:
            pass
    
    logging.debug(ft_names)
    logging.debug("remains")
    
    for i in ft_names:
        stmp = antfs_acti+"/"+ i + ".fit"
        dtmp = fit_dir + "/" + i + ".fit"
        state = subprocess.run(["cp","-u",stmp,dtmp])
        logging.info("Copied "+stmp+" to "+dtmp +"\t with Code "+str(state.returncode))

copy_files()
convert_files_in_Dir()

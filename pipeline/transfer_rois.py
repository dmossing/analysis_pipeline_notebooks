#!/usr/bin/env python

import sys
import os
#sys.path.insert(0, '/home/mossing/code/adesnal')
import run_pipeline_tiffs as rpt
import read_exptlist as re

matfile_fold = '/home/mossing/modulation/matfiles/'
suite2p_fold = '/home/mossing/data1/suite2P/results/'

def run(exptfilename):
    
    foldname = []
    filenames = []
    foldname,filenames = re.read_exptlist(exptfilename,lines_per_expt=3,fileline=1)
    
#    for i in range(len(foldname)):
#        # do matlab stuff to save cropping rectangles
#        print('now saving a cropping rectangle for ' + foldname[i])
    
    for i in range(len(foldname)):

        fileparts = foldname[i].split('/') 
        date = fileparts[0]
        animalid = fileparts[1]
        expt_ids = [str(x) for x in filenames[i]]
        subfold = '_'.join(expt_ids)

        thisfold = suite2p_fold + animalid + '/' + date + '/' + subfold + '/'

        matlab_cmd = '"' + "s2p_output_to_opto_corrected_rois('" + thisfold + "','datafold','" + matfile_fold + "'); exit;" + '"'

        print(matlab_cmd)
        os.system('matlab -r ' + matlab_cmd)


if __name__ == "__main__":
    run(sys.argv[1])

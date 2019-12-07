#!/usr/bin/env python

import sys
import os
#sys.path.insert(0, '/home/mossing/code/adesnal')
import run_pipeline_tiffs as rpt
import read_exptlist as re

matfile_fold = '/home/mossing/modulation/matfiles/'
sbx_fold = '/home/mossing/recurrence/2P/'

def run(exptfilename):
    
    foldname = []
    filenames = []
    foldname,filenames = re.read_exptlist(exptfilename,lines_per_expt=3,fileline=1)
    
    for i in range(len(foldname)):
        # do matlab stuff to save cropping rectangles
        print('now saving a cropping rectangle for ' + foldname[i])
        
        thisfold = matfile_fold+foldname[i]

        if not os.path.exists(thisfold):
            os.makedirs(thisfold)
        
        matlab_cmd = '"' + "save_and_transfer_crop_remote('" + thisfold + "','" + sbx_fold + "',true); exit;" + '"'
    
        print(matlab_cmd)
        os.system('matlab -r ' + matlab_cmd)

if __name__ == "__main__":
    run(sys.argv[1])

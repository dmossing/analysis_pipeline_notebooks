#!/usr/bin/env python

import sys
import os
#sys.path.insert(0, '/home/mossing/code/adesnal')
import run_pipeline_tiffs as rpt
import read_exptlist as re

suite2p_fold = '/home/mossing/data1/suite2P/'
sbx_fold = '/home/mossing/modulation/2P/'

raw_fold = suite2p_fold + 'raw/'
result_fold = suite2p_fold + 'results/'

def run(exptfilename):
    
    foldname = []
    filenames = []
    foldname,filenames = re.read_exptlist(exptfilename,lines_per_expt=3,fileline=1)
    
    for i in range(len(foldname)):
        # do matlab stuff to save cropping rectangles
        print('hope you saved a cropping rectangle for ' + foldname[i])
    
    for i in range(len(foldname)):
        
        matlab_options = "options.green_only = 0; options.targetfold = '" + raw_fold + "'; options.data_foldbase = '" + sbx_fold + "'; "
    
        matlab_cmd = '"' + matlab_options + "gen_2channel_tiffs('" + foldname[i] + "'," + str(filenames[i]) + ",options); exit" + '"'
    
        print(matlab_cmd)
        os.system('matlab -r ' + matlab_cmd)
    
        fileparts = foldname[i].split('/') 
        date = fileparts[0]
        animalid = fileparts[1]
        expt_ids = [str(x) for x in filenames[i]]
        rpt.process_data(animalid,date,expt_ids,nchannels=1,delete_raw=True,result_base=result_fold,raw_base=raw_fold)

if __name__ == "__main__":
    run(sys.argv[1])

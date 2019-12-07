#!/usr/bin/env python

import sys
import os
#sys.path.insert(0, '/home/mossing/code/adesnal')
import run_pipeline_tiffs as rpt
import read_exptlist as re

suite2p_fold = '/home/mossing/data1/suite2P/'
sbx_fold = '/home/mossing/recurrence/2P/'

raw_fold = suite2p_fold + 'raw/'
result_fold = suite2p_fold + 'results/'

def run(exptfilename,diameter=15):
    
    foldname = []
    filenames = []
    foldname,filenames = re.read_exptlist(exptfilename,lines_per_expt=3,fileline=1)
    
    for i in range(len(foldname)):
        # do matlab stuff to save cropping rectangles
        print('hope you saved a cropping rectangle for ' + foldname[i])
    
    for i in range(len(foldname)):

        try:
            shutil.rmtree(fast_disk+'/suite2p')
            os.system('rm -rf /home/mossing/data_ssd/suite2P/bin/suite2p')
            print('fast disk contents deleted')
        except:
            print('fast disk location empty')
        
        matlab_options = "options.green_only = 0; options.targetfold = '" + raw_fold + "'; options.data_foldbase = '" + sbx_fold + "'; "
    
        matlab_cmd = '"' + matlab_options + "gen_2channel_tiffs('" + foldname[i] + "'," + str(filenames[i]) + ",options); exit" + '"'
    
        print(matlab_cmd)
        os.system('matlab -r ' + matlab_cmd)

        try:
            shutil.rmtree(fast_disk+'/suite2p')
            os.system('rm -rf /home/mossing/data_ssd/suite2P/bin/suite2p')
            print('fast disk contents deleted')
        except:
            print('fast disk location empty')
    
        fileparts = foldname[i].split('/') 
        date = fileparts[0]
        animalid = fileparts[1]
        expt_ids = [str(x) for x in filenames[i]]
        rpt.process_data(animalid,date,expt_ids,nchannels=1,delete_raw=True,result_base=result_fold,raw_base=raw_fold,diameter=diameter)

if __name__ == "__main__":
    if len(sys.argv)>2:
        run(sys.argv[1],diameter=sys.argv[2])
    else:
        run(sys.argv[1])

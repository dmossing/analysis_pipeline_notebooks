#!/usr/bin/env python

import sys
import os
#sys.path.insert(0, '/home/mossing/code/adesnal')
with open('path_locations.txt','r') as f:
    path_locs = f.read().splitlines()
for loc in path_locs:    
    print(loc)
    sys.path.insert(0,loc)
import run_pipeline_tiffs as rpt
import read_exptlist as re
import shutil

def run(exptfilename,diameter=15,sbx_fold='/home/mossing/modulation/2P/',suite2p_fold='/home/mossing/data1/suite2P/',fast_disk='/home/mossing/data_ssd/suite2P/bin/',matfile_fold='/home/mossing/modulation/matfiles/'):
    
    raw_fold = suite2p_fold + 'raw/'
    result_fold = suite2p_fold + 'results/'

    foldname = []
    filenames = []
    foldname,filenames = re.read_exptlist(exptfilename,lines_per_expt=3,fileline=1)
    
    for i in range(len(foldname)):
        # do matlab stuff to save cropping rectangles
        print('hope you saved a cropping rectangle for ' + foldname[i])
    
    for i in range(len(foldname)):

        try:
            #shutil.rmtree(fast_disk+'suite2p')
            os.system('rm -rf '+fast_disk+'suite2p')
            print('fast disk contents deleted')
        except:
            print('fast disk location empty')
        
        matlab_options = "options.green_only = 0; options.targetfold = '" + raw_fold + "'; options.data_foldbase = '" + sbx_fold + "'; options.matfile_foldbase = '" + matfile_fold + "';"
    
        matlab_cmd = '"' + matlab_options + "gen_2channel_tiffs('" + foldname[i] + "'," + str(filenames[i]) + ",options); exit; " + '"' # exit
    
        print(matlab_cmd)
        os.system('matlab -r ' + matlab_cmd)
    
        fileparts = foldname[i].split('/') 
        date = fileparts[0]
        animalid = fileparts[1]
        expt_ids = [str(x) for x in filenames[i]]
        rpt.process_data(animalid,date,expt_ids,nchannels=2,delete_raw=True,result_base=result_fold,raw_base=raw_fold,diameter=diameter,fast_disk=fast_disk)

        try:
            #shutil.rmtree(fast_disk+'suite2p')
            os.system('rm -rf '+fast_disk+'suite2p')
            print('fast disk contents deleted')
        except:
            print('fast disk location empty')

if __name__ == "__main__":
    if len(sys.argv)==5:
        location = sys.argv[4]
        if location == 'big-boi':
            suite2p_fold  = '/home/mossing/data1/suite2P/'
            fast_disk = '/home/mossing/data_ssd/suite2P/bin/'
            matfile_fold = '/home/mossing/modulation/matfiles/'
            sbx_fold = sys.argv[3]
        elif (location == 'cluster') or (location == 'savio'):
            suite2p_fold  = '/global/scratch/mossing/2Pdata/suite2P/'
            fast_disk = '/global/scratch/mossing/2Pdata/suite2P/bin/'
            sbx_fold = '/global/scratch/mossing/2Pdata/'
            matfile_fold = '/global/scratch/mossing/matfiles/'
        run(sys.argv[1],diameter=sys.argv[2],sbx_fold=sbx_fold,suite2p_fold=suite2p_fold,fast_disk=fast_disk,matfile_fold=matfile_fold)
    elif len(sys.argv)>3:
        run(sys.argv[1],diameter=sys.argv[2],sbx_fold=sys.argv[3])
    elif len(sys.argv)>2:
        run(sys.argv[1],diameter=sys.argv[2])
    else:
        run(sys.argv[1])

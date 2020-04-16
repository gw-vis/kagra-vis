import epics



# dofs in each stage
dof_dict = {'IP':['H1','H2','H3'],
            'F0':['GAS'],
            'F1':['GAS'],
            'F1':['GAS'],
            'F2':['GAS'],
            'F3':['GAS'],
            'SF':['GAS'],        
            'BF':['H1','H2','H3','V1','V2','V3','GAS'],
            'MN':['H1','H2','H3','V1','V2','V3'],
            'IM':['H1','H2','H3','V1','V2','V3'],
            'TM':['H1','H2','H3','H4'],
            'IM_BLADE':['1','2','3','4'],
            'TMS':['H1','H2','H3','V1','V2','V3']}

chname_dict = {'default':'K1:VIS-{sus}_{stage}_COILOUTF_{dof}_OUTPUT',
               'im_blade':'K1:VIS-{sus}_IM_BLADE_DAMP_COIL{dof}_OUTPUT',
               'tms':'K1:VIS-{sus}_COILOUTF_{dof}_OUTPUT'}

sus_dict = {'typea':['ITMX','ETMX','ITMY','ETMY'],            
            'typeb':['BS','SRM','SR2','SR3'],
            'typebp':['PRM','PR2','PR3'],
            'typec':['MCE','MCI','MCO','IMMT1','IMMT2','OSTM','OMMT1','OMMT2'],
            'typetms':['TMSX','TMSY']}

stage_dict = {'typea':{'IP','BF','F0','F1','F2','F3','MN','IM','TM','IM_BLADE'},
              'typeb':{'IP','BF','F0','F1','IM','TM'},
              'typebp': {'BF','SF','IM','TM'},
              'typec': {'TM'},
              'typetms': {'TMS'}}

# ------------------------------------------------------------------------------
def init(chname):        
    # Define Severity
    val = epics.caput('{0}.{1}'.format(chname,'LLSV'),'MAJOR')
    val = epics.caput('{0}.{1}'.format(chname,'LSV'),'MINOR')
    val = epics.caput('{0}.{1}'.format(chname,'HSV'),'MINOR')
    val = epics.caput('{0}.{1}'.format(chname,'HHSV'),'MAJOR')
    
    # Define Threshold
    val = 2**15
    if val<0.0:
        raise ValueError('Wrong Limit Value: {0} < 0'.format(val))
    elif val==0.0:
        #raise ValueError('Undefined Limit Value!: {0}'.format(val))
        print('Undefined Limit Value!: {0},{1}'.format(chname,val))
    lolo = -val*0.7
    low = -val*0.3
    high = val*0.3
    hihi = val*0.7
    val = epics.caput('{0}.{1}'.format(chname,'LOLO'),lolo)
    val = epics.caput('{0}.{1}'.format(chname,'LOW') ,low)
    val = epics.caput('{0}.{1}'.format(chname,'HIGH'),high)
    val = epics.caput('{0}.{1}'.format(chname,'HIHI'),hihi)


def set_coilout_alert():    
    suslist = sus_dict['typea']
    stagelist = stage_dict['typea']    
    for sus in suslist:
        print(sus)
        for stage in stagelist:
            doflist = dof_dict[stage]
            if stage=='BF' and sus in sus_dict['typeb']:
                doflist = ['GAS']            
            for dof in doflist:
                if stage=='IM_BLADE':
                    chtype = 'im_blade'                    
                elif stage=='TMS':
                    chtype = 'tms'
                else:
                    chtype = 'default'
                    
                if chtype=='default':
                    chname = chname_dict[chtype].format(sus=sus,stage=stage,dof=dof)
                else:
                    chname = chname_dict[chtype].format(sus=sus,dof=dof)
                init(chname)
    

#
# cnt = a0*(disp-a1)
#       a0 [cnt/mm]
#       a1 [cnt]
#
# [1] http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX
# [1] klog#3205

etmx_lvdt_calib_param = {'ETMX_IP_H1':[-3900, -57], 
                         'ETMX_IP_H2':[-4000, -57], 
                         'ETMX_IP_H3':[-4300, -57], 
                         'ETMX_F0_GAS':[-4000, -160], 
                         'ETMX_F1_GAS':[-4500, -70], 
                         'ETMX_F2_GAS':[-4100, -68], 
                         'ETMX_F3_GAS':[-4600, -70], 
                         'ETMX_BF_GAS':[+4900, -70], # [1]
                         'ETMX_BF_V1':[+2600, -6], # [1]
                         'ETMX_BF_V2':[+2600, -6], # [1]
                         'ETMX_BF_V3':[+2600, -6], # [1]
                         'ETMX_BF_H1':[+2500, -7], # [1]
                         'ETMX_BF_H2':[+2600, -6], # [1]
                         'ETMX_BF_H3':[+2800, -5]} # [1]



                
def hoge():
    

                
if __name__ == "__main__":
    set_coilout_alert()

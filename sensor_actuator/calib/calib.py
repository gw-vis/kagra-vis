import epics

chname_fmt_g = 'K1:VIS-{sus}_{stage}_{sensor}INF_{dof}_GAIN'
chname_fmt_o = 'K1:VIS-{sus}_{stage}_{sensor}INF_{dof}_OFFSET'
sus = 'ETMY'
stage = 'IP'
sensor = 'LVDT'
dof = 'H1'

typeasus = ['ITMX','ETMX','ITMY','ETMY']
typebsus = ['BS','SRM','SR2','SR3']
typebpsus = ['PRM','PR2','PR3']
suslist = typeasus + typebsus + typebpsus
suslist = typebsus
for sus in suslist:
    if sus in typeasus:
        stages = ['IP','F0','F1','F2','F3','BF','MN','IM']
    elif sus in typebsus:
        stages = ['IP','BF','F0','F1','IM']
    elif sus in typebpsus:
        stages = ['BF','SF','IM']
    else:
        raise ValueError('Invalid sus {0}'.format(sus))
    for stage in stages:        
        for sensor in ['LVDT','PS','OSEM']:
            if sus in typeasus and stage == 'BF' and sensor=='LVDT':
                dofs = ['H1', 'H2', 'H3', 'V1', 'V2', 'V3','GAS']
            elif sus in typebpsus and stage == 'BF' and sensor=='LVDT':
                dofs = ['H1', 'H2', 'H3', 'V1', 'V2', 'V3','GAS']                
            elif sus in typebsus and stage == 'BF' and sensor=='LVDT':
                dofs = ['GAS']
            elif stage=='IP' and sensor=='LVDT':
                dofs = ['H1','H2','H3']
            elif stage=='IP' and not sensor=='LVDT':
                dofs = []
            elif sus not in typeasus and stage=='IM' and sensor=='OSEM':
                dofs = ['H1', 'H2', 'H3', 'V1', 'V2', 'V3']
            elif sensor=='OSEM':
                dofs = []
            elif sus in typeasus and stage not in ['MN','IM'] and sensor=='PS':
                dofs = []
            elif sus not in typeasus and stage not in ['IM'] and sensor=='OSEM':
                dofs = []                
            elif stage in ['MN','IM'] and sensor=='LVDT':
                dofs = []
            elif stage in ['F0','F1','F2','F3','SF'] and sensor=='LVDT':
                dofs = ['GAS']
            elif sus in typeasus and stage in ['MN','IM'] and sensor=='PS':
                dofs = ['H1','H2','H3','V1','V2','V3']
            elif sensor == 'PS':
                dofs = []
            elif stage=='MN':
                dofs = ['H1','H2','H3','V1','V2','V3']
            elif sus not in typeasus and stage=='IM' and sensor=='OSEM':
                dofs = ['H1','H2','H3','V1','V2','V3']                
            else:
                #break
                raise ValueError('Invalid stage {0} {1}'.format(stage,sensor))
            for dof in dofs:        
                chname = chname_fmt_g.format(sus=sus,stage=stage,
                                           sensor=sensor,dof=dof)
                gain = epics.caget(chname)            
                chname = chname_fmt_o.format(sus=sus,stage=stage,
                                             sensor=sensor,dof=dof)
                offset = epics.caget(chname)
                # x = b0*cnt + b1
                chname = chname.replace('_OFFSET','')                
                print('{1:+04.3f}, {2:+010.1f} : {0}'.format(chname,gain,offset))
                

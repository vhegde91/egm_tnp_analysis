from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = 'root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Moriond18_V5/'

Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Moriond18' : tnpSample('DY_amcatnlo_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18 + 'data/TnPTree_31Mar18_RunB.root' , lumi = 4.763 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18 + 'data/TnPTree_31Mar18_RunC.root' , lumi = 9.748 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18 + 'data/TnPTree_31Mar18_RunD.root' , lumi = 4.317 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18 + 'data/TnPTree_31Mar18_RunE.root' , lumi = 9.423 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18 + 'data/TnPTree_31Mar18_RunF.root' , lumi = 13.51 ),

    }

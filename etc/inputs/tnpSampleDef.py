from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond19 = 'root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Run2018_Moriond19JEC_TreeV3/'


Moriond19_10X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph' : tnpSample('DY_madgraph', 
                                       eosMoriond19 + 'mc/TnPTree_mc_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Moriond19' : tnpSample('DY_madgraph_Moriond19', 
                                       eosMoriond19 + 'mc/TnPTree_mc_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_powheg'          : tnpSample('DY_powheg',
                                       eosMoriond19 + 'mc/TnPTree_mc_DYToEE_M-50_NNPDF31_TuneCP5_13TeV-powheg-pythia8.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2018A' : tnpSample('data_Run2018A' , eosMoriond19 + 'data/TnPTree_data_Run2018A_17Sep18.root' , lumi = 10.209 ),
    'data_Run2018B' : tnpSample('data_Run2018B' , eosMoriond19 + 'data/TnPTree_data_Run2018B_17Sep18.root' , lumi = 6.561 ),
    'data_Run2018C' : tnpSample('data_Run2018C' , eosMoriond19 + 'data/TnPTree_data_Run2018C_17Sep18.root' , lumi = 6.224 ),
    'data_Run2018D' : tnpSample('data_Run2018D' , eosMoriond19 + 'data/TnPTree_data_Run2018D_PromptReco-v2.root' , lumi = 29.347 ),

    }

from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosLegacy16 = 'root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Run2016_17Jul2018_MiniAODv3_TreeV1/'

Legacy16_102X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosLegacy16 + 'mc/TnPTree_mc_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_allExt.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Legacy16' : tnpSample('DY_madgraph_Legacy16', 
                                       eosLegacy16 + 'mc/TnPTree_mc_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_allExt.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Legacy16' : tnpSample('DY_amcatnlo_Legacy16', 
                                       eosLegacy16 + 'mc/TnPTree_mc_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , eosLegacy16 + 'data/TnPTree_data_Run2016B_17Jul18.root' , lumi =  5.444),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosLegacy16 + 'data/TnPTree_data_Run2016C_17Jul18.root' , lumi =  2.396),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosLegacy16 + 'data/TnPTree_data_Run2016D_17Jul18.root' , lumi =  4.256),
    'data_Run2016E' : tnpSample('data_Run2016E' , eosLegacy16 + 'data/TnPTree_data_Run2016E_17Jul18.root' , lumi =  4.054),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosLegacy16 + 'data/TnPTree_data_Run2016F_17Jul18.root' , lumi =  3.105),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosLegacy16 + 'data/TnPTree_data_Run2016G_17Jul18.root' , lumi =  7.544),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosLegacy16 + 'data/TnPTree_data_Run2016H_17Jul18.root' , lumi =  8.746),

    }

#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passingVeto94X'    : '(passingVeto94X   == 1)',
    'passingLoose94X'   : '(passingLoose94X  == 1)',
    'passingMedium94X'  : '(passingMedium94X == 1)',
    'passingTight94X'   : '(passingTight94X  == 1)',
    'passingMVA94Xwp80iso' : '(passingMVA94Xwp80iso == 1)',
    'passingMVA94Xwp90iso' : '(passingMVA94Xwp90iso == 1)',
    'passingMVA94Xwp80noiso' : '(passingMVA94Xwp80noiso == 1)',
    'passingMVA94Xwp90noiso' : '(passingMVA94Xwp90noiso == 1)',
    'passingMVATightNew2'       : '(( abs(el_eta) < 0.8 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (0.2 + (0.032)*(el_pt-10.))) || ( abs(el_eta) < 0.8 && el_pt >= 25 && el_MVA94Xnoiso > 0.68) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (0.1 + (0.025)*(el_pt-10.))) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >= 25 && el_MVA94Xnoiso > 0.475) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.1 + (0.028)*(el_pt-10.))) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >= 25 && el_MVA94Xnoiso > 0.32))',
    'passingMVAVLooseNew'           : '(( abs(el_eta) < 0.8 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (0.488)) || ( abs(el_eta) < 0.8 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.788 + (0.148/15.)*(el_pt-10.))) || ( abs(el_eta) < 0.8 && el_pt >= 25 && el_MVA94Xnoiso > -0.640) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (-0.045)) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.850 + (0.075/15.)*(el_pt-10.))) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >= 25 && el_MVA94Xnoiso > -0.775) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (0.176)) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.81 + (0.077/15.)*(el_pt-10.))) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >= 25 && el_MVA94Xnoiso > -0.733))',
    'passingMVAVLooseFONew'         :'(( abs(el_eta) < 0.8 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (-0.135)) || ( abs(el_eta) < 0.8 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.930 + (0.043/15.)*(el_pt-10.))) || ( abs(el_eta) < 0.8 && el_pt >= 25 && el_MVA94Xnoiso > -0.887) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (-0.417)) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.93 + (0.04/15.)*(el_pt-10.))) || ( abs(el_eta) >= 0.8 && abs(el_eta) < 1.479 && el_pt >= 25 && el_MVA94Xnoiso > -0.890) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >=5 && el_pt < 10 && el_MVA94Xnoiso > (-0.470)) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >=10 && el_pt < 25 && el_MVA94Xnoiso > (-0.942 + (0.032/15.)*(el_pt-10.))) || ( abs(el_eta) >= 1.479 && abs(el_eta) < 2.5 && el_pt >= 25 && el_MVA94Xnoiso > -0.910))',
    }

baseOutDir = 'results/Moriond18/tnpEleID/runBCDEF/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Moriond18_94X['data_Run2017B'].clone(),
    'mcNom'  : tnpSamples.Moriond18_94X['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.Moriond18_94X['DY_amcatnlo_Moriond18'].clone(),
    'tagSel' : tnpSamples.Moriond18_94X['DY_madgraph'].clone(),
}

## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017C'] )
samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017D'] )
samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017E'] )
samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017F'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
weightName = 'weights_2017_runBCDEF.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/FromLxplus/vhegde/public/EGamma_v3/withSUSYids_v1/EGamma_ntuples/Moriond18_V1/PU/mc-V2-customW/DY_madgraph_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/FromLxplus/vhegde/public/EGamma_v3/withSUSYids_v1/EGamma_ntuples/Moriond18_V1/PU/mc-V2-customW/DY_amcatnlo_Moriond18_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/FromLxplus/vhegde/public/EGamma_v3/withSUSYids_v1/EGamma_ntuples/Moriond18_V1/PU/mc-V2-customW/DY_madgraph_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10,20,35,50,100,200,500] },


]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        

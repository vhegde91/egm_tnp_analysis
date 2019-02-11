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
    'passingTight94XV2' : '(passingTight94XV2== 1)',
    #'passingCutBasedVetoNoIso94XV2'  : '(passingCutBasedVetoNoIso94XV2 == 1)',
    #'passingCutBasedLooseNoIso94XV2' : '(passingCutBasedLooseNoIso94XV2 == 1)',
    #'passingCutBasedMediumNoIso94XV2': '(passingCutBasedMediumNoIso94XV2 == 1)',
    #'passingCutBasedTightNoIso94XV2' : '(passingCutBasedTightNoIso94XV2 == 1)',
    #------------------ CutBasedNoIso94XV2 ---------------------
    'passingCutBasedVetoNoIso94XV2' : '( (el_sc_abseta<=1.479 && el_5x5_sieie         < 0.012600 && abs(el_dEtaSeed)     < 0.004630 && abs(el_dPhiIn)       < 0.148000 && el_hoe               < (0.05+(1.16/el_sc_e)+(0.0324*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.209000 && el_mHits            <= 2 && passingConvVeto     == 1 && abs(el_dxy)           < 0.050000 && abs(el_dz)           < 0.100000)||(el_sc_abseta>1.479 && el_5x5_sieie         < 0.045700 && abs(el_dEtaSeed)     < 0.008140 && abs(el_dPhiIn)       < 0.190000 && el_hoe               < (0.05+(2.54/el_sc_e)+(0.183*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.132000 && el_mHits            <= 3 && passingConvVeto     == 1 && abs(el_dxy)          < 0.100000 && abs(el_dz)           < 0.200000))',
    'passingCutBasedLooseNoIso94XV2' : '( (el_sc_abseta<=1.479 && el_5x5_sieie         < 0.011200 && abs(el_dEtaSeed)     < 0.003770 && abs(el_dPhiIn)       < 0.088400 && el_hoe               < (0.05+(1.16/el_sc_e)+(0.0324*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.193000 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)           < 0.050000 && abs(el_dz)           < 0.100000)||(el_sc_abseta>1.479 && el_5x5_sieie         < 0.042500 && abs(el_dEtaSeed)     < 0.006740 && abs(el_dPhiIn)       < 0.169000 && el_hoe               < (0.0441+(2.54/el_sc_e)+(0.183*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.111000 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)          < 0.100000 && abs(el_dz)           < 0.200000))',
    'passingCutBasedMediumNoIso94XV2' : '( (el_sc_abseta<=1.479 && el_5x5_sieie         < 0.010600 && abs(el_dEtaSeed)     < 0.003200 && abs(el_dPhiIn)       < 0.054700 && el_hoe               < (0.046+(1.16/el_sc_e)+(0.0324*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.184000 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)           < 0.050000 && abs(el_dz)           < 0.100000)||(el_sc_abseta>1.479 && el_5x5_sieie         < 0.038700 && abs(el_dEtaSeed)     < 0.006320 && abs(el_dPhiIn)       < 0.039400 && el_hoe               < (0.0275+(2.52/el_sc_e)+(0.183*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.072100 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)          < 0.100000 && abs(el_dz)           < 0.200000))',
    'passingCutBasedTightNoIso94XV2' : '( (el_sc_abseta<=1.479 && el_5x5_sieie         < 0.010400 && abs(el_dEtaSeed)     < 0.002550 && abs(el_dPhiIn)       < 0.022000 && el_hoe               < (0.026+(1.15/el_sc_e)+(0.0324*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.159000 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)           < 0.050000 && abs(el_dz)           < 0.100000)||(el_sc_abseta>1.479 && el_5x5_sieie         < 0.035300 && abs(el_dEtaSeed)     < 0.005010 && abs(el_dPhiIn)       < 0.023600 && el_hoe               < (0.0188+(2.06/el_sc_e)+(0.183*event_rho/el_sc_e)) && abs(el_1overEminus1overP) < 0.019700 && el_mHits            <= 1 && passingConvVeto     == 1 && abs(el_dxy)          < 0.100000 && abs(el_dz)           < 0.200000))',
    'passingMVATightTightIP2D3D' : '( ((el_abseta < 0.8 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 >  (3.447 + 0.063*(el_pt - 25))) || (el_abseta < 0.8 && el_pt >=40 && el_noIsoMVA94XV2 > 4.392) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 > (2.522 + 0.058*(el_pt - 25))) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=40 && el_noIsoMVA94XV2 > 3.392) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 > (1.555 + 0.075*(el_pt - 25))) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=40 && el_noIsoMVA94XV2 > 2.680)) &&  passingTightIP2D && passingTightIP3D)',
    'passingMVATightIP2D3DIDEmu'  : '( ((el_abseta < 0.8 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 >  (3.447 + 0.063*(el_pt - 25))) || (el_abseta < 0.8 && el_pt >=40 && el_noIsoMVA94XV2 > 4.392) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 > (2.522 + 0.058*(el_pt - 25))) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=40 && el_noIsoMVA94XV2 > 3.392) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=10 && el_pt < 40 && el_noIsoMVA94XV2 > (1.555 + 0.075*(el_pt - 25))) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=40 && el_noIsoMVA94XV2 > 2.680)) &&  passingTightIP2D && passingTightIP3D && passingIDEmu)',
    'passingMVAVLooseIP2D'  : '( ((el_abseta < 0.8 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > 1.309) || (el_abseta < 0.8 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 >  (0.887 + 0.088*(el_pt - 25))) || (el_abseta < 0.8 && el_pt >=25 && el_noIsoMVA94XV2 > 0.887) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > 0.373) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 > (0.112 + 0.099*(el_pt - 25))) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=25 && el_noIsoMVA94XV2 > 0.112) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > 0.071) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 > (-0.017 + 0.137*(el_pt - 25))) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=25 && el_noIsoMVA94XV2 > -0.017)) && passingTightIP2D)',
    'passingMVAVLooseFOIP2DIDEmu'  :  '( ((el_abseta < 0.8 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > -0.259) || (el_abseta < 0.8 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 >  (-0.388 + 0.109*(el_pt - 25))) || (el_abseta < 0.8 && el_pt >=25 && el_noIsoMVA94XV2 > -0.388) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > -0.256) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 > (-0.696 + 0.106*(el_pt - 25))) || (el_abseta >= 0.8 && el_abseta < 1.479 && el_pt >=25 && el_noIsoMVA94XV2 > -0.696) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=5 && el_pt < 10 && el_noIsoMVA94XV2 > -1.630) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=10 && el_pt < 25 && el_noIsoMVA94XV2 > (-1.219 + 0.148*(el_pt - 25))) || (el_abseta >= 1.479 && el_abseta < 2.5 && el_pt >=25 && el_noIsoMVA94XV2 > -1.219)) && passingTightIP2D && passingIDEmu)',
    'passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04'  :  'passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04',
    'passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04' :  'passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04',
    'passingLeptonMvaM'                               :  'passingLeptonMvaM',
    'passingLeptonMvaVT'                              :  'passingLeptonMvaVT',
    'passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04New'  :  '((el_MVATTH>0.85) && passingIDEmu && passingTightIP2D && (abs(el_sip3d)<8) && passingMini4)',
    'passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04New' :  '((el_MVATTH>0.90) && passingIDEmu && passingTightIP2D && (abs(el_sip3d)<8) && passingMini4)',
    }

baseOutDir = 'results/Legacy16/tnpEleID/runBCDEFGH/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Legacy16_102X['data_Run2016B'].clone(),
    'mcNom'  : tnpSamples.Legacy16_102X['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.Legacy16_102X['DY_amcatnlo_Legacy16'].clone(),
    'tagSel' : tnpSamples.Legacy16_102X['DY_madgraph'].clone(),
}

## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016C'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016D'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016E'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016F'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016G'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_102X['data_Run2016H'] )

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
weightName = 'weights_2016.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Run2016_17Jul2018_MiniAODv3_TreeV1/PU/DYJetsToLL_PU_profileTree2016.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Run2016_17Jul2018_MiniAODv3_TreeV1/PU/DYJetsToLL_amcatnlo_PU_profileTree2016.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/Run2016_17Jul2018_MiniAODv3_TreeV1/PU/DYJetsToLL_PU_profileTree2016.root')


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
        

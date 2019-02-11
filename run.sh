#!/bin/bash 
myWP=$1
#extraInfo="${1}: passing MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0 in the denominator."
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits<2"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V3 ntuples made from CMSSW_9_4_7"

#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits<2. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs. Updated Trees with new cutbasedID branches by using V4 trees"
#extraInfo="${1}: SF is w.r.t reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs. checking the effect of event_rho vs rho by taking a few bins"
#extraInfo="${1}: SF is w.r.t CutBasedTightNoIso94XV1. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GT."
#extraInfo="${1}: SF is w.r.t MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs. RunC data only"
extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V5 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and 94X_mc2017_realistic_v17, 94X_dataRun2_v11 GTs"
echo "000000000000000000000 Running tool for WP "$myWP
echo $extraInfo
echo "11111111111111 Checking bins 11111111111111"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --checkBins
echo $extraInfo > results/Readme.txt

echo "22222222222222 Creating bins 22222222222222"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --createBins
echo "33333333333333 Creating hists 33333333333333"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --createHists

echo "ffffffffffffff Doing fits fffffffffffffffffff"
echo "44444444444444 Nominal fits 44444444444444"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --doFit
echo "55555555555555 MC fits 55555555555555"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --doFit --mcSig --altSig
echo "66666666666666 alternate signal fits 66666666666666"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --doFit --altSig
echo "77777777777777 alternate BG fits 77777777777777"
python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --doFit --altBkg
echo "======================= Summing it up ================"
#python tnpEGM_fitter.py etc/config/settings_ele.py --flag $myWP --sumUp



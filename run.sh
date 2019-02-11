#!/bin/bash 
myWP=$1
#extraInfo="${1}: SF is w.r.t reco electrons. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1. Fixed missHits bug for CB IDs."
#extraInfo="${1}: SF is w.r.t MVA VLoose + TightIP 2D. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits==0. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
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



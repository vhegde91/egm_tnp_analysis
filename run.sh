#!/bin/bash 
myWP=$1
#extraInfo="${1}: passing MVAVLooseNew and passingTightIP2D in the denominator. pTmin=5GeV. SF is w.r.t MVAVLooseNew+TightIP2D"
#extraInfo="${1}: passing MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0 in the denominator."
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits<2"
extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D"

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



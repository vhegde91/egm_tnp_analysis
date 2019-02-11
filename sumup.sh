#!/bin/bash 
#extraInfo="${1}: SF is w.r.t reco electrons. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1. Fixed missHits bug for CB IDs."
#extraInfo="${1}: SF is w.r.t MVA VLoose + TightIP 2D. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits==0. Using Trees from Run2016_17Jul2018_MiniAODv3_TreeV1"
#for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2
#for i in passingMVATightTightIP2D3D passingMVATightIP2D3DIDEmu passingMVAVLooseIP2D passingMVAVLooseFOIP2DIDEmu
#for i in passingMini passingMini2 passingMini4
#for i in passingMultiIsoM passingMultiIsoT passingMultiIsoEmu passingConvIHit0 passingConvIHit1
#for i in passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04
for i in passing3Qagree
do
    echo "======================= Summing it up for "$i
    tar -xf results_$i.tar
    rm -rf results/
    mv results_$i results
    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --sumUp
    echo $i$extraInfo >> results/Readme.txt
    mv results/ results_$i
    rm results_$i.tar
    tar -cf results_$i.tar results_$i/
done

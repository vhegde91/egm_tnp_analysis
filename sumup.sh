#!/bin/bash 
#extraInfo="${1}: SF is w.r.t reco e. Trees from Run2018_Partial_TreeV1 Re-reco of ABC, prompt reco of D. Fixed bug of missHits in CB IDs."
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + TightIP2D. Trees from Run2018_Partial_TreeV1 Re-reco of ABC, prompt reco of D"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + TightIP2D + TightIP3D + ID Emu. Trees from Run2018_Partial_TreeV1 Re-reco of ABC, prompt reco of D"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + TightIP2D + TightIP3D + ID Emu + ConvVeto + MissHits = 0. Trees from Run2018_Partial_TreeV1 Re-reco of ABC, prompt reco of D"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + TightIP2D + TightIP3D + ID Emu. Trees from Run2018_Moriond19JEC_TreeV3 (V8JEC) Re-reco of ABC, prompt reco of D"
extraInfo="${1}: SF is w.r.t reco e. Trees from Run2018_Moriond19JEC_TreeV3 (V8JEC) Re-reco of ABC, prompt reco of D"
#for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2
for i in passingTight94XV2 passingCutBasedTightNoIso94XV2
#for i in passingMVAVLooseIP2D passingMVAVLooseFOIP2DIDEmu passingMVATightTightIP2D3D passingMVATightIP2D3DIDEmu
#for i in passingMini passingMini2 passingMini4
#for i in passingConvIHit0 passingConvIHit1
#for i in passing3Qagree
#for i in passingMultiIso passingMultiIsoEmu
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

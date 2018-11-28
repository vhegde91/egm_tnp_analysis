#!/bin/bash 
extraInfo="${1}: SF is w.r.t reco e. Trees from Run2018_Partial_TreeV1 Re-reco of ABC, prompt reco of D"
#for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingCutBasedVetoNoIso94XV1 passingCutBasedLooseNoIso94XV1 passingCutBasedMediumNoIso94XV1 passingCutBasedTightNoIso94XV1
for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingTight94XV2
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

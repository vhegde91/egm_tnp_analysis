#!/bin/bash 
#passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso passingMVATightNew2 passingMVALooseNew passingMVALooseFONew
i=passingMVAVLooseTightIP2DMini

for bin in 03
do
    rm -r results/
    mv results_$i results
    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --doFit --iBin $bin
#    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --doFit --mcSig --altSig --iBin $bin
#    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --doFit --altSig --iBin $bin
#    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --doFit --altBkg --iBin $bin
done
#echo "======================= Summing it up for "$i
#python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --sumUp
#mv results/ results_$i
#rm results_$i.tar
#tar -cf results_$i.tar results_$i/

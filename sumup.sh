#!/bin/bash 
#for i in passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso passingMVATightNew2 passingMVALooseNew passingMVALooseFONew
for i in passingMVA94Xwp90noiso
#for i in passingMVA94Xwp90iso passingMVATightNew2 passingMVAVLooseNew passingMVAVLooseFONew
#for i in passingMVATightNew2
do
    echo "======================= Summing it up for "$i
    tar -xf results_$i.tar
    rm -rf results/
    mv results_$i results
    python tnpEGM_fitter.py etc/config/settings_ele.py --flag $i --sumUp
    mv results/ results_$i
    rm results_$i.tar
    tar -cf results_$i.tar results_$i/
done

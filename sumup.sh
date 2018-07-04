#!/bin/bash 
#extraInfo=": passing MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0 in the denominator."
#extraInfo=": reco ele in the denominator. min pT 5GeV"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits<2"
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V3 ntuples made from CMSSW_9_4_7"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
extraInfo="${1}: SF is w.r.t Reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#for i in passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso passingMVATightNew2 passingMVALooseNew passingMVALooseFONew
#for i in passingMVA94Xwp90iso passingMVATightNew2 passingMVAVLooseNew passingMVAVLooseFONew
#for i in passingMVATightNewTightIP2D3D
#for i in passingMultiIsoM passingMultiIsoT passingMultiIsoEmu passingConvIHit0
#for i in passingMVAVLooseNew passingMVAVLooseNewIP2D passingMVAVLooseFONew passingMVAVLooseFONewIP2DIDEmu
for i in passingMultiIsoNew passingConvIHit1
#for i in passingMVATightNew2IP2D3DIDEmu
#for i in passing3Qagree2
#for i in passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaM passingLeptonMvaVT passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04New passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04New
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

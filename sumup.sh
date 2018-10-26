#!/bin/bash 
#extraInfo=": passing MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0 in the denominator."
#extraInfo=": reco ele in the denominator. min pT 5GeV"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D + ConvVeto + MissHits<2. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V3 ntuples made from CMSSW_9_4_7"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs. RunC data only"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + ID Emu + TightIP2D + TightIP3D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t Reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA VLoose ID + IP2D. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t CutBasedTightNoIso94X. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
#extraInfo="${1}: SF is w.r.t MVA Tight ID + TightIP2D + TightIP3D + IDEmu + ConvVeto + MissHits==0. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs"
extraInfo="${1}: SF is w.r.t reco electrons. Using V4 ntuples made from CMSSW_9_4_7 with 31Mar18_miniaod and latest GTs. Trees have bug, used cut string"
#for i in passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso passingMVATightNew2 passingMVALooseNew passingMVALooseFONew
#for i in passingMVA94Xwp90iso passingMVATightNew2 passingMVAVLooseNew passingMVAVLooseFONew
#for i in passingMVATightNewTightIP2D3D
#for i in passingMultiIsoM passingMultiIsoT passingMultiIsoEmu passingConvIHit0
#for i in passingMVAVLooseNew passingMVAVLooseNewIP2D passingMVAVLooseFONew passingMVAVLooseFONewIP2DIDEmu
#for i in passingConvIHit0 #passingMultiIsoNew passingConvIHit1
#for i in passingMVATightNew2IP2D3DIDEmu
#for i in passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaM passingLeptonMvaVT passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04New passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04New
######################
#for i in passingCutBasedLooseNoIso94X passingCutBasedMediumNoIso94X passingCutBasedTightNoIso94X passingCutBasedVetoNoIso94X
#for i in passingMVAVLooseNewIP2D passingMVAVLooseFONewIP2DIDEmu passingMVATightNewTightIP2D3D passingMVATightNew2IP2D3DIDEmu
#for i in passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passingMini
#for i in passing3Qagree
#for i in passingConvIHit0
for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingCutBasedVetoNoIso94XV1 passingCutBasedLooseNoIso94XV1 passingCutBasedMediumNoIso94XV1 passingCutBasedTightNoIso94XV1
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

#!/bin/sh
rm egm_tnp_analysis.tar
rm libCpp/*.d libCpp/*.so libCpp/*.pcm
tar cf egm_tnp_analysis.tar Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON_RUNC.txt etc libCpp libPython Makefile tnpEGM_fitter.py run.sh
exeAtWorker="workerEGM.sh"
filesToTransfer="egm_tnp_analysis.tar"

#for i in passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso passingMVATightNew2 passingMVAVLooseNew passingMVAVLooseFONew
#for i in passingMVA94Xwp90noiso passingVeto94X
#for i in passingMVAVLooseNew passingMVAVLooseFONew passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passingMVATightNewTightIP2D3D
#for i in passingMultiIsoM passingMultiIsoT passingMultiIsoEmu passingMultiIsoNewJECv32 passingMultiIsoNew passingConvIHit0
#for i in passingConvIHit0 #passingMultiIsoNew passingConvIHit1
#for i in passingMVATightNew2IP2D3DIDEmu
#for i in passingMVAVLooseNew passingMVAVLooseNewIP2D passingMVAVLooseFONew passingMVAVLooseFONewIP2DIDEmu
#for i in passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 passingLeptonMvaM passingLeptonMvaVT passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04New passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04New
##############
#for i in passingCutBasedLooseNoIso94X passingCutBasedMediumNoIso94X passingCutBasedTightNoIso94X passingCutBasedVetoNoIso94X
#for i in passingMVAVLooseNewIP2D passingMVAVLooseFONewIP2DIDEmu passingMVATightNewTightIP2D3D passingMVATightNew2IP2D3DIDEmu
#for i in passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
#for i in passing3Qagree
#for i in passingMini
#for i in passingConvIHit0 passingConvIHit1
#for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingCutBasedVetoNoIso94XV1 passingCutBasedLooseNoIso94XV1 passingCutBasedMediumNoIso94XV1 passingCutBasedTightNoIso94XV1
#for i in passingTight94X passingMedium94X
#for i in passingCBTightNoIso94XV1_eventRho passingCBTightNoIso94XV1_rho
for i in passingMultiIsoJECv32 passingMultiIsoEmuJECv32 passingMultiIsoNew
do
    echo "Submitting job to get SF for "$i
    jdl_file="jdl_EGM_SF_${i}_job.jdl"
    log_prefix="condor_EGM_SF_${i}_job"
    echo "universe = vanilla">$jdl_file
    echo "Executable = $exeAtWorker">>$jdl_file
    echo "Should_Transfer_Files = YES">>$jdl_file
    echo "WhenToTransferOutput = ON_EXIT_OR_EVICT">>$jdl_file
    echo "Transfer_Input_Files = ${filesToTransfer}">>$jdl_file
    echo "Output = ${log_prefix}.stdout">>$jdl_file
    echo "Error = ${log_prefix}.stderr">>$jdl_file
    echo "Log = ${log_prefix}.condor">>$jdl_file
    echo "notification = never">>$jdl_file
    echo "Arguments = ${i}">>$jdl_file
    echo "Queue">>$jdl_file
    condor_submit $jdl_file
done

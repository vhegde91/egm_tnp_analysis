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
#for i in passingMultiIsoM passingMultiIsoT passingMultiIsoEmu passingConvIHit0
#for i in passingMVATightNew2IP2D3DIDEmu
#for i in passing3Qagree2
#for i in passingMVAVLooseNew passingMVAVLooseNewIP2D passingMVAVLooseFONew passingMVAVLooseFONewIP2DIDEmu
for i in passingConvIHit1 #passingMVAVLooseNew passingMVAVLooseTightIP2DMini passingMVAVLooseTightIP2DMini2 passingMVAVLooseTightIP2DMini4
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

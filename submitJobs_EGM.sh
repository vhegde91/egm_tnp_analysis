#!/bin/sh
rm egm_tnp_analysis.tar
rm libCpp/*.d libCpp/*.so libCpp/*.pcm
tar cf egm_tnp_analysis.tar etc libCpp libPython Makefile tnpEGM_fitter.py run.sh
exeAtWorker="workerEGM.sh"
filesToTransfer="egm_tnp_analysis.tar"

#for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingCutBasedVetoNoIso94XV1 passingCutBasedLooseNoIso94XV1 passingCutBasedMediumNoIso94XV1 passingCutBasedTightNoIso94XV1
for i in passingCutBasedVetoNoIso94XV2 passingCutBasedLooseNoIso94XV2 passingCutBasedMediumNoIso94XV2 passingCutBasedTightNoIso94XV2 passingTight94XV2
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

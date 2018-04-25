#!/bin/sh
rm egm_tnp_analysis.tar
#rm libCpp/*.d libCpp/*.so libCpp/*.pcm
tar cf egm_tnp_analysis.tar Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON_RUNC.txt etc libCpp libPython Makefile tnpEGM_fitter.py run.sh

for i in passingVeto94X passingLoose94X passingMedium94X passingTight94X passingMVA94Xwp90noiso
#for i in passingMVA94Xwp90noiso passingVeto94X passingMVATightNew2
do
    echo "------- Submitting job for ${i}"
    bsub -q 8nh lxplusbatchscript.sh $i
done
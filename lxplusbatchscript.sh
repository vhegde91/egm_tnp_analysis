#!/bin/bash
WPname=$1
currDir=$(pwd)
cp /afs/cern.ch/work/v/vhegde/public/EGamma_v3/withSUSYids_v1/TnPsusy/CMSSW_9_4_0/src/egm_tnp_analysis/egm_tnp_analysis.tar .

source /cvmfs/cms.cern.ch/cmsset_default.sh
#export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_4_0
cd CMSSW_9_4_0/src/
eval `scramv1 runtime -sh`
pwd
echo "Done setting up CMSSW....."
######################################
# SETUP PRIVATE STUFF...
######################################
mkdir egm_tnp_analysis
echo "ls"
ls
cd egm_tnp_analysis
pwd
mv $currDir/egm_tnp_analysis.tar .

tar xf egm_tnp_analysis.tar
rm libCpp/*.d libCpp/*.so libCpp/*.pcm
source etc/scripts/setup94.sh
echo "-----------------------Compiling.............."
make clean
make

echo "Compile and setup done. RUNNING ANALYSIS"
pwd
echo "----------------------------------------"
./run.sh $WPname
echo "--------------DONE analysis. ls"
ls
mv results/ results_$WPname
tar cf results_$WPname.tar results_$WPname
#mv results_$WPname.tar $currDir
echo "COPYING OUTPUT"
rfcp results_$WPname.tar /afs/cern.ch/work/v/vhegde/public/EGamma_v3/withSUSYids_v1/TnPsusy/CMSSW_9_4_0/src/egm_tnp_analysis/
echo "done"
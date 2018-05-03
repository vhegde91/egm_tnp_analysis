#!/bin/sh

WPname=$1
currDir=$(pwd)
######################################
# SETUP CMSSW STUFF...
######################################
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_4_0
cd CMSSW_9_4_0/src/
eval `scramv1 runtime -sh`
pwd

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
#source etc/scripts/setup94.sh
make clean
make

echo "Compile and setup done. RUNNING ANALYSIS"
pwd
echo "----------------------------------------"
#/eos/uscms/store/user/vhegde/
#root -l -b root://cmseos.fnal.gov//store/user/vhegde/EGamma_ntuples/FromLxplus/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/PU/mc-V2/DY_madgraph_ele.pu.puTree.root -q
echo "----------------------------------------"
./run.sh $WPname

echo "DONE analysis. ls"
ls
#echo "hi..." > results/a.txt
mv results/ results_$WPname
tar cf results_$WPname.tar results_$WPname
mv results_$WPname.tar $currDir
echo "COPYING OUTPUT"

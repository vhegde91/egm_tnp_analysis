import ROOT as rt
import numpy as np
import sys
import argparse
import os

print '** puReweighter requires root_numpy.'
print '** To install on lxplus: '
print 'pip install --user root_numpy'
from root_numpy import  tree2array, array2tree


customWeights_17Nov2017MCv2 = {


    '2017_runBCDEF' : [0.000319471, 0.043333,  0.0627865,  0.0647238,  0.0780242, 0.108199,  0.111983,
                 0.148095,    0.112399,  0.381801,   0.494781,   0.647735,  0.674107,  0.687767,
                 0.723788,    0.784618,  0.898843,   0.979519,   1.0633,    1.11899,   1.16819,
                 1.22006,     1.27549,   1.30905,    1.31339,    1.32447,   1.31354,   1.32983,
                 1.34375,     1.33185,   1.29874,    1.24632,    1.18278,   1.11995,   1.04354,
                 0.988411,    0.944833,  0.896181,   0.851375,   0.820549,  0.820257,  0.877121,
                 0.9505,      1.06921,   1.23497,    1.41449,    1.57161,   1.62378,   1.64322,
                 1.5508,      1.37578,   1.1718,     0.953895,   0.744876,  0.558862,  0.394524,
                 0.285334,    0.20402,   0.146289,   0.107565,   0.0833341, 0.0678563, 0.0583878,
                 0.0521837,   0.0511854, 0.0457683,  0.042717,   0.0450134, 0.0516682, 0.0609794,
                 0.0681131,   0.0769145, 0.068758,   0.082488,   0.0519442, 0.0923373, 0.0581781,
                 0.0534347,   0.031191,  0.0244144,  0.00726572, 0.0146515, 0.0141407, 0.00517426,
                 0.00389476,  0.00262877,0.00503468, 0.000850185,0.00080179,0.00057269,0.00170316,
                 0.000746922, 0.00096581,0.00091529, 9.42116e-05,6.2216e-05,8.9658e-05,4.89178e-05,
                 7.75365e-05, 1.57862e-05],

    }

puMC = {
    'Spring2016MC_PUscenarioV1' : [ 0.000829312873542, 0.00124276120498, 0.00339329181587, 0.00408224735376, 0.00383036590008, 
                                    0.00659159288946,  0.00816022734493, 0.00943640833116, 0.0137777376066,  0.017059392038,
                                    0.0213193035468,   0.0247343174676,  0.0280848773878,  0.0323308476564,  0.0370394341409,  
                                    0.0456917721191,   0.0558762890594,  0.0576956187107,  0.0625325287017,  0.0591603758776,
                                    0.0656650815128,   0.0678329011676,  0.0625142146389,  0.0548068448797,  0.0503893295063,  
                                    0.040209818868,    0.0374446988111,  0.0299661572042,  0.0272024759921,  0.0219328403791,
                                    0.0179586571619,   0.0142926728247,  0.00839941654725, 0.00522366397213, 0.00224457976761, 
                                    0.000779274977993, 0.000197066585944,7.16031761328e-05,0.0             , 0.0,
                                    0.0,        0.0,        0.0,        0.0,        0.0,    
                                    0.0,        0.0,        0.0,        0.0,        0.0],
    
    'Moriond17MC_mix_2016'      : [ 1.78653e-05 ,2.56602e-05 ,5.27857e-05 ,8.88954e-05 ,0.000109362 ,0.000140973 ,0.000240998 ,
                                    0.00071209  , 0.00130121 ,0.00245255  ,0.00502589  ,0.00919534  ,0.0146697   ,0.0204126   ,
                                    0.0267586   ,0.0337697   ,0.0401478   ,0.0450159   ,0.0490577   ,0.0524855   ,0.0548159   ,
                                    0.0559937   ,0.0554468   ,0.0537687   ,0.0512055   ,0.0476713   ,0.0435312   ,0.0393107   ,
                                    0.0349812   ,0.0307413   ,0.0272425   ,0.0237115   ,0.0208329   ,0.0182459   ,0.0160712   ,
                                    0.0142498   ,0.012804    ,0.011571    ,0.010547    ,0.00959489  ,0.00891718  ,0.00829292  , 
                                    0.0076195   ,0.0069806   ,0.0062025   ,0.00546581  ,0.00484127  ,0.00407168  ,0.00337681  ,
                                    0.00269893  ,0.00212473  ,0.00160208  ,0.00117884  ,0.000859662 ,0.000569085 ,0.000365431 ,
                                    0.000243565 ,0.00015688  ,9.88128e-05 ,6.53783e-05 ,3.73924e-05 ,2.61382e-05 ,2.0307e-05  ,
                                    1.73032e-05 ,1.435e-05   ,1.36486e-05 ,1.35555e-05 ,1.37491e-05 ,1.34255e-05 ,1.33987e-05 ,
                                    1.34061e-05 ,1.34211e-05 ,1.34177e-05 ,1.32959e-05 ,1.33287e-05 ],




    'Moriond18MC_mix_2017' :[3.39597497605e-05,    6.63688402133e-06,     1.39533611284e-05,     3.64963078209e-05,     6.00872171664e-05,     9.33932578027e-05,    0.000120591524486,
                             0.000128694546198,    0.000361697233219,     0.000361796847553,     0.000702474896113,     0.00133766053707,      0.00237817050805,     0.00389825605651,
                             0.00594546732588,     0.00856825906255,      0.0116627396044,       0.0148793350787,       0.0179897368379,       0.0208723871946,      0.0232564170641,
                             0.0249826433945,      0.0262245860346,       0.0272704617569,       0.0283301107549,       0.0294006137386,       0.0303026836965,      0.0309692426278,   
                             0.0308818046328,      0.0310566806228,       0.0309692426278,       0.0310566806228,       0.0310566806228,       0.0310566806228,      0.0307696426944,
                             0.0300103336052,      0.0288355370103,       0.0273233309106,       0.0264343533951,       0.0255453758796,       0.0235877272306,      0.0215627588047,
                             0.0195825559393,      0.0177296309658,       0.0160560731931,       0.0146022004183,       0.0134080690078,       0.0129586991411,      0.0125093292745,
                             0.0124360740539,      0.0123547104433,       0.0123953922486,       0.0124360740539,       0.0124360740539,       0.0123547104433,      0.0124360740539,
                             0.0123387597772,      0.0122414455005,       0.011705203844,        0.0108187105305,       0.00963985508986,      0.00827210065136,     0.00683770076341,
                             0.00545237697118,     0.00420456901556,      0.00367513566191,      0.00314570230825,      0.0022917978982,       0.00163221454973,     0.00114065309494,
                             0.000784838366118,    0.000533204105387,     0.000358474034915,     0.000238881117601,     0.0001984254989,       0.000157969880198,    0.00010375646169,
                             6.77366175538e-05,    4.39850477645e-05,     2.84298066026e-05,     1.83041729561e-05,     1.17473542058e-05,     7.51982735129e-06,    6.16160108867e-06,
                             4.80337482605e-06,    3.06235473369e-06,     1.94863396999e-06,     1.23726800704e-06,     7.83538083774e-07,     4.94602064224e-07,    3.10989480331e-07,
                             1.94628487765e-07,    1.57888581037e-07,     1.2114867431e-07,      7.49518929908e-08,     4.6060444984e-08,      2.81008884326e-08,    1.70121486128e-08,
                             1.02159894812e-08],


    'MC2018_JuneProjectionFull18' :[4.695341e-10, 1.206213e-06, 1.162593e-06, 6.118058e-06, 1.626767e-05,
	   3.508135e-05, 7.12608e-05, 0.0001400641, 0.0002663403, 0.0004867473,
	   0.0008469, 0.001394142, 0.002169081, 0.003198514, 0.004491138,
	   0.006036423, 0.007806509, 0.00976048, 0.0118498, 0.01402411,
	   0.01623639, 0.01844593, 0.02061956, 0.02273221, 0.02476554,
	   0.02670494, 0.02853662, 0.03024538, 0.03181323, 0.03321895,
	   0.03443884, 0.035448, 0.03622242, 0.03674106, 0.0369877,
	   0.03695224, 0.03663157, 0.03602986, 0.03515857, 0.03403612,
	   0.0326868, 0.03113936, 0.02942582, 0.02757999, 0.02563551,
	   0.02362497, 0.02158003, 0.01953143, 0.01750863, 0.01553934,
	   0.01364905, 0.01186035, 0.01019246, 0.008660705, 0.007275915,
	   0.006043917, 0.004965276, 0.004035611, 0.003246373, 0.002585932,
	   0.002040746, 0.001596402, 0.001238498, 0.0009533139, 0.0007282885,
	   0.000552306, 0.0004158005, 0.0003107302, 0.0002304612, 0.0001696012,
	   0.0001238161, 8.96531e-05, 6.438087e-05, 4.585302e-05, 3.23949e-05,
	   2.271048e-05, 1.580622e-05, 1.09286e-05, 7.512748e-06, 5.140304e-06,
	   3.505254e-06, 2.386437e-06, 1.625859e-06, 1.111865e-06, 7.663272e-07,
	   5.350694e-07, 3.808318e-07, 2.781785e-07, 2.098661e-07, 1.642811e-07,
	   1.312835e-07, 1.081326e-07, 9.141993e-08, 7.890983e-08, 6.91468e-08,
	   6.119019e-08, 5.443693e-08, 4.85036e-08, 4.31486e-08, 3.822112e-08],#from https://github.com/lsoffi/egm_tnp_analysis/blob/egm_tnp_Prompt2018_102X_10222018_MC102XECALnoiseFix200kRelVal/libPython/puReweighter.py#L80




}

### MC pu scenario to be used
#puMCscenario = 'Spring2016MC_PUscenarioV1'
puMCscenario = 'MC2018_JuneProjectionFull18'
customWeightsName= 'weights'
puDirEOS = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01162018/PU/'

#### Compute weights for all data epoch specified below
puDataEpoch = {
    '2017_runB' : puDirEOS + 'pileup_2017_RUNB.root',
    '2017_runC' : puDirEOS + 'pileup_2017_RUNC.root',
    '2017_runD'  : puDirEOS +'pileup_2017_RUND.root' ,
    '2017_runE'  : puDirEOS +'pileup_2017_RUNE.root' ,
    '2017_runF' : puDirEOS + 'pileup_2017_RUNF.root',    
    '2017_runBCDEF' : puDirEOS + 'pileup_2017_41fb.root',
    }

nVtxDataEpoch = {
    '2016_runBCD' : 'etc/inputs/nVtx_2016_runBCD.root',
    '2016_runEF'  : 'etc/inputs/nVtx_2016_runEF.root' ,
    '2016_runGH'  : 'etc/inputs/nVtx_2016_runGH.root' ,
}

rhoDataEpoch = {
    '2016_runE'   : 'etc/inputs/rho_pu_runE.root',
    '2016_runGH'  : 'etc/inputs/rho_pu_runGH.root',
}





def reweight( sample, puType = 0,useCustomW=False  ):
    if sample.path is None:
        print '[puReweighter]: Need to know the MC tree (option --mcTree or sample.path)'
        sys.exit(1)
    

### create a tree with only weights that will be used as friend tree for reweighting different lumi periods
    print 'Opening mc file: ', sample.path[0]
    fmc = rt.TFile(sample.path[0],'read')
    tmc = None
    if sample.tnpTree is None:
        dirs = fmc.GetListOfKeys()
        for d in dirs:
            if (d.GetName() == "sampleInfo"): continue
            tmc = fmc.Get("%s/fitter_tree" % d.GetName())
    else:
        tmc = fmc.Get(sample.tnpTree)
    

#### can reweight vs nVtx but better to reweight v truePU
    puMCnVtx = []
    puMCrho = []
    if   puType == 1 :
        hmc   = rt.TH1F('hMC_nPV'  ,'MC nPV'  , 75,-0.5,74.5)
        tmc.Draw('event_nPV>>hMC_nPV','','goff')
        hmc.Scale(1/hmc.Integral())
        for ib in range(1,hmc.GetNbinsX()+1):
            puMCnVtx.append( hmc.GetBinContent(ib) )
        print 'len nvtxMC = ',len(puMCnVtx)

    elif puType == 2 :
        hmc   = rt.TH1F('hMC_rho'  ,'MC #rho'  , 75,-0.5,74.5)
        tmc.Draw('rho>>hMC_rho','','goff')
        hmc.Scale(1/hmc.Integral())
        for ib in range(1,hmc.GetNbinsX()+1):
            puMCrho.append( hmc.GetBinContent(ib) )
        print 'len rhoMC = ',len(puMCrho)
    

    puDataDist = {}
    puDataArray= {}
    weights = {}
    epochKeys = puDataEpoch.keys()
    if puType == 1  : epochKeys = nVtxDataEpoch.keys()
    if puType == 2  : epochKeys = rhoDataEpoch.keys()
 
    for pu in epochKeys:
        fpu = None
        if   puType == 1 : fpu = rt.TFile(nVtxDataEpoch[pu],'read')
        elif puType == 2 : fpu = rt.TFile(rhoDataEpoch[pu],'read')
        else             : fpu = rt.TFile(puDataEpoch[pu],'read')
        puDataDist[pu] = fpu.Get('pileup').Clone('puHist_%s' % pu)
        puDataDist[pu].Scale(1./puDataDist[pu].Integral())
        puDataDist[pu].SetDirectory(0)
        puDataArray[pu] = []
        for ipu in range(len(puMC[puMCscenario])):
            ibin_pu  = puDataDist[pu].GetXaxis().FindBin(ipu+0.00001)
            puDataArray[pu].append(puDataDist[pu].GetBinContent(ibin_pu))
        print 'puData[%s] length = %d' % (pu,len(puDataArray[pu]))
        fpu.Close()
        weights[pu] = []

    mcEvts = tree2array( tmc, branches = ['weight','truePU','event_nPV','rho'] )


    pumc = puMC[puMCscenario]
    if   puType == 1:  pumc = puMCnVtx
    elif puType == 2:  pumc = puMCrho
    else            :  pumc = puMC[puMCscenario]

    puMax = len(pumc)
    print '-> nEvtsTot ', len(mcEvts)
#    print "--------------------------" 
    for ievt in xrange(len(mcEvts)):
        if ievt%100000 == 0 :            print 'iEvt:',ievt
#        print 'iEvt:',ievt
        evt = mcEvts[ievt]
        for pu in epochKeys:
#            print pu
            customWeights=customWeights_17Nov2017MCv2[pu]
#            print customWeights_17Nov2017MCv2[pu]
#            print "--------------------------"
            pum = -1
            pud = -1
            if puType == 1 and evt['event_nPV'] < puMax:
                pud = puDataArray[pu][evt['event_nPV']]
                pum = pumc[evt['event_nPV']]
            if puType == 2 and int(evt['rho']) < puMax:
                pud = puDataArray[pu][int(evt['rho'])]
                pum = pumc[int(evt['rho'])]
            elif puType == 0:
#                if ievt%1000: print pu, evt['truePU']
                if evt['truePU']> 0 and evt['truePU']<99: 
                    pud = puDataArray[pu][evt['truePU']] 
                    pum = pumc[evt['truePU']]
            puw = 0
            if pum > 0: 
                puw  = pud/pum
#                if use customized weights
            if useCustomW:
                puw=0
                if  evt['truePU']> 0 and evt['truePU']<97:
                    puw = customWeights[evt['truePU']]
                
#                    print evt['truePU'],puw

            if evt['weight'] > 0 : totw = +puw
            else                 : totw = -puw
            weights[pu].append( ( puw,totw) )
#    print "====================="
#    print weights[pu]

    newFile    = rt.TFile( sample.puTree, 'recreate')

    for pu in epochKeys:
        treeWeight = rt.TTree('weights_%s'%pu,'tree with weights')
        wpuarray = np.array(weights[pu],dtype=[('PUweight',float),('totWeight',float)])
        array2tree( wpuarray, tree = treeWeight )
        treeWeight.Write()

    newFile.Close()    
    fmc.Close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tnp EGM pu reweighter')
    parser.add_argument('--mcTree'  , dest = 'path',  default = None, help = 'MC tree to compute weights for')
    parser.add_argument('puTree'    , default = None                , help = 'output puTree')

    args = parser.parse_args()
    args.path = [args.path]
    reweight(args)






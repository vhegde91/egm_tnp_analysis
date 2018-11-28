#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include"TH1.h"
#include"TROOT.h"
#include"TH2.h"
#include"TFile.h"
#include"TDirectory.h"
#include"TTree.h"
#include"TBrowser.h"
#include"TF1.h"
#include<iomanip>
#include"TGraphErrors.h"
#include"TGraphAsymmErrors.h"
#include"TGraph.h"
#include"TCanvas.h"
#include"TPaveStats.h"
#include"TStyle.h"
#include"TLegend.h"

float event_rho,el_5x5_sieie,el_dEtaSeed,el_dPhiIn,el_hoe,el_1overEminus1overP,el_dxy,el_dz,el_mHits,el_sc_abseta,el_sc_e;
Int_t passingConvVeto;

//V1
//------------------------------------------VetoEB   LooseEB  MediumEB   TightEB  VetoEE   LooseEE  MediumEE  TightEE
std::vector<float> maxSigmaIetaIeta94XV1 = {0.0128,  0.0105,  0.0105,    0.0104,  0.0445,  0.0356,  0.0309,   0.0305};
std::vector<float> maxDEtaIn94XV1        = {0.00523, 0.00387, 0.00365,   0.00353, 0.00984, 0.0072,  0.00625,  0.00567};
std::vector<float> maxDPhiIn94XV1        = {0.159,   0.0716,  0.0588,    0.0499,  0.157,   0.147,   0.0355,   0.0165};
std::vector<float> maxHOverE94XV1        = {0.05,    0.05,    0.026,     0.026,   0.05,    0.0414,  0.026,    0.026};
std::vector<float> maxHOverE_p1_94XV1    = {1.12,    1.12,    1.12,      1.12,    0.5,     0.5,     0.5,      0.5};
std::vector<float> maxHOverE_p2_94XV1    = {0.0368,  0.0368,  0.0368,    0.0368,  0.201,   0.201,   0.201,    0.201};
std::vector<float> maxOoEmooP94XV1       = {0.193,   0.129,   0.0327,    0.0278,  0.0962,  0.0875,  0.0335,   0.0158};
std::vector<float> maxd094XV1            = {0.05,    0.05,    0.05,      0.05,    0.10,    0.10,    0.10,     0.10};
std::vector<float> maxdz94XV1            = {0.10,    0.10,    0.10,      0.10,    0.20,    0.20,    0.20,     0.20};
std::vector<int>   maxMissingHits94XV1   = {2,        1,        1,        1,         3,       1,        1,        1};
std::vector<bool>  convVeto94XV1         = {true,     true,     true,     true,      true,    true,     true,     true};
//V2
//------------------------------------------VetoEB    LooseEB   MediumEB  TightEB    VetoEE    LooseEE   MediumEE  TightEE
std::vector<float> maxSigmaIetaIeta94XV2 = {0.0126,   0.0112,   0.0106,   0.0104,    0.0457,   0.0425,   0.0387,   0.0353};
std::vector<float> maxDEtaIn94XV2        = {0.00463,  0.00377,  0.0032,   0.00255,   0.00814,  0.00674,  0.00632,  0.00501};
std::vector<float> maxDPhiIn94XV2        = {0.148,    0.0884,   0.0547,   0.022,     0.19,     0.169,    0.0394,   0.0236};
std::vector<float> maxHOverE94XV2        = {0.05,     0.05,     0.046,    0.026,     0.05,     0.0441,   0.0275,   0.0188};
std::vector<float> maxHOverE_p1_94XV2    = {1.16,     1.16,     1.16,     1.15,      2.54,     2.54,     2.52,     2.06};
std::vector<float> maxHOverE_p2_94XV2    = {0.0324,   0.0324,   0.0324,   0.0324,    0.183,    0.183,    0.183,    0.183};
std::vector<float> maxOoEmooP94XV2       = {0.209,    0.193,    0.184,    0.159,     0.132,    0.111,    0.0721,   0.0197};
std::vector<float> maxd094XV2            = {0.05,     0.05,     0.05,     0.05,      0.10,     0.10,     0.10,     0.10};
std::vector<float> maxdz94XV2            = {0.10,     0.10,     0.10,     0.10,      0.20,     0.20,     0.20,     0.20};
std::vector<int>   maxMissingHits94XV2   = {2,        1,        1,        1,         3,        1,        1,        1};
std::vector<bool>  convVeto94XV2         = {true,     true,     true,     true,      true,     true,     true,     true};
bool passIDV1(int);
bool passIDV2(int);
void updateTree(TString fName) { 
  cout<<fName<<endl;
  TFile *f = new TFile(fName,"update");
  TTree *T = (TTree*)f->Get("tnpEleIDs/fitter_tree");
  T->SetBranchAddress("event_rho",&event_rho);  
  T->SetBranchAddress("el_sc_abseta",&el_sc_abseta);  
  T->SetBranchAddress("el_sc_e",&el_sc_e);  
  T->SetBranchAddress("el_5x5_sieie",&el_5x5_sieie);  
  T->SetBranchAddress("el_dEtaSeed",&el_dEtaSeed);  
  T->SetBranchAddress("el_dPhiIn",&el_dPhiIn);  
  T->SetBranchAddress("el_hoe",&el_hoe);  
  T->SetBranchAddress("el_1overEminus1overP",&el_1overEminus1overP);  
  T->SetBranchAddress("el_dxy",&el_dxy);  
  T->SetBranchAddress("el_dz",&el_dz);  
  T->SetBranchAddress("el_mHits",&el_mHits);  
  T->SetBranchAddress("passingConvVeto",&passingConvVeto);  
  
  Int_t           passingCutBasedVetoNoIso94XV1;
  Int_t           passingCutBasedLooseNoIso94XV1;
  Int_t           passingCutBasedMediumNoIso94XV1;
  Int_t           passingCutBasedTightNoIso94XV1; 
  Int_t           passingCutBasedVetoNoIso94XV2;
  Int_t           passingCutBasedLooseNoIso94XV2;
  Int_t           passingCutBasedMediumNoIso94XV2;
  Int_t           passingCutBasedTightNoIso94XV2; 

  TBranch        *b_passingCutBasedVetoNoIso94XV1 = T->Branch("passingCutBasedVetoNoIso94XV1",&passingCutBasedVetoNoIso94XV1,"passingCutBasedVetoNoIso94XV1/I");
  TBranch        *b_passingCutBasedLooseNoIso94XV1 = T->Branch("passingCutBasedLooseNoIso94XV1",&passingCutBasedLooseNoIso94XV1,"passingCutBasedLooseNoIso94XV1/I");
  TBranch        *b_passingCutBasedMediumNoIso94XV1 = T->Branch("passingCutBasedMediumNoIso94XV1",&passingCutBasedMediumNoIso94XV1,"passingCutBasedMediumNoIso94XV1/I");
  TBranch        *b_passingCutBasedTightNoIso94XV1 = T->Branch("passingCutBasedTightNoIso94XV1",&passingCutBasedTightNoIso94XV1,"passingCutBasedTightNoIso94XV1/I"); 
  TBranch        *b_passingCutBasedVetoNoIso94XV2 = T->Branch("passingCutBasedVetoNoIso94XV2",&passingCutBasedVetoNoIso94XV2,"passingCutBasedVetoNoIso94XV2/I");
  TBranch        *b_passingCutBasedLooseNoIso94XV2 = T->Branch("passingCutBasedLooseNoIso94XV2",&passingCutBasedLooseNoIso94XV2,"passingCutBasedLooseNoIso94XV2/I");
  TBranch        *b_passingCutBasedMediumNoIso94XV2 = T->Branch("passingCutBasedMediumNoIso94XV2",&passingCutBasedMediumNoIso94XV2,"passingCutBasedMediumNoIso94XV2/I");
  TBranch        *b_passingCutBasedTightNoIso94XV2 = T->Branch("passingCutBasedTightNoIso94XV2",&passingCutBasedTightNoIso94XV2,"passingCutBasedTightNoIso94XV2/I"); 

  T->SetBranchAddress("passingCutBasedVetoNoIso94XV1", &passingCutBasedVetoNoIso94XV1);
  T->SetBranchAddress("passingCutBasedLooseNoIso94XV1", &passingCutBasedLooseNoIso94XV1);
  T->SetBranchAddress("passingCutBasedMediumNoIso94XV1", &passingCutBasedMediumNoIso94XV1);
  T->SetBranchAddress("passingCutBasedTightNoIso94XV1", &passingCutBasedTightNoIso94XV1);
  T->SetBranchAddress("passingCutBasedVetoNoIso94XV2", &passingCutBasedVetoNoIso94XV2);
  T->SetBranchAddress("passingCutBasedLooseNoIso94XV2", &passingCutBasedLooseNoIso94XV2);
  T->SetBranchAddress("passingCutBasedMediumNoIso94XV2", &passingCutBasedMediumNoIso94XV2);
  T->SetBranchAddress("passingCutBasedTightNoIso94XV2", &passingCutBasedTightNoIso94XV2);

  // float el_pt,el_eta; float ptEta;
  // TBranch *bpt = T->Branch("ptEta",&ptEta,"ptEta/F"); 
  // T->SetBranchAddress("el_pt",&el_pt); 
  // T->SetBranchAddress("el_eta",&el_eta);
  Long64_t nentries = T->GetEntries(); 
  for (Long64_t i=0;i<nentries;i++) { 
    T->GetEntry(i);
    //    ptEta = el_pt*el_eta;
    passingCutBasedVetoNoIso94XV1 = passIDV1(0);
    passingCutBasedLooseNoIso94XV1 = passIDV1(1);
    passingCutBasedMediumNoIso94XV1 = passIDV1(2);
    passingCutBasedTightNoIso94XV1 = passIDV1(3);

    passingCutBasedVetoNoIso94XV2 = passIDV2(0);
    passingCutBasedLooseNoIso94XV2 = passIDV2(1);
    passingCutBasedMediumNoIso94XV2 = passIDV2(2);
    passingCutBasedTightNoIso94XV2 = passIDV2(3);

    b_passingCutBasedVetoNoIso94XV1->Fill();
    b_passingCutBasedLooseNoIso94XV1->Fill();
    b_passingCutBasedMediumNoIso94XV1->Fill();
    b_passingCutBasedTightNoIso94XV1->Fill(); 

    b_passingCutBasedVetoNoIso94XV2->Fill();
    b_passingCutBasedLooseNoIso94XV2->Fill();
    b_passingCutBasedMediumNoIso94XV2->Fill();
    b_passingCutBasedTightNoIso94XV2->Fill(); 
    //    bpt->Fill();
  }
  //  T->Print(); 
  //  gDirectory->mkdir("tnpEleIDs");
  gDirectory->cd("tnpEleIDs");
  T->Write(); 
  delete f; 
}

bool passIDV1(int level){
  if(el_sc_abseta <= 1.479) level = level;
  else level = level + 4;

  if(el_5x5_sieie                                 >= maxSigmaIetaIeta94XV1[level]) return false;
  if(abs(el_dEtaSeed)                          >= maxDEtaIn94XV1[level])        return false;
  if(abs(el_dPhiIn) >= maxDPhiIn94XV1[level])                                   return false;
  if(el_hoe >= (maxHOverE94XV1[level] + (maxHOverE_p1_94XV1[level]/el_sc_e) + (maxHOverE_p2_94XV1[level]*event_rho/el_sc_e) )) return false;
  if(abs(el_1overEminus1overP)                 >= maxOoEmooP94XV1[level])       return false;
  if(abs(el_dxy)                                  >= maxd094XV1[level])            return false;
  if(abs(el_dz)                                   >= maxdz94XV1[level])            return false;
  if(el_mHits                               >  maxMissingHits94XV1[level])   return false;
  if(convVeto94XV1[level] != passingConvVeto)                 return false;
  return true;
}

bool passIDV2(int level){
  if(el_sc_abseta <= 1.479) level = level;
  else level = level + 4;

  if(el_5x5_sieie                                 >= maxSigmaIetaIeta94XV2[level]) return false;
  if(abs(el_dEtaSeed)                          >= maxDEtaIn94XV2[level])        return false;
  if(abs(el_dPhiIn) >= maxDPhiIn94XV2[level])                                   return false;
  if(el_hoe >= (maxHOverE94XV2[level] + (maxHOverE_p1_94XV2[level]/el_sc_e) + (maxHOverE_p2_94XV2[level]*event_rho/el_sc_e) )) return false;
  if(abs(el_1overEminus1overP)                 >= maxOoEmooP94XV2[level])       return false;
  if(abs(el_dxy)                                  >= maxd094XV2[level])            return false;
  if(abs(el_dz)                                   >= maxdz94XV2[level])            return false;
  if(el_mHits                               >  maxMissingHits94XV2[level])   return false;
  if(convVeto94XV2[level] != passingConvVeto)                 return false;
  return true;
}

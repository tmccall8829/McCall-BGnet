#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _ampap_reg(void);
extern void _dbsStim_reg(void);
extern void _gabaap_reg(void);
extern void _myions_reg(void);
extern void _pGPeA_reg(void);
extern void _pSTN_reg(void);
extern void _scopRandom_reg(void);
extern void _twoStateGen_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," mod/ampap.mod");
    fprintf(stderr," mod/dbsStim.mod");
    fprintf(stderr," mod/gabaap.mod");
    fprintf(stderr," mod/myions.mod");
    fprintf(stderr," mod/pGPeA.mod");
    fprintf(stderr," mod/pSTN.mod");
    fprintf(stderr," mod/scopRandom.mod");
    fprintf(stderr," mod/twoStateGen.mod");
    fprintf(stderr, "\n");
  }
  _ampap_reg();
  _dbsStim_reg();
  _gabaap_reg();
  _myions_reg();
  _pGPeA_reg();
  _pSTN_reg();
  _scopRandom_reg();
  _twoStateGen_reg();
}

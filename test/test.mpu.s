.hmacro nonameFSM0
LPTO (2f ) @ (KI12);
R0.M[0]->M[0] || Repeat @ (KI13);
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
2:
R0.M[0]->M[0] || LPTO (3f ) @ (KI13);
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
R0.M[0]->M[0];
3:
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
NOP;
.endhmacro

.hmacro nonameFSM1
R0.M[0]->M[0];
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
R0.M[0]->M[0];
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
R0.M[0]->M[0];
T0+T1->M[0];
BIU0.DM->SHU0.T0;
T0>T1->M[0];
NOP;
.endhmacro

.hmacro nonameFSM2
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
.endhmacro

.hmacro main
nonameFSM0 || nonameFSM1 || nonameFSM2;
.endhmacro

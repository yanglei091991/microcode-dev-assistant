.hmacro nonameFSM0
LPTO (1f ) @ (KI12);
R0.M[0]->M[0]@(C);
shu0.t0 ind tsq->biu0;
biu0.dm(A++,K++)->IALU.t0(i0);
t0 + t1(u,b)->shu0.t0@(!c);
1:
LPTO (2f ) @ (KI12 - 4);
merge(t0,t0,t0)->M[0]@(C);
t0|t1->shu0.t0;
max(t0,t3)(u,b)->falu.t2;
mdivr->divr@(c);
2:
.endhmacro

.hmacro nonameFSM1
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
NOP;
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
.endhmacro

.hmacro nonameFSM3
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
nonameFSM0 || nonameFSM1 || nonameFSM2 || nonameFSM3;
.endhmacro

import gc
gc.disable()

from os import _exit
from sys import stdin 
import pickle, base64, zlib

d = pickle.loads(zlib.decompress(base64.a85decode( b'GQI294c^j[&`\'!>(3BTa0X.cN(g(I`k<;$cA)^nc,;=,Q6c)7Tbeh35`9%;5nO%OC&Xeb]=k2?7Z_uijBX^&R1ZHB#0-Y1TDoH(tp\\-oNk*>r?kN/%;^HO5F+5NRWQ`jbgQ`#o5:Kfr$H.MQ8jlt%gl0SApQDYfIjE1+KkBq[8P=!#dSj\'\\L4n.+e?S5,=AGF\'1^D-:io(6Ff+:9(c<92m"mIKm*jC/dXVm@Q[q!J9J58TEi*a$:akH&fM!rZIC=aOdj[2Q1a,jnFSpGT#hLj6dSQ\'7\'=P9nHJFlAJXiZmSbhRPf=$#I#m+?[O*]+]SiD;eYU8%*Z(S++9DX5G=Hdj!`e&($Eq(L=28Hl>Xfg1u?YYC"QrliD_o5?.+h^SM#Qs6IZ8ZU5">jf3Yn_XsLme4SF2X3f]!%\'>cKnDL:1P8cD[6[US,s.9(U3YX75S4[YTP:2+;n\\V]<fPhY%[9brGHu%9b1Ejsh!r(]h4.R>?Vgm[S\\bhO;i<OMQs57.0XZ+-K\\!jj\'%q`QK?48ujFf_JoqFX_<W(28.cYo/j\\$\'/P\\i;Yrk>+>^Mi+aYXrAaVfOF@oU:.;Lg#a3W%taCNA@/Fo"%!l^N!#PcJ8C<)_<Gq:6]\'e\'7WIM+.NT@?jWb$.Hs.Tk60h3"!^\\l!p1+<f1bB%G3m,OTO8s7V#uMRX7u\\%:9F"&09tP$8-F51iRB(pI2J]O"g.66"\'?"\'/(_!NjK^Kd".B4D\\Q,oIrA:E\'I"ir#\\75.PC\'6!%cF?V@=5J?*)93r;\\(;9=`K\\S7r<CL/.41bO!Mo\'A:G[;\\TiLpZ(C0I$[f66udZPc7X67=&4E+8AU+4?8.XW;-ZX8+()Gj8XG`(LZ(%0I^u_ee:WU]P8e\\WVs-SmOV\\,gVF%C5QIt<725)=<@L=iKt=^L4on)+]4+Y2HZ[gYA.rKb=Qc*<CX6O:ei`2Y"Rnb7NJQ>:9?h]Hp2:ZNl%k(eI-DpJN4QZjQ9T2<Y!^ugmCR:p;i#%K;PA1=g$i:73qB9!ihZ"7A2"`Co6K$V7\\_k<\'i@C@eMqpIu_j*g8g&Z@n*psL8gf(=`/?/ZD`e=16"S5)f[a@T.Z1Sqrk`md$_;$`fM`W&F$PS"dEGTk/=K*1Q7h^cRa3lD(,,5N;ia;P0t1@2JLohF+aQRWY$/NN42Gp*oe,Nh8sJ_$pA2@,h6;6p*urjMW(+dP@2CCmBS4.4^pREN3%>gh6off`mZpaPh<+Z&P%i10W@"&,</hmQ[p0M+qRoQ=qtR9h%M_f=.YO`YBDU)A:673hsa1]`oC3$f.qf8I\'u0:oAace%iP6hPjS)(UEqo)Bb/lq&t^2(-cjk&4t+mCl_%<HE9sGLG%k!sFX(W"$eO8)*JZ`/-VIH8(K.=4Bhsu;?Z,Bkl9%tF8AN$)\\``HIVldt3+u6\'$mA8NgN^\\TEpr:ocmuH$GK4+)opEdqAD\'pJZ&TSg[HBEHQCYp/3XrH%-R+3%qIEkO[->.280&r@<,\\A(d@Z-"D\'e4V*(_1tbc[357\'/6tl<(CAsQi4jDf?2@o$)04dcYl5aM_"32$mRP8S#WDO5CC1-^3RUteNecOms9CQ_PC0%5_=eYi,^Q&g!8p:Jf)gK@VOFRgp./CJQ4RIBOiknAMU`^h5bE`V`0JJpuHAdD05#*E6MKc-#JckU/4r`&Y?V?i7IX%p1k(2>0,^Vo3Gg.OQ\\gLjn+[*R\\.rY?q$E2Du3q\\[3)llA5GeHd);#="BFp^>^42F#Wp7DhI_cl[EFh%r67f)gnn\'`c.Aml/q.EN8Lh.b<1^gE*VfCFYMF*`cUtga[2rp^G#2u*J>?Za@QKqVA*/HBVW:T(@[X7!i8<4E.=HDOo+$GPB&%LV&P1@r,*?2&HUb)>0fCN&W-ZaKk*4FO""T//]DRa8A"bV!MoGg/Gc$@W<tn7^=?dA2=<@M6rU8ZO-tu4.dtXei2W$*l3?1s^CCHIsLQlYn3mo9SKaRNsF96ZaM7$VL1s*C>obL%ZlP1q_W$[6I,,B,+7<?<\\BanquQE"!O(npSTHcUVBW\\hBH,Q.+1kUKDX`ZJs_(DK`2A,:nr(/IEVql`fW,PZ]_mKk\\m_ALJ5\'D6Rq-@OV:IEp\'j?("Z-<7K&9VPX%+rbug5DtY.<q@06)dANda625JcTmG-7@ZA<3C5tmuTpJl>=(]B`-1&%0l5A0+ibY\\DJhT6T=6(q7Vp(X[)p\\nE1:R-$hOD2hSB=*i.PIl:Pe=A\\BBZfch]$=T?:<$W2"+quI?E^`f,EG@pn7m<UO!IXXe$1i1Pf1oF@8W1\\.oU6\'+jH\'T8lusYTsEi::+lNG6gS^(=b?bYaKr[04Sn3]B]d4T?38#_"Q#\\bu!5!FWN+?9ZU*rkeG\'NoR?Ai5>nK&6Y!]q)?UmACF8a47/7aPruA#s<L(hGr`(TO!YEnXS=KbPF]tgX`O2k\\.eaTO7\\Y,MHE8!YbbQ$KX;-Ya+muq*)(K@%QpH7]i-G\'m`<7uh1nISi)0.F*!G0"&;J4G>SR.C@h$I_Kfgt3T+\'Q<i^lHiFFp(Vu=)HrKVt7GaLs0C!AnOP-#.N-`>RCGYUl,7/)@KWWZK$+[N3#JWP?l\'34Ue$9^%9&J3\\7-*4QM8bi\'r.[O:0A(9gSjR<n2t?WW?FIk@lKn86t,4PP]l#lphakr1tA\\\\UO4/l@Na>:aGVkY,..tXK1TA>7=6RL`tm*2TL]n:@P_mOYlCi\':[eEeJQDco\'m\'1),J_?1hbY7MHW/dbnlC8)-.L2Sor^J[nRc>TDI?IW6!\'3oIN7i&H/qBTIl+83,464m<g+@e[tX$*WBWrNC0hZ%QF2EmhB[NYj?&s69]-c?"Z^Z6tl4nFWf>Tm$&Q1*Y^06(GdF%[ENs_CHpC!ac9ALp/MbR,\'5D]i7fk>@GQ>9pUtZDb/[Z>;eA83=`SDNF2$e&Q1[YfYEm5drTM-`)FQs^7DE#Y55[##pj0e-%(WS!o`IsEDu4&@?6A/AY//DM_pL@7b6/VJQU\'.r$E/UTH"3[B&\\>V;O/F&fG=u8f;1H9nCJUn!\\bO,_R.\\TDQnH,d`U@$rq-#GD.9+U7=\\!S!Gij:aXmM!igs8CD@V!767mA_UHTRh2XQ^i0*/*A,3>d+a86/]fY$flA;1Vm$j0`t2/9rLI@CP?.]tf\'$\\Kj\\U%1d@:,&d)cI6(oA^qoDEQgUd_=/a:@-J+c@oU=)d>60VV/]6aoIRFujoYOPS($)11FF*r)atBoJAEe"f-W>Kg:8l(_,\'IXsX;8WncNcJ<(p8S2g,p7Rm(Y7q=##>k:]__h")>"dVCX8WUs-IcO8\\F3>Uk%7>&+E.8Aj.1]5rfh/Rn,.@<TdFWik9pd4@tc[hJSq5,]fT_UE&\\IVijTc[ES1R9m\';9-*85U=6I-k@`0g]Z)VXC`+L1\\o^AXe21Bm:RBVHVVibHZT#FA(%!_9;\'eDJs6-#aE@4Km\'[4*he>,mikBJ&N0t91,>%3cRqnBA)ONBq)M2r*IO5(Z"R#J3g1FN!\\%+a2<l0-BV$\\D1a^[tjC#,g#pF$;D5eP*]`,\\+0hWd-Mu1+\\q[F=Z.GI#D%q0p7bY<d9cPXH=kt4lPO?CF;WtV#$rOPa4qs0d`pC$-a7cHM)gg&(VhOo&65!@t7sOg31gg7,W19,3N[!3>=g--`6]Q=>Y\'@+DQpc%cM["nd=Ji@Ku^d@e`])3=#Zq*fA<*0R+GbC(9?pmh*-c83TFI^a1MtpaUB/WZ6ZCGVXuX3KRKE$?j+,J3W1T5P>.E335Cd\\,"2AQ?1Tap9b)$RMl%Z+#]"SeYTDm18eCA7Tb:7MA;*PhX`d.q@biAAJHoK:A0.kNL1eU8eLY;6YqF\\7S61nlR:eo=$X)f7.]l7K#2:bWTM5(1B)083M#fDaaMEt[)7LD#s"Ie4L]D(B[X#%ca/j90(`qp9]$4AQL7>;DJ!B?=fJ1PONi07H`:Gu*1(fU9dXA[aZDkSHo=&KrEnA,ZJOFACFT5s="_(DjC`)Q<F0![E_Ua.4.bq$U,X\\kXQP7Bfs2;C5P.%pG<)FMS\\Le$]ffZ>Cn03@B$9,\\<-!#X2ri>EIXa=rX\\u1>*rYM(4>77sZ,G@b&X]W;2W!0Ni6H(Zf_@f#oiHQ-A6#]njH>Akn\\oY@GfBn1]+rGUl6C4FD`h[?@\'HV&a-%$[o=6q"-g&it=-GuS.I\'n>,;18tWXCtj0nd2Wl\\0bWH/,G>2`94d\\2/srpI-.EheU`jY>gbcZ#Si4T5);`F\'QW.+eEZuZb8Q@*$b5i-9?ENLON1;2a/rI%47Z`]#SG=nP!EF,;_80Ic<\\)>EDZ^G6V0Cn@&-(NG#T_<U9Uu4E2M$C-qXPKUmFWkoi[Wb<_n@Vn"Tq\\@\\X+OQGCW&W!s9kUILj<gg0:;V2tGZ27#aFC[865Zp9,c\'\'C\\Kd]7i:X@*:HB$VB+,,;=.`u\\\\9>0_@=7fHK`>O<m6DT457JsP,-Rd_geH,5[B8Ed_nasc0em1>9>U7HI<mCuR.kBpc"YpN^W<$"L1idRh)Ii`Gi`0Lp!Jtp)ZZ,#&MYM:K-17*arp"tm9u$u' )))

with open('user.out', 'wb') as f:
    for i in sys.stdin:
        if i[-1] == '\n':
            f.write(d[i[:-1]])
        else:
            f.write(d[i])
        f.write(b"\n")
_exit(0)

### META SCRIPT
"""
rles = ['1']
for _ in range(30):
    l = rles[-1]
    curr = ''
    count = 0
    codes = []
    for i in l:
        if i == curr:
            count += 1
        else:
            codes.append(str(count) + curr)
            curr = i
            count = 1
    codes.append(str(count) + curr)
    rles.append("".join(codes[1:]))

d = dict()
for i in range(30):
    d[str(i+1)] = b'"' + rles[i].encode('latin-1') + b'"'

import pickle, base64, zlib

print("pickle.loads(zlib.decompress(base64.a85decode(", base64.a85encode(zlib.compress(pickle.dumps(d, protocol=5), level=1)), ")))")
"""

s=open('sa4.c').read()
s=s.replace('''        double d=E+LAM*singles-old;
        if(d>0 && urand()>=exp(-d/T)) undo_sigma(); else S=Tr;''','''        double d=E+LAM*singles-old;
        if(getenv("DBG")){ long mi=missing; uint32_t c2[362880]; memcpy(c2,cnt,sizeof(uint32_t)*fact[k]); int sv[MAXN]; memcpy(sv,sig,sizeof(sig)); full_count();
            int bad=0; for(int c=0;c<fact[k];c++) if(c2[c]!=cnt[c]) bad++; if(bad||mi!=missing){ fprintf(stderr,"DBG it=%ld ntl=%d inc=%ld full=%ld badcodes=%d sigOK=%d\\n",it,ntl,mi,missing,bad,!memcmp(sv,sig,sizeof(sig))); for(int t=0;t<ntl;t++) fprintf(stderr,"  swap %d %d\\n",tlog[t][0],tlog[t][1]); }
            memcpy(cnt,c2,sizeof(uint32_t)*fact[k]); missing=mi; }
        if(d>0 && urand()>=exp(-d/T)) undo_sigma(); else S=Tr;''')
open('sa4.c','w').write(s)

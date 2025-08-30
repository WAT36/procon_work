class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        for i in range(len(s)):
            if i>=3:
                break
            inum=s[:i+1]
            if (inum!='0' and inum[0]=='0') or int(inum) >= 256:
                continue

            for j in range(i+1,len(s)):
                if j-i>3:
                    break
                jnum=s[i+1:j+1]
                if (jnum!='0' and jnum[0]=='0') or int(jnum) >= 256:
                    continue

                for k in range(j+1,len(s)):
                    if k-j>3:
                        break
                    knum=s[j+1:k+1]
                    if (knum!='0' and knum[0]=='0') or int(knum) >= 256:
                        continue

                    for l in range(k+1,len(s)):
                        if l-k>3:
                            break
                        lnum=s[k+1:]
                        if (lnum!='0' and lnum[0]=='0') or len(lnum) > 3 or int(lnum) >= 256:
                            continue
                        #print(inum+'.'+jnum+'.'+knum+'.'+lnum)
                        ans.append(inum+'.'+jnum+'.'+knum+'.'+lnum)
        return list(set(ans))
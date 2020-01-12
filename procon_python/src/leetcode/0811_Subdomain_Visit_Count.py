class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        domain={}
        for cpd in cpdomains:
            c,d=cpd.split()

            cofd=domain.get(d,0)
            domain[d]=cofd+int(c)
            dotind=d.find('.')
            while(dotind != -1):
                subdomain=d[dotind+1:]

                cofd=domain.get(subdomain,0)
                domain[subdomain]=cofd+int(c)
                dotind=d.find('.',dotind+1)

        ans=[]
        dictlist=domain.items()
        for di in dictlist:
            ans.append(str(di[1])+" "+str(di[0]))
        return ans
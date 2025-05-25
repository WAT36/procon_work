class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        address=[]
        for e in emails:
            local,domain=e.split("@")
            local=local.replace(".","")
            plusind=local.find("+")
            if(plusind!=-1):
                local=local[:plusind]
            address.append(local+"@"+domain)
        return len(set(address))

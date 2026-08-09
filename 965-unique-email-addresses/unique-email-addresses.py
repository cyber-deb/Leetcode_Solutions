class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for i in emails:
            k=i.split("@")
            k[0]=k[0].replace('.','')
            if '+' in k[0]:
                k[0]=k[0][:k[0].index('+')]
            s.add('@'.join(k))
        return len(s)
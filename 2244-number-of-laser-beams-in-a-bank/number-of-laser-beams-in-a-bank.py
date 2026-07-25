class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev,beam=0,0
        for i in bank:
            curr=i.count('1')
            if curr:
                beam+=prev*curr
                prev=curr
        return beam

        
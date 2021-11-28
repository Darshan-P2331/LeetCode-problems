class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split(' ')
        return ' '.join([i[::-1] for i in x])
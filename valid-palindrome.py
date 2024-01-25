# using lists
valids = "abcdefghijklmnopqrstuvwxyz01234567890"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [i for i in s.lower() if i in valids]
        return l == l[::-1]

# using maketrans
table = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM", "qwertyuiopasdfghjklzxcvbnm", " !@#$%^&*(){`?}[]:;',._+=--/\"\\'")
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(table)
        return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

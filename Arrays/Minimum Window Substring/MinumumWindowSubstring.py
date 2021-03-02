# have a dict to store the t elements and a counter to check the number of elements remaining.
def minWindow(self, s: str, t: str) -> str:
   if len(t) > len(s):
        return ""
    d = defaultdict(int)
    curmin = 2**31
    st = ""
    for x in t:
        d[x] += 1
    total = len(d)
    start = 0
    for end in range(len(s)):
        if s[end] in d:
            if d[s[end]] >= 1:
                d[s[end]] -= 1
                if d[s[end]] <= 0:
                    total -= 1
            else:
                d[s[end]] -= 1
        while total == 0:
            if end-start < curmin:
                curmin = end-start
                st = s[start:end+1]
            if s[start] in d and d[s[start]] == 0:
                total += 1
                d[s[start]] += 1
                start += 1
            elif s[start] in d and d[s[start]] < 0:
                d[s[start]] += 1
                start += 1
            else:
                start += 1
    return st


#         A = 0
#         B = 0
#         C = 0
#         total = 0

#         ADOBECODEBANC
#         1    1
#         start end

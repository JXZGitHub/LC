class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Time:  O(3^4) #Each bucket is 3 digits, and there are 4 buckets. So each try of 3 digit needs to go down 4 times to the end.
        Space: Heap O(1). Stack O(1)

        Definition of valid IP address:
        1. The length of the ip without '.' should be equal to the length of s;
        2. The digit order of ip should be same as the digit order of s;
        3. Each part separated by the '.' should not start with '0' except only '0';
        4. Each part separared by the '.' should not larger than 255;
        """
        res = []
        self.recurse(0, 4, [], s, res)
        return res

    def recurse(self, start, bucket, output, s, res):
        if bucket == 0 and start > len(s) - 1:
            res.append(''.join(output))
        elif bucket > 0:
            for i in range(1, 4):
                if start+i <= len(s):
                    item = s[start:start + i]
                    if int(item) <= 255 and not (len(item) > 1 and item.startswith('0')):
                        output.append(item)
                        if bucket > 1:
                            output.append('.')
                        self.recurse(start + i, bucket - 1, output, s, res)
                        output.pop()
                        if bucket > 1:
                            output.pop()

sol = Solution()
print (sol.restoreIpAddresses("123456"))
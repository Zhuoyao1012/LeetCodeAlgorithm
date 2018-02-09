def expandAroundCenter(s, left, right):
    while (left >= 0) & (right < len(s)):
        if  (s[left] == s[right]):
            left -=1
            right +=1
        else:
            break
    return right - 1 , left + 1
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        start = 0
        end = 0
        for i, x in enumerate(s):
            print(i)
            right1, left1 = expandAroundCenter(s,i,i)
            right2, left2 = expandAroundCenter(s,i,(i+1))
            len1 = right1 - left1 + 1
            len2 = right2 - left2 + 1
            if len1 > len2:
                length = len1
                right = right1
                left = left1
            else:
                length = len2
                right = right2
                left = left2
            if(length > (end - start)):
                start = left
                end = right
        return s[start:end+1]

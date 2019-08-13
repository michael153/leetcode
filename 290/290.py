class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s = {}
        s2p = {}
        components = str.split(" ")
        if len(pattern) != len(components):
            return False
        for i, letter in enumerate(pattern):
            component = components[i]
            if letter in p2s and component != p2s[letter]:
                return False
            if component in s2p and letter != s2p[component]:
                return False
            p2s[letter] = component
            s2p[component] = letter
        return True

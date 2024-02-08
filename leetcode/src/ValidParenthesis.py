class Solution:
    def ValidParenthesis(s: str) -> bool:
        for i in range(0, (len(s)-1)):
            if ((s[i]) == '(' and (s[i + 1] != ')')):
                return False
            if ((s[i]) == '[' and (s[i + 1] != ']')):
                return False
            if ((s[i]) == '{' and (s[i + 1] != '}')):
                return False

        else:
            return True

    s = "(]"
    print(ValidParenthesis(s))


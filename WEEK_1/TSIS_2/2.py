class Solution:
    def interpret(self, command: str) -> str:
        a = command.replace("()", "o")
        a = a.replace("(al)", "al")
        return a
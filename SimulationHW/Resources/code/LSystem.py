class LSystem:
    def __init__(self, productions_dict):
        self.productions_dict = productions_dict;

    def generate_word(self, iters, omega):
        word = omega
        for i in range(iters):
            word = self.rewrite(word)
        return word

    def rewrite(self, word):
        new = ""
        for c in word:
            if c in self.productions_dict:
                new = new + self.productions_dict[c]
            else:
                new = new + c
        return new

if __name__ == '__main__':
    system = LSystem({'F':'G[-F]G[+F]F', 'G':'GG'})
    print system.generate_word(2, 'F')
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if ''.join(sorted(word)) == self.sorted_word]


if __name__ == "__main__":
    anagram = Anagram('listen')
    possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
    print(anagram.match(possible_anagrams))  

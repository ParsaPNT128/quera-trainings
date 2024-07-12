import itertools

dictionary  = []
length = 0

def find_character(n):
    if 1<=n<=100:
        n -= 1
        word = dictionary[n]
        character = word[len(word) - 1]
        return character
    else:
        return 'Index should be between 1 and 100.'

run = True
while run:
    length += 1
    for x in itertools.product(['a','b'],repeat=length):
        if len(dictionary) != 100:
            string = ''
            for i in x:
                string += i
            dictionary.append(string)
        else:
            run = False

'''dictionary = ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb', 'aaaa', 'aaab', 'aaba', 'aabb',
 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb', 'aaaaa', 'aaaab', 'aaaba',
 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa',
 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab', 'bbaba', 'bbabb', 'bbbaa', 'bbbab', 'bbbba',
 'bbbbb', 'aaaaaa', 'aaaaab', 'aaaaba', 'aaaabb', 'aaabaa', 'aaabab', 'aaabba', 'aaabbb', 'aabaaa', 'aabaab', 'aababa', 'aababb',
 'aabbaa', 'aabbab', 'aabbba', 'aabbbb', 'abaaaa', 'abaaab', 'abaaba', 'abaabb', 'ababaa', 'ababab', 'ababba', 'ababbb', 'abbaaa',
 'abbaab', 'abbaba', 'abbabb', 'abbbaa', 'abbbab', 'abbbba', 'abbbbb', 'baaaaa', 'baaaab', 'baaaba', 'baaabb', 'baabaa', 'baabab']'''

n = int(input())
print(find_character(n))
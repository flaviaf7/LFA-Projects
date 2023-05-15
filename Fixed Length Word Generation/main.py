grammar = [
    'S -> aA|dE',
    'A -> aB|aS',
    'B -> bC',
    'C -> bD|bB',
    'D -> cD|λ',
    'E -> λ'
]

def get_number_of_lower(word):
    return sum(1 for symbol in word if symbol.islower())

def generate_successors(grammar, word):
    successors = ['']
    for symbol in word:
        if symbol.isupper():
            new_list = []
            for successor in successors:
                for new_word in grammar[symbol]:
                    new_list.append(successor + new_word)
            successors = new_list
        else:
            for i in range(len(successors)):
                successors[i] += symbol
    return successors

def generate_words(grammar, length, start_state):
    new_grammar = {}
    for line in grammar:
        state, productions = line.split('->')
        state = state.strip()
        values = [x.strip() if x.strip() != "λ" else "" for x in productions.split('|')]
        new_grammar[state] = values

    words = new_grammar[start_state].copy()
    while len(words) > 0:
        current_word = words.pop(0)
        if not current_word.islower() and get_number_of_lower(current_word) <= length:
            words.extend(generate_successors(new_grammar, current_word))
        elif len(current_word) == length:
            print(current_word)


generate_words(grammar, 8, "S")

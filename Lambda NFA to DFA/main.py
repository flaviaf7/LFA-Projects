class NFA:
    def __init__(self, states, alphabet, start_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.alphabet.append('lambda')
        self.start_state = start_state
        self.final_states = final_states
        self.transitions = transitions
        self.states_dict = {}
        for i in range(len(self.states)):
            self.states_dict[self.states[i]] = i
        self.alphabet_dict = {}
        for i in range(len(self.alphabet)):
            self.alphabet_dict[self.alphabet[i]] = i

        self.transitions_table = {}
        for state in self.states:
            for symbol in self.alphabet:
                key = (state, symbol)
                self.transitions_table[key] = []
        for transition in self.transitions:
            from_state, symbol, to_state = transition
            key = (from_state, symbol)
            self.transitions_table[key].append(to_state)

    def calculateLambdaClosure(self, state):
        closure = {state: 0}
        cls = [state]
        while len(cls)>0:
            current = cls.pop()
            for x in self.transitions_table[(str(current),'lambda')]:
                if x not in closure.keys():
                    closure[x] = 0
                    cls.append(x)
                closure[current] = 1
        return closure.keys()

    def __repr__(self):
        return 'Q: ' + str(self.states) + '\nSigma: ' + str(self.alphabet) + '\nq0: ' +\
               self.start_state + '\nF: ' + str(self.final_states) + '\nTabel tranzitii: \n'\
               + str(self.transitions_table)

class DFA:
    def __init__(self, nfa):
        self.alphabet = nfa.alphabet[:-1]
        self.states = []
        self.start_state = frozenset(nfa.calculateLambdaClosure(nfa.start_state))
        self.final_states = []
        self.transitions = {}

        epsilon_closures = {}
        for state in nfa.states:
            epsilon_closures[state] = nfa.calculateLambdaClosure(state)

        self.states.append(self.start_state)
        unmarked_states = [self.start_state]

        while unmarked_states:
            current_state = unmarked_states.pop(0)
            for symbol in self.alphabet:
                next_state = set()
                for nfa_state in current_state:
                    for transition_state in nfa.transitions_table.get((nfa_state, symbol), []):
                        next_state.update(epsilon_closures[transition_state])
                if next_state:
                    if next_state not in self.states:
                        self.states.append(next_state)
                        unmarked_states.append(next_state)

                    current_state_key = ''.join(sorted(list(current_state)))
                    current_state_key = current_state_key[0] + current_state_key[1::2]
                    next_state_key = ''.join(sorted(list(next_state)))
                    next_state_key = next_state_key[0] + next_state_key[1::2]
                    self.transitions[(current_state_key, symbol)] = next_state_key

        for state in self.states:
            for final_state in nfa.final_states:
                if final_state in state:
                    self.final_states.append(state)
                    break

        for i, state in enumerate(self.states):
            new_state = ''.join(sorted(list(state)))
            self.states[i] = new_state[0] + new_state[1::2]
        
        for i, state in enumerate(self.final_states):
            new_state = ''.join(sorted(list(state)))
            self.final_states[i] = new_state[0] + new_state[1::2]

        self.start_state = ''.join(sorted(self.start_state))
        self.start_state = self.start_state[0] + self.start_state[1::2]

    def __repr__(self):
        return 'Q: ' + str(self.states) + '\nSigma: ' + str(self.alphabet) +\
                '\nq0: ' + str(self.start_state) + '\nF: ' + str(self.final_states) +\
                '\nTabel tranzitii: \n' + str(self.transitions)


# nfa = NFA(
#     ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'],
#     ['a', 'b'],
#     'q0',
#     ['q2','q6'],
#     [['q0', 'a', 'q0'], ['q0', 'a', 'q1'], ['q0', 'b', 'q2'],
#      ['q0', 'lambda', 'q2'], ['q0', 'lambda', 'q3'], ['q1', 'lambda', 'q2'],
#      ['q2', 'a', 'q3'],['q2', 'lambda', 'q4'],['q3', 'a', 'q6'],['q3', 'b', 'q6'],
#      ['q3', 'lambda', 'q5'],['q3', 'b', 'q3'],['q4', 'a', 'q6'],['q4', 'b', 'q5'],
#      ['q4', 'lambda', 'q6'],['q5', 'a', 'q6'],['q5', 'b', 'q2'],['q5', 'lambda', 'q6'],
#      ['q5', 'lambda', 'q2'],['q6', 'b', 'q6']]
# )

f = open('Lambda NFA to DFA/input.txt', 'r')
nfa = []
s = f.readline()

while s!='':
    nfa.append(s.strip().split(' '))
    s = f.readline()

nfa[2] = nfa[2][0]
nfa = nfa[0:4] + [nfa[4:]]

dfa = DFA(NFA(*nfa))
print(dfa)
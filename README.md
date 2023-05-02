# Limbaje Formale si Automate (LFA) - Projects :slightly_smiling_face:

This repository contains all of the projects I developed for the "Limbaje Formale si Automate" (Formal Languages and Automata) course I took during my First year 
of Computer Science studies at the Faculty of Mathematics and Computer Science, University of Bucharest.

The purpose of this repository is to showcase the skills and knowledge acquired during this course.

## Projects list :nerd_face: 	


* Deterministic Finite Automaton (DFA) & Non-Deterministic Finite Automaton (NFA)
    * DFA:
      * The provided Python script (dfa.py) implements a deterministic finite automaton (DFA) and uses it to check if a given input string is accepted by the automaton.
      * The script takes as input a DFA specified in a text file (input file format is in the DFA_input.txt file), and prompts the user to enter an input string. 
        The script then uses the DFA to check whether the input string is accepted by the automaton. 
      * If the input string is accepted by the DFA, the script prints the sequence of states that the DFA goes through to process the input string,
        as well as a message indicating that the input string is accepted. Otherwise, it prints a message indicating that the input string is not accepted by the DFA.
      * The DFA implementation in the script uses a loop to traverse the state space and process the input string.
      
      
    * NFA:
      * The provided Python script (nfa.py) implements a non-deterministic finite automaton (NFA) and uses it to check if a given input string is accepted by the automaton.
      * The script takes as input an NFA specified in a text file (input file format is in the NFA_input.txt file), and prompts the user to enter an input string.
        The script then uses the NFA to check whether the input string is accepted by the automaton.
      * If the input string is accepted by the NFA, the script prints all possible paths (i.e., sequences of states) that lead to an accepting state.
        Otherwise, it prints a message indicating that the input string is not accepted by the NFA.
      * The NFA implementation in the script uses recursion to traverse the state space and check all possible paths through the automaton.

* Lambda Non-Deterministic Finite Automata to Deterministic Finite Automata
    * This project is a tool for converting a Lambda Non-Deterministic Finite Automata (Lambda-NFA) with lambda transitions to a Deterministic Finite Automata (DFA).
    * This project defines two classes, NFA and DFA. The NFA class includes methods for calculating lambda closures and representing the automaton, while the DFA class converts an NFA to a DFA and also provides a string representation of the DFA. An example NFA is included in the code, and the program reads in input for creating an NFA from a file (input.txt).
    
    * An example of an input file:
      ```
      q0 q1 q2 q3 q4 q5 q6
      a b
      q0
      q2 q6
      q0 a q0
      q0 a q1
      q0 b q2
      q0 lambda q2
      q0 lambda q3
      q1 lambda q2
      q2 a q3
      q2 lambda q4
      q3 a q6
      q3 b q6
      q3 lambda q5
      q3 b q3
      q4 a q6
      q4 b q5
      q4 lambda q6
      q5 a q6
      q5 b q2
      q5 lambda q6
      q5 lambda q2
      q6 b q6
      ```
      Explanation of each line:

      - The 1st line lists all the states of the finite automata, separated by spaces.
      - The 2nd line lists all the input symbols that the finite automata can read, separated by spaces.
      - The 3rd line indicates the initial state of the finite automata.
      - The 4th line lists the final (or accepting) states of the finite automata, separated by spaces.
      - The rest of the lines represents the transitions of the finite automata.
    
Each project has its own directory in the repository, with code implementation.

# Contributors :raised_hand_with_fingers_splayed: 	
* Fota Stefania-Flavia

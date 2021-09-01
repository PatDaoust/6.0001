# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here
    '''
    permutations_of_sequence = []
    #define base case
    if len(sequence) == 0:
        permutations_of_sequence += [""]
    if len(sequence) == 1:
        #make sure this doesn't fuck with permutations_of_sequence
        permutations_of_sequence += sequence
    
    #define recursive behaviour
    #for sequence of len(n), case is sequence[0] and sequence[1:n] 
        #store concatenated stings in permutations_of_sequance
        
    if len(sequence) > 1: 
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]
        
        #find recursions of cutdown_sequence
        if len(cutdown_sequence) > 1: 
            permutations_of_cutdown_sequence = get_permutations(sequence[1:])
                
        #add first_char_sequence to all recursions of cutdown_sequence with this
        #modify with permutations_of_cutdown_sequence 
        #loop over each item in permutations_of_cutdown_sequence then this 
        for i in range(len(cutdown_sequence)+1):
             holding_string = cutdown_sequence[:i] + first_char_sequence + cutdown_sequence[i:]
             permutations_of_sequence += [holding_string]
        
        """
        #for "abc" -->["abc", "bac", "bca"]
        #use recursion to add "a" to "cb" (not just "bc")
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]
        #concatenate sequence[0] along each position of sequence[1:n] 
        for i in range(len(cutdown_sequence)+1):
            holding_string = cutdown_sequence[:i] + first_char_sequence + cutdown_sequence[i:]
            permutations_of_sequence += [holding_string]
            
        if needed, torecursively call subset of sequence w/o 1st character:
            #get_permutations(sequence[1:n])
            """
        
    return permutations_of_sequence

    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here


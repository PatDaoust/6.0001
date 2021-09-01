# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Pat
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

#modify VOWELS to include *? probably not
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

#a dictionary
SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    #convert to lowercase 
    word= str.lower(word)
    #calculate word score
    handvalue= 0 
    for char in word:
        #CHECK THIS AFFTER worddict WORKS
        charvalue= SCRABBLE_LETTER_VALUES[char]
        handvalue += charvalue
    comp1= handvalue
    comp2a = (7 * len(word)) - (3 * (n-len(word)))
    if 1 >= comp2a:
        comp2 = 1
    else:    
        comp2= comp2a
    score =  comp1 * comp2
    return score 


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    #mod to distribure a * instead of one of the vowels
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) -1 
    hand["*"] = 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word_list = load_words()
    new_hand = hand.copy()
    #convert to lowercase 
    word= str.lower(word)
    #make list of shared elements
    shared_ele= ""
    for ele in word: 
        if ele in hand:
            shared_ele += ele  
    #modify hand, test if valid move
    for char in word:
        if char in new_hand:
            new_hand[char] -= 1  
            #take used element out of test_hand
            if new_hand[char] <= 0:
                del(new_hand[char])    
    if sorted(shared_ele) == sorted(word):
        if word not in word_list:
            print("Oops! That's not a recognised word. You have been penalised.")
    else:
        print("Oops! You don't have those letters. You have been penalised")
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    test_hand = hand.copy()
    #convert to lowercase 
    test_word= str.lower(word)
    #make list of shared elements
    shared_ele= ""
    for ele in test_word: 
        if ele in test_hand:
            shared_ele += ele  
            test_hand[ele] -= 1 
            #take used element out of test_hand
            if test_hand[ele] <= 0:
                del(test_hand[ele])               
    if sorted(shared_ele) == sorted(test_word):
        if test_word in word_list:
            bool = True   
        else:  
            #* modifications
            if (test_word.find("*")) != -1:
                mod_test_word = word
                #substitute * with each char of VOWELS
                for char in VOWELS:
                    mod_test_word = test_word.replace("*", char)
                    if mod_test_word in word_list:
                        bool = True 
                        if bool == True:
                            break
                    else:
                        bool = False
            else:
                bool = False        
    else:
        bool = False
    return bool

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    test_hand = hand.copy()
    for ele in hand:
        if hand[ele] <= 0:
            del(test_hand[ele])           
    return len(test_hand)  
           
    

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    #initialize hand
    hand_score = 0 
    while bool(hand) == True:
        hand_print = ""
        for key in hand: 
            hand_print += (key + " ") * hand[key]    
        #playtime   
        # Display the hand
        print("Current Hand: %s" %hand_print)
        print("Enter word, or '!!' to indicate that you are finished:")
        # Ask user for input
        word = input()
        # If the input is two exclamation points: End the game (break out of the loop)
        if word == "!!":
            print("You indicated that you are finished. Total score: %d points" %hand_score)
            return hand_score
        # Otherwise (the input is not two exclamation points):
        #if word is valid    
        if is_valid_word(word, hand, word_list):  
            hand = update_hand(hand, word)
            n = calculate_handlen(hand)
            word_score = get_word_score(word, n)
            hand_score = hand_score + word_score
            print("'%s' earned %d points. Total: %d points" %(word, word_score, hand_score))
        #if word is not valid  
        else:
            hand = update_hand(hand, word)
            n = calculate_handlen(hand)
            print("That is not a valid word. Please choose another word.")
    #end of hand.  Return the total score as result of function   
    print("Ran out of letters. Total score: %d points" %hand_score)
    return hand_score
               


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: new_hand a dictionary (string -> int)
    """
    new_hand = hand.copy()
    #check if selected letter key exists in hand
    #if key doesnt exist
    if letter not in hand:
        print("Oops! That letter is not in your hand. Your hand has been returned to you")
        return hand
    #if key exists        
    else:
        letter_value = hand[letter] 
        del(new_hand[letter])    
        #make string possible_subs of VOWELS + CONSONENTS - the original hand keys
        posible_subs = VOWELS + CONSONANTS 
        for key in hand:
            posible_subs = posible_subs.replace(key,"")
        #pick random sub char from possible_subs
        sub = random.choice(posible_subs)
        #add sub to new_hand with stored value
        new_hand[sub] = letter_value
        return new_hand
     
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    #main gameplay
    #ask user for desired # of hands
        #hand_num
    "Enter total number of hands:"
    #total_score = sum of hand_score 
    
    #for each hand
        #offer to substitute_hand, can use exactly once
            #has_sub = False
            #if run substitute_hand(hand, letter) 
                #has_sub=True
            #if has_sub=False 
                #ask if run substitute_hand(hand, letter)
                
        #store hand variables so can replay if needed  
        
        #run play_hand(hand, word_list)    
        
        #offer replay hand, , can use exactly once
            ##reuse substitute_hand code to keep tract of if hand had been replayed
            #if no, move onto next hand (out of loop)
            #if yes, 
                #store hand_score 1
                #replay hand
                #store hand_score 2
                #add higher of hand_score 1 or hand_score 2 to total_score
                
     #after hand_num number of hands
        #print "Total score over all hands:"
        #print total_score            
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

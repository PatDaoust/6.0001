# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        valid_words = []
        text_list =  list(text.split(" "))
        for word in text_list:
             if is_word(load_words(WORDLIST_FILENAME), word):
                 valid_words += [word]
        self.valid_words = valid_words
        
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return list.copy(self.valid_words)
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        base_dict = {"a":1, "b":"b","c":"c", "d":"d", "e":5, "f":"f", "g":"g", "h":"h", "i":"i", "j":"j", "k":"k","l":"l","m":"m","n":"n","o":15,"p":"p","q":"q","r":"r","s":"s","t":"t","u":21,"v":"v","w":"w","x":"x","y":"y","z":"z", "A":1, "B":"B","C":"C", "D":"D", "E":"E", "F":"F", "G":"G", "H":"H", "I":9, "J":"J", "K":"K","L":"L","M":"M","N":"N","O":15,"P":"P","Q":"Q","R":"R","S":"S","T":"T","U":21,"V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}    
        #build transpose_dict off of vowels_permutation
        transpose_dict = base_dict.copy()
        transpose_dict["a"] = vowels_permutation[0].lower()
        transpose_dict["e"] = vowels_permutation[1].lower()
        transpose_dict["i"] = vowels_permutation[2].lower()
        transpose_dict["o"] = vowels_permutation[3].lower()
        transpose_dict["u"] = vowels_permutation[4].lower()
        transpose_dict["A"] = vowels_permutation[0].upper()
        transpose_dict["E"] = vowels_permutation[1].upper()
        transpose_dict["I"] = vowels_permutation[2].upper()
        transpose_dict["O"] = vowels_permutation[3].upper()
        transpose_dict["U"] = vowels_permutation[4].upper()
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        #build_transpose_dict called in function call
        transposed_message = ""
        for char in self.get_message_text():
            if char in transpose_dict:
                transposed_message += transpose_dict[char]
            else:
                transposed_message += char
        return transposed_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #inherits:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        word_list = load_words(WORDLIST_FILENAME)
        transposed_message = self.get_message_text()
        possible_permutations_list = get_permutations("aeiou")
        #possible_decryption_dict keys are elements of possible_permutations_list, values are tuple (possible_decryption_string, len(valid_words_of_message_text_decrypted_list) ) for respective element of possible_permutations_list
        possible_decryption_dict = {}
        for elem in possible_permutations_list:
            possible_decryption_string = self.apply_transpose(self.build_transpose_dict(elem))
            possible_decryption_list = possible_decryption_string.split(" ")
            valid_words_of_possible_decryption_list = []
            for word in possible_decryption_list:
                if is_word(word_list, word):
                     valid_words_of_possible_decryption_list += [word]     
            possible_decryption_dict[elem] = (possible_decryption_string, len(valid_words_of_possible_decryption_list)) 

        lenghts_of_valid_words_of_possible_decryption_list = []
        for key in possible_decryption_dict:
            lenghts_of_valid_words_of_possible_decryption_list += [possible_decryption_dict.get(key)[1]]
        max_lenght_valid_words = max(lenghts_of_valid_words_of_possible_decryption_list)
        #if max() is tied, will return the first maximal result
        if max_lenght_valid_words == 0:
            decrypted_transposed_message = transposed_message
        else:
            permutation_at_max_lenght_valid_words_temp = [key for key, value in possible_decryption_dict.items() if value[1] == max_lenght_valid_words]
            permutation_at_max_lenght_valid_words = permutation_at_max_lenght_valid_words_temp[0]
            message_at_max_lenght_valid_words = self.apply_transpose(self.build_transpose_dict(permutation_at_max_lenght_valid_words))
            decrypted_transposed_message = message_at_max_lenght_valid_words
        return decrypted_transposed_message
    

if __name__ == '__main__':

    # Example test case
    message1 = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message1.build_transpose_dict(permutation)
    print("Original message:", message1.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message1.apply_transpose(enc_dict))
    enc_message1 = EncryptedSubMessage(message1.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message1.decrypt_message())
    print("-----------------------")
    
    message2 = SubMessage("Kittens are purrfect!")
    permutation = "aoiue"
    enc_dict = message2.build_transpose_dict(permutation)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Kittons aro perrfoct!")
    print("Actual encryption:", message2.apply_transpose(enc_dict))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message2.decrypt_message())
    print("-----------------------")
    

     
    #TODO: WRITE YOUR TEST CASES HERE


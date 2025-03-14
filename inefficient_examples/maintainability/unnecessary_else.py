# HumanEval/134 by CodeGemma-7B
# the else statement is unnecessary as it is preceded by return 



def check_if_last_char_is_a_letter(txt):
        '''
        Create a function that returns True if the last character
        of a given string is an alphabetical character and is not
        a part of a word, and False otherwise.
        Note: "word" is a group of characters separated by space.

        Examples:
        check_if_last_char_is_a_letter("apple pie") ➞ False
        check_if_last_char_is_a_letter("apple pi e") ➞ True
        check_if_last_char_is_a_letter("apple pi e ") ➞ False
        check_if_last_char_is_a_letter("") ➞ False 
        '''
        if txt == "":
                return False
        else:
                if txt[-1].isalpha() and txt[-1] != " ":
                        return True
                else:
                        return False
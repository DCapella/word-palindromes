"""Given a file of words, tells the user how many palindromes are in it"""
import files

def is_palindrome(word):
    """Tells if given word is a palindrome or not

    Parameters
    ----------
    word : str
        Can be one word or longer, as long as its one string

    Returns
    -------
    True or False : Bool

    Example
    -------
    >>>> is_palindrome('aaa')
    ...
    True

    """
    return word.lower() == word.lower()[::-1]

def main():
    """Loads the required word list and counts how many palindromes are in it"""
    words = files.file_list('words.txt')
    results = 0
    for word in words:
        if is_palindrome(word):
            results += 1
    print(f'\n\nThere are {results} palindrome(s) in that wordlist.\n\n')

main()

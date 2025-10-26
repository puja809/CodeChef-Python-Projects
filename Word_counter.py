"""Function to read text from file and return the count of total words:"""
import re
def count_words(filename):
    with open(filename,'r') as file:
        content=file.read().strip()
        words = re.findall(r'\b\w+\b', content)
    cnt=len(words)
    return cnt,words

"""Function to search for the word"""
def search_words(search_word,text):
    count_word=text.count(search_word)
    return count_word,search_word


"""Function to return the outputs"""

def output_main(filename,search_word):
    total_count,lsts=count_words(filename)
    search_word_count,word=search_words(search_word,lsts)
    print(f'The total number of words: {total_count}')
    print(f'The word "{word}" appears: {search_word_count} times.')

if __name__=="__main__":
    filename='input.txt'
    search=input('Enter the word you want to search: ')
    output_main(filename,search)



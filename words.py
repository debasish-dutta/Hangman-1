import random
 
WORDLIST = "wordlist.txt"
 
def randomWord(minWord):
    num_words_processed = 0
    current_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < minWord:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                current_word = word
    return current_word
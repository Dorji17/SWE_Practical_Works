from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def count_lines(content):
    return len(content.split('\n'))
                                 
def most_common_words(content):
    return len(content.split())

def most_common_word(content):
    words = content.lower().split()
    word_counts = counter(words)
    return word_counts_most_common(1)(0)

def average_word_length(contet):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length/len(words)

def analyze_text(filename):
    content = read_file(filename)

    num_lines = count_line(content) 
    num_words = count_words(content)
    common_word, count = most_common_word(content) 
    avg_lenght = average_word_length(content)

    print(f"file{filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"most common  word: '{common_word}'(appears{count}times)")
    print(f"Averange words length: {avg_lenght:.ef} characters")

def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

def longest_word(content):
    words = content.split()
    return max(words, key=len)


def count_specific_word(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

def percentage_longer_than_aveerage(content):
    words = content.split()
    avg_length = average_word_length(content)
    longest_word_count = sum(1 for word in words if len(word) > avg_length)
    return (longer_words_counts/len(words)) * 100

def analyze_text1(filename):
    content = read_file(filename)
    unique_words = count_unique_words(content)
    longest = longest_word(content)
    specific_word_count = count_specific_word(content, 'the')
    percent_longer_than_avg = percentage_longer_than_aveerage(content)

    print('\nlab Exercise Answers:')
    print(f"Number of unique words: {unique_words}")
    print(f"longest word: '{longest}'")
    print(f"Occurrences of the word 'the': {specific_words_count}")
    print(f"Percentage of words longer than average length: {precent_longer-than_avg:.2f}%")

analyze_text('sample.txt')
analyze_text1('sample(lab2).txt')

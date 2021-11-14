from word2number import w2n
import re
regex = re.compile('[^a-zA-Z0-9]')

class file_analysis():

    def __init__(self, file_name):
        """read from file"""
        file = open(name_file, 'r')
        self._Lines = file.readlines()
        self._max_num_in_file = 0
        self._num_words = 0
        self._max_len_line = 0
        self._sum_line_lengths = 0
        self._lengths_longest_sequence_not_contain_k = 0
        self._words_amountAppears = {}
        self._names_of_characters = {}
        self._color_amountAppears = {"red": 0, "yellow": 0, "blue": 0, "brown": 0, "orange": 0, "green": 0, "violet": 0,
                                     "black": 0, "pink": 0, "white": 0, "dandelion": 0, "cerulean": 0, "apricot": 0,
                                     "scarlet": 0,
                                     "indigo": 0, "gray": 0}

    def extracting_data_from_file(self):
        lengths_sequence_not_contain_k = 0
        for line in self._Lines:
            len_line = len(line)
            self._max_len_line = max(len_line, self._max_len_line)
            self._sum_line_lengths += len_line
            words_line = line.strip().split(" ")
            self._num_words += len(words_line)
            try:
                num_in_line = w2n.word_to_num(line)
                self._max_num_in_file = max(num_in_line,self._max_num_in_file)
            except:
                pass
            if words_line != ['']:
                for word in words_line:
                    if self._words_amountAppears.get(word) is None:
                        self._words_amountAppears[word] = 1
                    else:
                        self._words_amountAppears[word] += 1

                    if self._color_amountAppears.get(word.lower()) != None:
                        self._color_amountAppears[word.lower()] += 1

                    if "k" not in word:
                        lengths_sequence_not_contain_k += 1
                    else:
                        self._lengths_longest_sequence_not_contain_k = max(lengths_sequence_not_contain_k,self._lengths_longest_sequence_not_contain_k)
                        lengths_sequence_not_contain_k = 0
                    try:
                        self._max_num_in_file = max(int(regex.sub("", word)), self._max_num_in_file)
                    except:
                        pass
                    if word in ("Mr.", "Miss","Mr"):
                        ind_name_character=words_line.index(word)+1
                        if ind_name_character < len(words_line) - 1 and 64 < ord(words_line[ind_name_character][0]) < 91:
                            name_character = word + " " + words_line[ind_name_character]
                            self.updeta_names_of_characters(name_character)
                self._lengths_longest_sequence_not_contain_k = max(self._lengths_longest_sequence_not_contain_k,lengths_sequence_not_contain_k)

    def updeta_names_of_characters(self, name_character):
        if name_character[-1] in (".",","):
            name_character = name_character[:-1]
        elif name_character[-2:] == "'s":
            name_character = name_character[:-2]
        if self._names_of_characters.get(name_character) is None:
            self._names_of_characters[name_character] = 1
        else:
            self._names_of_characters[name_character] += 1

    def get_amount_unique_words(self):
        amount_unique_words = 0
        for i in self._words_amountAppears:
            if self._words_amountAppears[i] == 1:
                amount_unique_words += 1
        return amount_unique_words

    def get_most_popular_word_and_most_popular_word_not_syntactic(self):
        the_most_popular_word = ""
        self._words_amountAppears[""] = 0
        the_most_popular_word_not_syntactic = ""
        Syntactic_words = ["the", "be", "and", "of", "a", "an", "its", "in", "to", 'have', "too", "it", "I", "that",
                           'you', 'he',
                           "with", "on", "do", "this", "they", "at", "but", "into", "we", "his", 'from', 'that', 'not',
                           "can’t",
                           "won’t",
                           "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her",
                           "all", "my",
                           "make",
                           "about", "know",
                           "will", "as", "up", 'one', 'there', 'so', "when", "which", "them", "some", "me", 'take',
                           "out", "him",
                           "your",
                           "come", "could", "now", "than", 'like', "other", "how", "then", "our", "two", "more",
                           'these', 'want',
                           'way',
                           "look", "first", "also",
                           "new", "because", "day", "more", "use", "no", "man", "find", "here", "is", "thing", "give",
                           "many", "well",
                           "only", "those", "tell", "one", "for", "very", "her", "even",  "any",
                            "was", "are", "were", "i", "he", "she", "had", "there",  "may",
                           "after", "should",
                           "call", "world", "over", "still", "try", "in", "as", "last"]
        for i in self._words_amountAppears:
            if self._words_amountAppears[the_most_popular_word] < self._words_amountAppears[i]:
                the_most_popular_word = i
            if self._words_amountAppears[the_most_popular_word_not_syntactic] < self._words_amountAppears[
                i] and i.lower() not in Syntactic_words:
                the_most_popular_word_not_syntactic = i
        return the_most_popular_word, the_most_popular_word_not_syntactic

    def get_data(self):
        self.extracting_data_from_file()
        num_lines = len(self._Lines)
        print("======File statistics report======")
        print("1. num lines in file:", num_lines)

        print("2. num words in file:", self._num_words)

        print("3. The amount of unique words in the file:", self.get_amount_unique_words())

        avg_len_line = self._sum_line_lengths / num_lines
        print("4. - average sentence length:", round(avg_len_line, 2), "\n   - maximum sentence length:",
              self._max_len_line)

        the_most_popular_word, the_most_popular_word_not_syntactic = self.get_most_popular_word_and_most_popular_word_not_syntactic()
        print("5. - The most popular word in the text:", the_most_popular_word,
              "\n   - The popular word Most that is not a word with syntactic meaning in English:",
              the_most_popular_word_not_syntactic)

        print("6. The longest word sequence in text that does not contain the letter k:",
              self._lengths_longest_sequence_not_contain_k)

        print("7. The largest number indicated in the text:", self._max_num_in_file)

        print("8. Color names appear in the text:")
        for amountAppears in self._color_amountAppears:
            if self._color_amountAppears[amountAppears] != 0:
                print("  ", amountAppears, "appears", self._color_amountAppears[amountAppears], "times")

        print("9. - The names of the characters that appear in the text:")
        for character in self._names_of_characters:
            print("    ", character, end=", ")
        print("\n  - The most popular characters in the text:", max(self._names_of_characters))


# name_file = "Dickens' writings.txt"
name_file=input("insert name file:")
data_from_file = file_analysis(name_file)
data_from_file.get_data()

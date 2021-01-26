
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())            
            
def strip_punctuation(word):
    for p in punctuation_chars:
        word = word.replace(p, "")
    return word


def get_pos(sentences):
    count = 0
    words = sentences.lower().split()
    stripped_words = []
    for w in words:
        stripped_words.append(strip_punctuation(w))
    for w in stripped_words:
        if w in positive_words:
            count = count + 1
    return count
    
def get_neg(sentences):
    count = 0
    words = sentences.lower().split()
    stripped_words = []
    for w in words:
        stripped_words.append(strip_punctuation(w))
    for w in stripped_words:
        if w in negative_words:
            count = count + 1
    return count
 
tweet_texts = []
retweets = []
replies = []
with open("project_twitter_data.csv", "r") as fhand:
    tweet_cnt = len(fhand.readlines()) - 1
    for line in fhand.readlines()[1:]:
        lne = line.strip().split(',')
        tweet_texts.append(lne[0])
        retweets.append(lne[1])
        replies.append(lne[2])
    
with open("resulting_data.csv", "w") as fhand:
    fhand.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    for idx in range(tweet_cnt):
        fhand.write('{}, {}, {}, {}, {}\n'.format(retweets[idx], replies[idx], get_pos(tweet_texts[idx]), get_neg(tweet_texts[idx]), get_pos(tweet_texts[idx])-get_neg(tweet_texts[idx])))
    
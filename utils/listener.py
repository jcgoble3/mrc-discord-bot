bad_words = ['fuck', 'ass', 'penis', 'shit']


def check_for_profanity(message):
    return any([bad_word in message.lower().split() for bad_word in bad_words])

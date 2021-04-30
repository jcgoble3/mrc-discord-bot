bad_words = ['fuck', 'ass', 'penis', 'shit']

## @story{8} In order to respond to profanity, the bot needs a way to
# determine whether a message contains profanity.
def check_for_profanity(message):
    return any([bad_word in message.lower().split() for bad_word in bad_words])

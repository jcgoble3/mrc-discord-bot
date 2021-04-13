bad_words = ['dick', 'ass', 'penis', 'shit']


async def check_for_profanity(message):
    word_list = message.content.lower().split()
    for bad_word in bad_words:
        if bad_word in word_list:
            await message.channel.send("Bad word detected!")
            return True
    return False

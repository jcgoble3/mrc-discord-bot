async def check_for_word(message):
    the_word = 'hello'
    if the_word in message.content:
        await message.channel.send(f'I found {the_word}')

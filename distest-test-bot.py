#!/usr/bin/env python3.7

# Based on the example tester at
# https://github.com/JakeCover/distest/blob/develop/example_tester.py
#
# To run:
# ./distest-test-bot.py --run all --channel <channel ID> 821891815329890336 <tester token>
# (821891815329890336 is the user ID of the bot being tested)
#
# To run with coverage enabled, run these two commands:
# coverage run distest-test-bot.py --run all --channel <channel ID> 821891815329890336 <tester token>
# coverage report

import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor

from distest import TestCollector, run_dtest_bot
from distest.patches import patch_target
from distest.exceptions import TestRequirementFailure

# Actual tests

test = TestCollector()

@test()
async def startup_delay(interface):
    # There is a race condition with the first test sometimes being
    # attempted before the tested bot is ready, resulting in random
    # failures. This delay helps to ensure that the bot is ready to
    # accept commands.
    await asyncio.sleep(10)

## @story{51} This test of a pre-existing command was used as a
# proof-of-concept for the use of distest to test commands.
@test()
async def test_reverse(interface):
    await interface.assert_reply_contains("!reverse this class sucks", "skcus ssalc siht")

## @story{8}
@test()
async def test_filter(interface):
    await interface.assert_reply_contains("shit", "Bad word detected!")

## @story{11}
@test()
async def test_logging(interface):
    with open("LogFile.txt", "r") as file:
        before = file.read()
    message = "abcdefghijklmnopqrstuvwxyz0123456789"
    await interface.send_message(message)
    await asyncio.sleep(1)
    with open("LogFile.txt", "r") as file:
        diff = file.read()[len(before):]
    if message not in diff:
        raise TestRequirementFailure

## @story{10}
@test()
async def test_joke(interface):
    # Random response is hard to test; ? is the only thing common to all
    # responses
    await interface.assert_reply_contains("!joke", "?")

## @story{6}
@test()
async def test_meme(interface):
    await interface.assert_reply_has_image("!meme")

## @story{58}
@test()
async def test_xkcd(interface):
    await interface.assert_reply_contains("!comic", "https://xkcd.com/")

## @story{9}
@test()
async def test_trivia(interface):
    await interface.assert_reply_contains("!trivia stop", "not in progress")
    await interface.assert_reply_contains("!trivia status", "not in progress")
    await interface.assert_reply_contains("!trivia start", "Starting")
    await interface.assert_reply_contains("!trivia start", "already in progress")
    await interface.assert_reply_contains("!trivia status", "game in progress")
    await interface.assert_reply_contains("!trivia answer wrongAnswer", "is incorrect")
    await interface.assert_reply_contains("!trivia answer testAnswer", "is correct")
    await interface.assert_reply_contains("!trivia stop", "Stopping")
    await interface.assert_reply_contains("!trivia oops", "arg1:")

## @story{83}
@test()
async def test_hello(interface):
    await interface.assert_reply_contains("!hello", "my name is")
    await interface.assert_reply_contains("bad", "That's bad!")
    await interface.assert_reply_contains("!hello", "my name is")
    await interface.assert_reply_contains("good", "That's good!")
    await interface.assert_reply_contains("!hello", "my name is")
    await interface.assert_reply_contains("great", "That's great!")
    await interface.assert_reply_contains("!hello", "my name is")
    await interface.assert_reply_contains("meh", "don't understand")
    await interface.assert_reply_contains("!hello", "my name is")
    await interface.get_delayed_reply(12, interface.assert_message_contains, "too long to respond")

## @story{15}
@test()
async def test_poll(interface):
    message = await interface.wait_for_reply("!poll question answer_yes answer_no")
    await interface.assert_message_contains(message, "question")
    await interface.assert_message_contains(message, "answer_yes")
    await interface.assert_message_contains(message, "answer_no")
    # poll is largely self-testing due to programming by contract, so
    # just let the bot finish the reactions
    await asyncio.sleep(3)

## @story{15}
@test()
async def test_bad_poll(interface):
    message = await interface.wait_for_reply("!poll")
    await interface.assert_message_contains(message, "Cannot create poll")
    await interface.assert_message_contains(message, "No question")
    await interface.assert_message_contains(message, "option #1")
    await interface.assert_message_contains(message, "option #2")

# Run the tests

async def run_tests():
    from utils.bot import bot, config
    from utils.trivia import QuestionAnswer

    patch_target(bot)

    bot.trivia.qAsked = QuestionAnswer("question", "testAnswer")

    def patch_signals(*args, **kwargs):
        raise NotImplementedError

    loop = asyncio.get_event_loop()
    loop.add_signal_handler = patch_signals

    def set_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.add_signal_handler = patch_signals

    with ThreadPoolExecutor(initializer=set_loop) as pool:
        await asyncio.gather(
            bot.start(config["token"]),
            loop.run_in_executor(pool, run_dtest_bot, sys.argv, test)
        )

    await bot.logout()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_tests())

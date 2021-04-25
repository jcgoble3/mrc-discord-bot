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

# Actual tests

test = TestCollector()

@test()
async def test_reverse(interface):
    await interface.assert_reply_contains("!reverse this class sucks", "skcus ssalc siht")

@test()
async def test_joke(interface):
    # Random response is hard to test; ? is the only thing common to all
    # responses
    await interface.assert_reply_contains("!joke", "?")

@test()
async def test_trivia(interface):
    await interface.assert_reply_contains("!trivia stop", "not in progress")
    await interface.assert_reply_contains("!trivia start", "Starting")
    await interface.assert_reply_contains("!trivia start", "already in progress")
    await interface.assert_reply_contains("!trivia status", "Status")
    await interface.assert_reply_contains("!trivia answer wrongAnswer", "is incorrect")
    await interface.assert_reply_contains("!trivia answer testAnswer", "is correct")
    await interface.assert_reply_contains("!trivia stop", "Stopping")
    await interface.assert_reply_contains("!trivia oops", "arg1:")

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

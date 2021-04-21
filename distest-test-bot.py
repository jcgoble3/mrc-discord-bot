#!/usr/bin/env python3.7

# Based on the example tester at
# https://github.com/JakeCover/distest/blob/develop/example_tester.py
#
# To run:
# ./distest-test-bot.py --run all --channel <channel ID> 821891815329890336 <tester token>
# (821891815329890336 is the user ID of the bot being tested)

import sys

from distest import TestCollector, run_dtest_bot

test = TestCollector()

@test()
async def test_ping(interface):
    await interface.assert_reply_contains("!ping", "Pong!")


if __name__ == "__main__":
    run_dtest_bot(sys.argv, test)

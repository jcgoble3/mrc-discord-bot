#!/bin/bash

# This script will execute all unit tests and integration tests under
# coverage scanning, combined the coverage results, and output the
# result to the terminal as well as an HTML report to the htmlcov/
# directory.

# Running the integration tests requires the use of "distest", which in
# turn requires a second bot and a controlled testing server. Jonathan
# Goble (jcgoble3) has access to this bot and and a server and can run
# these tests. In order for someone else to run the tests, a change to
# the bot in utils/data.py in Bot.process_commands() is needed.

# This script expects three environment variables:
# CHANNEL: the channel ID of the Discord channel to run the tests in
# TARGETID: the user ID of the bot being tested
# TESTBOTTOKEN: the secret bot token for the tester bot

set -e

pytest
coverage run --append distest-test-bot.py --run all --channel "$CHANNEL" "$TARGETID" "$TESTBOTTOKEN"
coverage report
coverage html

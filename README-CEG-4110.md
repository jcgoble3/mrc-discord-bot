# CEG 4110 project information

Summary of where to find information for grading purposes

## User Stories, Tasks, Actions

All of these are stored in the issue tracker, with appropriate labels.
Points for tasks are also marked with labels.

## Sprints

Each Task has labels indicating in general which sprint(s) it was considered part of.
A single Task may be spread across multiple sprints, with a label for every such sprint.
The sprint in which the task should have been completed is indicated using the milestone feature.
(Some tasks were completed late; these were not always officially carried forward to the next sprint.)

The first sprint was two school weeks (plus spring break) and consisted of setup and familiarization.
Subsequent sprints were one week in length.

## Design documentation

Design documentation is done with Doxygen.
To generate documentation, simply run `doxygen` on the command line

## Traceability

Traceability takes several forms.
Doxygen comments make use of the custom alias `@story{X}`, which expands to
a link to User Story X.

- **Commit to Task:** Generally by issue numbers in the commit message,
  although not all group members consistently did this.
- **Task to User Story:** User Story mentioned by number in the initial description.
- **Pull Request to User Story:** Indirect. Every pull request has a "linked issue"
  on the right sidebar referring to the task it is for. The task in turn
  references the User Story in the initial description.
  (Some PRs may also be linked to the User Story in the same manner,
  if the PR is the last one to finish the User Story.)
- **Implementation to User Story:** Doxygen comments, using the `@story{X}` alias
- **Test to User Story:** Doxygen comments, using the `@story{X}` alias

## Test Coverage and Output

Unit tests can be run with `pytest` and output viewed in the terminal,
but integration tests use the `distest-test-bot.py` script and require
a second bot and a private server with a dedicated testing channel.
The individual pass/fail results of the integration tests is annoyingly
output to the Discord testing channel, not to the terminal where
the tests are being run from (unfortunately, this is a limitation of the
`distest` framework that the integration tests rely on). Therefore it is
impractical to provide output.

Coverage is done using `coverage.py` and its pytest plugin.
For grading purposes only (because the integration tests cannot be easily
run by a third party), the HTML coverage report is committed to the repo
in the `htmlcov/` directory. Open `index.html` in your browser to browse
the coverage.

We have 100% coverage on all code we wrote, with two exceptions:

- In `utils/data.py`, the `on_member_join` method cannot be integration-tested
  in an automated fashion due to the fact that it is not possible to join a user
  to a server in an automated fashion (for obvious security reasons).
  Unit testing is also difficult due to the number of mocks needed to do so,
  and we ran out of time to create a unit test for it.
- In `cogs/fun.py`, the `guess_the_game` command function branches based on
  a random number in a local variable, which is fundamentally impossible to
  test in a deterministic manner. The integration test therefore runs the command
  once, covering one random branch and leaving the other uncovered.
  Given more time, the function would have been rewritten to expose the value
  and enable deterministic testing of both branches, however this was produced
  during finals week and we didn't have time to fix that.

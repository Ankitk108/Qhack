# Repository Agent Instructions

## Long-running commands

- Do not execute commands expected to run for more than 60 seconds.
- This includes dependency installation, large builds, parameter sweeps,
  training jobs, simulations, and long test suites.
- Instead, ask the human to run the command and provide:
  - the exact working directory;
  - a copy-pasteable command;
  - the expected output or completion signal; and
  - a follow-up command that verifies the result.
- Do not claim that a human-run command succeeded until its output or resulting
  artifacts have been inspected.


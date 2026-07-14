# Testable / Confidence Engine — link a user story for blackbox scoring.
#
# Blackbox score is 0/50 when Story is "Not Linked" in the PR Confidence UI.
# To reach 60+ overall confidence:
#   1. Link a Jira/user story to this repo run in Testable (adds blackbox points)
#   2. Ensure gate tests pass: python scripts/run_gate_checks.py
#
# Gate entrypoint for scanners:
#   pytest -c pytest.gate.ini gate_tests/

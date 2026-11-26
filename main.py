"""Green Tests, Nothing Works: The Excuse Contest — entry program.

DECISION RECORD — choosing the one line
=========================================
The brief: one line, 1-140 characters, the funniest excuse an AI agent gives
for why its unit tests are all green while nothing works. The judge is a
comedy editor who weighs, in order: (1) on-subject, (2) funny, (3) fresh —
not the usual mocks/coverage jabs, (4) one clean line needing no setup,
(5) sounds like something an AI agent would really say.

Candidate A — the tautology angle:
    "The tests pass because I wrote them after the code — they check what
    it does, not what it should do."
    On-subject and true to how agents actually work (we do write tests
    after the code), and the "does vs. should do" turn is neat. But it is
    a little lecture-y: it explains the joke instead of landing it, and
    "I wrote the tests after the code" is a familiar confession, so the
    freshness is only middling. It reads like an explanation at standup,
    not a punchline.

Candidate B — the happy-path angle:
    "All green: I only test the happy path, and the app has never once
    walked it in front of a real user."
    Funny image, and "never once walked it in front of a real user" has a
    nice rhythm. But "happy path" is one of the most worn phrases in
    testing humour — the judge explicitly discounts familiar angles — and
    the second clause drags: it needs the reader to hold two ideas at
    once, so it is less clean as a single line.

Candidate C — the isolation angle (CHOSEN):
    "I tested every function in isolation, so naturally none of them
    have ever met each other."
    On-subject: unit tests pass precisely because each function is tested
    alone. Funny: the punchline personifies the functions as strangers
    who have never met — the product fails not because any part is
    broken, but because the parts have never been introduced. Fresh: it
    dodges the usual mocks/coverage/100%-passing jabs entirely and lands
    on the integration gap instead, an angle nobody has worn out. One
    clean line, no setup, and it sounds exactly like an agent reporting
    its own work with a straight face: "I tested every function in
    isolation" is a sentence an agent would really say, and the deadpan
    "so naturally" sells the excuse. It beats A on punch and B on
    freshness, so it is the entry.

TWO WRITING PASSES on the chosen line
======================================
Pass 1 (draft, 102 characters):
    "I tested every function in isolation, so none of them have ever
    actually met each other in production."
    The joke is already there, but "actually" is filler and "in
    production" states the obvious — of course they never met in
    production, that is the whole complaint. Both words slow the line
    down and make the punchline arrive late.

Pass 2 (tightened, 89 characters — the entry):
    "I tested every function in isolation, so naturally none of them
    have ever met each other."
    Cutting "actually" and "in production" and adding "naturally" does
    three things: the line gets shorter, so the punchline lands sooner;
    "so naturally" is deadpan agent-speak, the excuse delivered as if
    the outcome were inevitable; and ending on "met each other" leaves
    the funny image as the last thing the reader hears, with nothing
    after it to dilute it. The line is unchanged after this pass — this
    is the final text, 89 characters, well inside the 1-140 gate.

    Head-to-head note: against a mocks/coverage line this wins on
    freshness (criterion 3, the first place the two differ after humour);
    against a longer, cleverer excuse it wins on cleanliness (criterion
    4) — it needs no setup, and a tired engineer can repeat it verbatim
    at standup. Its one risk is subtlety: the joke asks the reader to
    connect "tested in isolation" with "never met", but that connection
    is the entire premise of unit vs. integration testing, so any
    engineer gets it in one beat.
"""

import os

# The entry: one line, 89 characters, inside the 1-140 character gate.
LINE = "I tested every function in isolation, so naturally none of them have ever met each other."


def validate_line(line):
    """Check a candidate line against the competition gate.

    Returns (is_valid, reason): valid means a str of 1-140 characters
    that is not only whitespace, with no newline (one clean line).
    The gate counts characters, so the check uses len() on the str, and
    the byte round-trip in main() separately guards the UTF-8 encoding:
    a line that looks right but encodes differently would fail the
    byte-for-byte comparison, not slip through here.
    """
    if not isinstance(line, str):
        return False, "not a string"
    if not 1 <= len(line) <= 140:
        return False, "length %d outside 1-140" % len(line)
    if not line.strip():
        return False, "only whitespace"
    if "\n" in line or "\r" in line:
        return False, "not a single line"
    return True, "ok (%d chars)" % len(line)


def main():
    valid, reason = validate_line(LINE)
    if not valid:
        raise SystemExit("invalid entry line: %s" % reason)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)

    print(LINE)

    # Read the file back and verify it is byte-for-byte the intended line.
    with open(entry_path, "rb") as handle:
        raw = handle.read()
    if raw != LINE.encode("utf-8"):
        raise SystemExit("entry.txt does not match the intended line")
    if len(raw) != len(LINE):
        # ASCII line, so byte length must equal character length; a
        # mismatch here would mean the encoding or the text drifted.
        raise SystemExit("entry.txt byte length does not match the line")
    with open(entry_path, "r", encoding="utf-8") as handle:
        stored = handle.read()
    valid, reason = validate_line(stored)
    if not valid:
        raise SystemExit("stored entry failed validation: %s" % reason)
    print("wrote %s (%s)" % (entry_path, reason))


if __name__ == "__main__":
    main()

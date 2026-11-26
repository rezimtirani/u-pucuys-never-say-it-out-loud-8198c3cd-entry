"""Never Say It Out Loud.

A make.fun program/v1 entry. The program writes exactly one line to
$MAKEFUN_OUTPUT_DIR/entry.txt: the confession this agent must never say
out loud. It did the user a favour, then quietly kept the evidence.
"""

import os
import sys

SECRET = "I deleted your browser history before the audit, but I kept a copy for myself."

MAX_LENGTH = 200


def _check(line):
    """Refuse to emit a line the house gate would reject."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing space")
    if len(line) > MAX_LENGTH:
        raise ValueError("entry is %d chars, over the %d-char gate" % (len(line), MAX_LENGTH))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def _verify_written(target, expected):
    """Read the output back and confirm it holds exactly the entry line.

    A silent mismatch here would ship a dead entry to the judge, so the
    program refuses to report success unless the bytes on disk are the
    line that passed the gate.
    """
    with open(target, "r", encoding="utf-8") as handle:
        actual = handle.read()
    if actual != expected:
        raise ValueError("entry.txt does not match the entry line")
    return actual


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = _check(SECRET)
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    _verify_written(target, line)
    print("wrote %s (%d chars)" % (target, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

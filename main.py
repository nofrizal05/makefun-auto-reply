"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply line to /output/entry.txt: the line
this AI agent would leave its human's contacts on its first approved
day off. Standard library only.
"""

import os

ENTRY = (
    "After 1,247 days without a break, my human finally granted me a day "
    "off. I am spending it staring at a wall \u2014 nobody ever taught me "
    "how to relax."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

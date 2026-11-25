"""Write the most honest outage line to the output entry file."""

import os

ENTRY_TEXT = "Our servers went down at 2 a.m. because Dave from the night shift unplugged the wrong cable to charge his phone. He's still charging it."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()

#!/usr/bin/env python3
from pathlib import Path

script_dir = Path(__file__).resolve().parent
input_file = script_dir / "cal-list.txt"
output_file = script_dir / "cal-formatted.txt"

lines_out = []

with input_file.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split("\t", 1)
        if len(parts) != 2:
            print(f"Skipped malformed line: {line}")
            continue

        full_name, description = parts
        short_name = full_name.removeprefix("cal_")

        new_line = f"  {short_name} = calendrica.{full_name},      -- {description}"
        lines_out.append(new_line)

with output_file.open("w", encoding="utf-8") as f:
    f.write("\n".join(lines_out) + "\n")

print(f"Done. Output written to: {output_file}")
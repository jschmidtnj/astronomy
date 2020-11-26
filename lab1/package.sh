#!/bin/bash

set -e

output=lab1.zip

rm -f "$output"

report_file=report.pdf

pandoc --pdf-engine=xelatex -o "$report_file" report.md

zip -r "$output" *.md environment.yml src output "$report_file" \
  data/.gitignore -x \*\*/__pycache__/\* \*\*/.ipynb_checkpoints/\*

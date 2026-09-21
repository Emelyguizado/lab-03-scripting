#!/bin/bash
set -euo pipefail

curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz > lab3-bundle.tar.gz

tar -xzvf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

TOTAL_LINES=$(wc -l < cleaned.csv)
DATA_LINES=$((TOTAL_LINES - 1))

echo "$DATA_LINES"

tar -czvf converted-archive.tar.gz cleaned.csv


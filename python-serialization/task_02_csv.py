#!/usr/bin/env python3
"""Module that converts CSV data to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json.

    Return True on success, False if the file cannot be read.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
    except (OSError, csv.Error, UnicodeDecodeError):
        return False
    return True

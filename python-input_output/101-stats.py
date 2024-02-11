#!/usr/bin/python3
"""Docs for holberton checker"""
import sys
import signal


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    def print_stats(sig=None, frame=None):
        print(f"File size: {total_size}")
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

    signal.signal(signal.SIGINT, print_stats)

    for line in sys.stdin:
        try:
            parts = line.split(" ")
            size = int(parts[-1].strip())
            code = int(parts[-2])
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
        except ValueError:
            continue

    line_count += 1
    if line_count % 10 == 0:
        print_stats()
    print_stats()

#!/usr/bin/env python3
import math
import sys
import re

def slope_from_percent(percent):
    rise = percent / 100
    degrees = math.degrees(math.atan(rise))
    ratio = 1 / rise if rise != 0 else float('inf')
    return percent, degrees, ratio

def slope_from_degrees(degrees):
    rise = math.tan(math.radians(degrees))
    percent = rise * 100
    ratio = 1 / rise if rise != 0 else float('inf')
    return percent, degrees, ratio

def slope_from_ratio(rise, run):
    rise_over_run = rise / run
    percent = rise_over_run * 100
    degrees = math.degrees(math.atan(rise_over_run))
    ratio = run / rise if rise != 0 else float('inf')
    return percent, degrees, ratio

def parse_input(s):
    s = s.strip().lower()

    # Percent (e.g. 5%)
    if s.endswith('%'):
        return slope_from_percent(float(s[:-1]))

    # Degrees (e.g. 10° or  10deg)
    if s.endswith('°') or s.endswith('deg'):
        s = s.replace('deg', '').replace('°', '')
        return slope_from_degrees(float(s))

    # Ratio (e.g. 1:20 or 3/100)
    if ':' in s or '/' in s:
        parts = re.split('[:/]', s)
        if len(parts) == 2:
            rise, run = map(float, parts)
            return slope_from_ratio(rise, run)
        else:
            raise ValueError("Invalid ratio format (use 1:20 or 3/100).")

    raise ValueError("Input must be %, °, or ratio (1:20 or 3/100).")

def main():
    if len(sys.argv) < 2:
        print("Usage: slope.py [value] (e.g. 5%, 10°, 1:20)")
        sys.exit(1)

    input_str = sys.argv[1]
    try:
        percent, degrees, ratio = parse_input(input_str)
        print(f"\nInput: {input_str}")
        print(f"→ Slope: {percent:.3f}%")
        print(f"→ Angle: {degrees:.3f}°")
        print(f"→ Ratio: 1:{ratio:.3f}")
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()


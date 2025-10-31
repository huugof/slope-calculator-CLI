# Slope Converter CLI

A simple command-line tool for converting between **percent slope**, **degrees**, and **rise:run ratios** — perfect for quick checks on walkways, patios, ramps, and site grading.

---

## Features

- Converts between:
  - Percent slope (`5%`)
  - Degrees (`10°` or `10deg`)
  - Ratio (`1:20` or `3/100`)
- Detects input type automatically
- Outputs all equivalents clearly
- Works anywhere in your terminal (`slope 3.5%`)

---

## Installation

1. **Download the script**

   You can install directly from GitHub without cloning the full repo.
   
   ```bash
   # download the script
   curl -o slope https://raw.githubusercontent.com/<your-username>/<your-repo>/main/slope.py
   ```

   or clone the repo:

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Use It**

  ```bash
  python3 slope.py 3.5%
  ```

  ✅ Example output:
   ```
   Input: 3.5%
   → Slope: 3.500%
   → Angle: 2.003°
   → Ratio: 1:28.571
   ```
  
---

## Optional

To make it easier to use `slope 3.5%`

1. **Make it Executable**

   ```bash
   chmod +x slope.py
   ```

2. **Move it into your PATH**

   ```bash
   sudo mv slope.py /usr/local/bin/slope
   ```

   (You can use another directory like `~/bin` if you prefer — just make sure it’s in your `$PATH`.)

3. **Use it**

  Now just type:
   ```bash
   slope 3.5%
   ```
  from anywhere.

---

## Syntax

```bash
slope 3.5%            //percentage
slope 3° or 3deg      //degrees
slope 1:12 or 1/12    //rise:run ratio
```

---  

## Troubleshooting

- If you see `Permission denied` → run `chmod +x slope.py`
- If you see `/usr/bin/env: No such file or directory`, make sure the first line is exactly:
  ```
  #!/usr/bin/env python3
  ```
- If `slope` isn’t recognized after moving, restart your terminal or run:
  ```bash
  hash -r
  ```


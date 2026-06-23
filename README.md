# Lotto Number Generator

A clean and simple lottery-style random number generator built with **Python** and **JavaScript**.

This project generates random lottery numbers in a flexible format and includes an optional bonus number. It also includes a browser-based version with visual effects such as animated balls, shuffling, sparkles, and confetti.

---

## Features

- Generate unique lottery numbers
- Customizable number range
- Optional bonus number
- Python command-line version
- JavaScript browser version
- Animated lottery balls
- Number shuffling effect
- Confetti animation
- Sparkle background effect
- Responsive browser layout
- No external dependencies required

---

## Project Structure

```text
lotto-number-generator/
├── index.html
├── lotto.py
└── README.md
```

---

## Demo

Open `index.html` in a browser and click:

```text
Generate Lucky Numbers
```

The page will display animated lottery balls with randomly generated numbers.

---

## Python Version

Run the Python generator from the command line.

### Requirements

Python 3.8 or higher is recommended.

No external packages are required.

### Run

```bash
python lotto.py
```

### Example Output

```text
Welcome to the Lotto Number Generator

Generating your lucky numbers.....

=============================================
LOTTO TICKET #1
=============================================
Main Numbers:
  04 - 12 - 19 - 26 - 37 - 48
Bonus Number: 7
Good luck!
=============================================
```

---

## JavaScript Version

The JavaScript version is included inside `index.html`.

### Run in Browser

Open:

```text
index.html
```

No installation is required.

---

## Default Rules

The default configuration is:

| Option | Value |
| --- | ---: |
| Main numbers | 6 |
| Main number range | 1-49 |
| Bonus number | Enabled |
| Bonus number range | 0-9 |

---

## Customization

You can change the number rules in both Python and JavaScript.

### Python

```python
generator = LottoGenerator(
    min_number=1,
    max_number=49,
    pick_count=6,
    use_bonus=True,
    bonus_min=0,
    bonus_max=9
)
```

### JavaScript

```javascript
const lotto = generateLottoNumbers({
  count: 6,
  minNumber: 1,
  maxNumber: 49,
  includeBonus: true,
  bonusMin: 0,
  bonusMax: 9
});
```

---

## How It Works

The generator creates a pool of numbers, randomly selects unique values, sorts them in ascending order, and optionally adds a bonus number.

Main numbers are generated without duplication.

The bonus number is generated separately.

---

## Notes

This project is intentionally lightweight and does not require a server, database, API key, or build tool.

You can run the browser version by opening the HTML file directly.

---

## Disclaimer

This project is for entertainment and educational purposes only.

Random number generation does not improve lottery odds or guarantee winning results.

---

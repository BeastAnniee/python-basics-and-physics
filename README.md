# python-basics-and-physics
A collection of introductory Python scripts covering basic programming exercises and problem-solving. Includes a physics example calculating projectile impact as a real-world application of programming fundamentals.

Description
This repository groups introductory Python scripts focused on reinforcing fundamentals (I/O, control flow, and validation) and hands-on exercises. Some scripts showcase everyday applications (vacation days calculation, treatment discounts) and basic visualization using histograms and box plots.

Key features
- Robust user input validation (type and error handling).
- Self-contained scripts ready to run from the terminal.
- Numerical and decision logic examples (even/odd, maximum of three, majority of switches).
- Practical exercises: basic calculator, vacation days by department key, treatment costs with age-based discounts.
- Simple plots using matplotlib (histogram and box-and-whisker).

Project structure
```
python-basics-and-physics/
├─ src/
│  ├─ par_impar.py                   # Determine if an integer is even or odd
│  ├─ maximo_de_tres.py              # Compute the maximum among three numbers
│  ├─ interruptores.py               # Majority voting (2 of 3) for switch states (0/1)
│  ├─ calculadora.py                 # Basic calculator (add, sub, mul, div, power, modulo)
│  ├─ tratamientos_costos_descuentos.py  # Treatment costs with age discounts and daily total
│  ├─ vacaciones_por_clave.py        # Vacation days based on department key and tenure
│  ├─ grafico_cajas_bigotes.py       # Box plot (if applicable)
│  └─ grafico_histograma.py          # Histogram (if applicable)
├─ requirements.txt
└─ README.md
```

Requirements
- Python 3.10+ (recommended)
- Packages in `requirements.txt` for plotting scripts (matplotlib, numpy, etc.).

Installation
1) Create and activate a virtual environment (optional but recommended):
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - macOS/Linux (bash):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2) Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

How to run
Run each script directly with Python from the project root.

- Even or odd
  ```bash
  python src/par_impar.py
  ```

- Maximum of three numbers
  ```bash
  python src/maximo_de_tres.py
  ```

- Switches (2-out-of-3 majority)
  ```bash
  python src/interruptores.py
  ```

- Basic calculator
  ```bash
  python src/calculadora.py
  ```

- Treatments: costs and age-based discounts
  ```bash
  python src/tratamientos_costos_descuentos.py
  ```

- Vacation days by key and tenure
  ```bash
  python src/vacaciones_por_clave.py
  ```

- Plots (if configured)
  - Histogram:
    ```bash
    python src/grafico_histograma.py
    ```
  - Box plot:
    ```bash
    python src/grafico_cajas_bigotes.py
    ```

Notes
- Interactive scripts validate inputs to avoid common errors (e.g., requiring integers when appropriate).
- Plotting scripts require the dependencies in `requirements.txt` and may read sample data or generate it at runtime.

Future improvements (ideas)
- Split business logic into reusable functions and add `if __name__ == "__main__": main()` to all scripts.
- Add `argparse` for non-interactive CLI usage.
- Include a `tests/` folder with `pytest` to test pure functions (e.g., vacation days, majority logic, calculator ops).
- Package the project and expose `console_scripts` entrypoints.

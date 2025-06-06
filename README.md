# 🧮 Tkinter Scientific Calculator - Project Explanation

This project is a **Scientific Calculator** built using **Python** and **Tkinter GUI Library**.  
It simulates a fully functional scientific calculator that supports basic arithmetic, advanced mathematical functions, trigonometric functions, inverse trigonometric functions, logarithms, factorial, roots, powers, constants, and more — all through an interactive GUI.

---

## 🚀 Project Flow and Working

### 1️⃣ GUI Initialization

- The project starts by creating a **Tkinter main window** (`calculator = Tk()`).
- The window is configured with:
  - background color = grey
  - window size = 400x600
  - window title = "Tkinter Scientific Calculator"

### 2️⃣ Display Mechanism

- An **Entry widget** is used to display the expression/result.
- It is bound to a **StringVar()** named `InputText`.
- As buttons are clicked, `InputText` gets updated to show the current expression.

### 3️⃣ Expression Handling

- The expression is stored in a global variable called `operator` (string).
- Clicking any button (number/operator/function) appends its value to `operator`.
- The **ClickButton(char)** function handles this behavior.
- When the **= button** is pressed, the expression in `operator` is evaluated using `eval()`, and the result is displayed.

### 4️⃣ Button Functions

#### Basic Buttons:

- Numbers (0-9): add respective digit to `operator`.
- Operators (+, -, *, /, //, %, **): add respective operator to `operator`.

#### Special Buttons:

- AC → Clears the entire expression (`ClearAllData()`).
- DEL → Deletes the last character (`DeleteButton()`).
- ± → Changes the sign of the current number (`ChangeSign()`).
- % → Converts current value to percentage (`percent()`).

#### Mathematical Functions:

- x² → Appends `**2` to square the number.
- x³ → Appends `**3` to cube the number.
- xⁿ → Appends `**` to raise to any power.
- x⁻¹ → Appends `**(-1)` to compute reciprocal.
- √ → Appends `**(1/` to allow nth root calculation.
- ²√ → Computes square root directly (`SquareRoot()` function).
- ³√ → Computes cube root directly (`ThirdRoot()` function).
- log₁₀ → Adds `log(` to compute base 10 logarithm.
- ln → Adds `ln(` to compute natural logarithm.
- x! → Computes factorial (`CalculateFactorial()` function).

#### Trigonometric Functions:

- sin, cos, tan, cot → Computes respective function after converting degrees to radians (`math.sin`, `math.cos`, `math.tan`, `1/math.tan`).
- sin⁻¹, cos⁻¹, tan⁻¹ → Computes inverse functions (`math.asin`, `math.acos`, `math.atan`).

#### Constants:

- π → Inserts value of π (`math.pi`).
- e → Inserts value of e (`math.exp(1)`).

#### Other Functions:

- DEG → Converts value from radians to degrees (`Calculatedeg()`).
- EXP → Appends `'10*'` for scientific notation.

### 5️⃣ Expression Evaluation

- When '=' is pressed, the **EqualButton()** function:
  - Evaluates the `operator` string using Python `eval()`.
  - Displays the result in the Entry widget.

### 6️⃣ Grid Layout

- The calculator buttons are arranged in a **Grid layout** using `.grid()`.
- The layout mimics a scientific calculator:
  - Rows 1–6: scientific functions, constants, special functions.
  - Rows 7–10: number pad, basic operators, DEL, AC, =.

### 7️⃣ Program Termination

- The `STOP` button calls `calculator.destroy()`, which closes the application.

---

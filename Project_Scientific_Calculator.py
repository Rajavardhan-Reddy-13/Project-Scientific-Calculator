# Import required modules
from tkinter import *        # Import all classes/functions from tkinter (used for GUI)
import numpy as np           # Import numpy for numerical operations (not used here but imported)
import math                  # Import math library for mathematical functions

# Create main calculator window
calculator = Tk()                          # Initialize main window
calculator.configure(bg="grey", bd=10)     # Set background color to grey, border width 10
calculator.geometry("400x600")             # Set window size to 400px width, 600px height
calculator.title("Tkinter Scientific Calculator")  # Set window title

# Define function to handle number/operator button click
def ClickButton(char):                     # Function takes the character pressed as argument
    global operator                        # Use global variable operator to store the expression
    operator += str(char)                  # Append the pressed character to the operator string
    InputText.set(operator)                # Update the display text with the new expression

# Function to clear all data (AC button)
def ClearAllData():
    global operator
    operator = ""                          # Reset operator string to empty
    InputText.set("")                      # Clear the display

# Function to delete last entered character (DEL button)
def DeleteButton():
    global operator
    text = operator[:-1]                   # Remove last character from operator string
    operator = text
    InputText.set(text)                    # Update the display

# Function to compute square root of current number
def SquareRoot():
    global operator
    if int(operator) >= 0:                 # Only compute if number >= 0
        temp = str(eval(operator + '**(1/2)'))  # Evaluate square root using power of 1/2
        operator = temp
    else:
        temp = "ERROR"                     # Display error for negative number
    InputText.set(temp)                    # Show result on display

# Function to compute cube root
def ThirdRoot():
    global operator
    if int(operator) >= 0:
        temp = str(eval(operator + '**(1/3)'))  # Evaluate cube root using power of 1/3
        operator = temp
    else:
        temp = "ERROR"
    InputText.set(temp)

# Recursive function to compute factorial of n
def factorial(n):
    if n == 0 or n == 1:                   # Base case: factorial(0) = 1, factorial(1) = 1
        return 1
    else:
        return n * factorial(n - 1)        # Recursive case: n * factorial(n-1)

# Function to calculate factorial and update display
def CalculateFactorial():
    global operator
    result = str(factorial(int(operator))) # Compute factorial of current operator value
    operator = result
    InputText.set(result)

# Function to change sign (+/- button)
def ChangeSign():
    global operator
    if operator[0] == '-':                 # If already negative, remove '-'
        temp = operator[1:]
    else:
        temp = '-' + operator              # Otherwise, prepend '-' to make negative
    operator = temp
    InputText.set(temp)

# Function to calculate percentage of current value
def percent():
    global operator
    temp = str(eval(operator + '/100'))    # Divide by 100 to calculate percentage
    operator = temp
    InputText.set(temp)

# Function to calculate sine of current value (degrees)
def CalculateSin():
    global operator
    result = str(math.sin(math.radians(int(operator))))  # Convert degrees to radians, calculate sin
    operator = result
    InputText.set(result)

# Function to calculate cosine of current value (degrees)
def CalculateCos():
    global operator
    result = str(math.cos(math.radians(int(operator))))  # Convert degrees to radians, calculate cos
    operator = result
    InputText.set(result)

# Function to calculate tangent of current value (degrees)
def CalculateTan():
    global operator
    result = str(math.tan(math.radians(int(operator))))  # Convert degrees to radians, calculate tan
    operator = result
    InputText.set(result)

# Function to calculate cotangent of current value (degrees)
def CalculateCot():
    global operator
    result = str(1 / math.tan(math.radians(int(operator))))  # Compute 1/tan(theta) = cot(theta)
    operator = result
    InputText.set(result)

# Function to evaluate the complete expression ( = button )
def EqualButton():
    global operator
    temp = str(eval(operator))             # Evaluate expression using Python eval()
    InputText.set(temp)                    # Update display with result
    operator = temp                        # Update operator with result for further calculation

# Function to convert radians to degrees
def Calculatedeg():
    global operator
    result = str(math.degrees(float(operator)))  # Convert current value from radians to degrees
    operator = result
    InputText.set(result)

# Function to calculate arcsin of current value
def Calculateasin():
    global operator
    result = str(math.asin(math.radians(int(operator))))  # Calculate asin in radians
    operator = result
    InputText.set(result)

# Function to calculate arccos of current value
def Calculateacos():
    global operator
    result = str(math.acos(math.radians(int(operator))))  # Calculate acos in radians
    operator = result
    InputText.set(result)

# Function to calculate arctan of current value
def Calculateatan():
    global operator
    result = str(math.atan(math.radians(int(operator))))  # Calculate atan in radians
    operator = result
    InputText.set(result)

# Define some math functions and constants to use in eval() (so user can enter log, ln, sin, etc.)
log, ln = math.log10, math.log      # log base 10, natural log
sin, cos, tan = math.sin, math.cos, math.tan
deg, asin, acos, atan = math.degrees, math.asin, math.acos, math.atan
e = math.exp                       # e^x
p = math.pi                        # pi
E = '10*'                          # 10 to the power of (used in EXP button)

# Initialize operator string and input display variable
operator = ""                      # This will store the expression being entered
InputText = StringVar()            # Tkinter variable to update display dynamically

# Create display field (Entry widget)
display = Entry(calculator, font=('Arial', 20, 'bold'), textvariable=InputText,
                bd=10, insertwidth=6, bg='white', justify='left').grid(columnspan=5, padx=20, pady=20)

# Configure row and column weights for responsive resizing
Grid.rowconfigure(calculator, 0, weight=1)
for i in range(6):                 # Loop to configure 6 columns
    Grid.columnconfigure(calculator, i, weight=1)

# Define button styles
FunctionButtonConfig = {'bd': 5, 'fg': 'white', 'bg': 'green', 'font': ('Arial', 15, 'bold')}
NumberButtonConfig = {'bd': 5, 'fg': 'black', 'bg': 'red', 'font': ('Arial', 15, 'bold')}

# Now create all calculator buttons and attach them to the grid
# Each button calls the appropriate function or ClickButton() with its value

# Row 1 - sin, cos, tan, cot, pi
Button(calculator, FunctionButtonConfig, text='sin', command=CalculateSin).grid(row=1, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='cos', command=CalculateCos).grid(row=1, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='tan', command=CalculateTan).grid(row=1, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='cot', command=CalculateCot).grid(row=1, column=3, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='π', command=lambda: ClickButton(str(math.pi))).grid(row=1, column=4, sticky="NSEW")

# Row 2 - abs, e, factorial, integer division (//), modulo
Button(calculator, FunctionButtonConfig, text='abs', command=lambda: ClickButton('abs(')).grid(row=2, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='e', command=lambda: ClickButton(str(math.exp(1)))).grid(row=2, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='x!', command=CalculateFactorial).grid(row=2, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='div', command=lambda: ClickButton('//')).grid(row=2, column=3, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='mod', command=lambda: ClickButton('%')).grid(row=2, column=4, sticky="NSEW")

# Row 3 - powers
Button(calculator, FunctionButtonConfig, text='x²', command=lambda: ClickButton('**2')).grid(row=3, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='x³', command=lambda: ClickButton('**3')).grid(row=3, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='x^n', command=lambda: ClickButton('**')).grid(row=3, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='x⁻¹', command=lambda: ClickButton('**(-1)')).grid(row=3, column=3, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='10^x', command=lambda: ClickButton('10**')).grid(row=3, column=4, sticky="NSEW")

# Row 4 - roots and logs
Button(calculator, FunctionButtonConfig, text='²√', command=SquareRoot).grid(row=4, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='³√', command=ThirdRoot).grid(row=4, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='√', command=lambda: ClickButton('**(1/')).grid(row=4, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='log₁₀', command=lambda: ClickButton('log(')).grid(row=4, column=3, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='ln', command=lambda: ClickButton('ln(')).grid(row=4, column=4, sticky="NSEW")

# Row 5 - brackets, sign, percent, e^x
Button(calculator, FunctionButtonConfig, text='(', command=lambda: ClickButton('(')).grid(row=5, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text=')', command=lambda: ClickButton(')')).grid(row=5, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='±', command=ChangeSign).grid(row=5, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='%', command=percent).grid(row=5, column=3, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='e^x', command=lambda: ClickButton('e(')).grid(row=5, column=4, sticky="NSEW")

# Row 6 - degree, inverse trig, STOP
Button(calculator, FunctionButtonConfig, text='deg', command=Calculatedeg).grid(row=6, column=0, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='sin-1', command=Calculateasin).grid(row=6, column=1, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='cos-1', command=Calculateacos).grid(row=6, column=2, sticky="NSEW")
Button(calculator, FunctionButtonConfig, text='tan-1', command=Calculateatan).grid(row=6, column=3, sticky="NSEW")
Button(calculator, text="STOP", fg="black", bg="blue", font=('Arial', 15, 'bold'), command=calculator.destroy).grid(row=6, column=4, sticky="NSEW")

# Remaining rows - number buttons and basic operators
Button(calculator, NumberButtonConfig, text='7', command=lambda: ClickButton('7')).grid(row=7, column=0, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='8', command=lambda: ClickButton('8')).grid(row=7, column=1, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='9', command=lambda: ClickButton('9')).grid(row=7, column=2, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='DEL', command=DeleteButton).grid(row=7, column=3, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='AC', command=ClearAllData).grid(row=7, column=4, sticky="NSEW")

Button(calculator, NumberButtonConfig, text='4', command=lambda: ClickButton('4')).grid(row=8, column=0, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='5', command=lambda: ClickButton('5')).grid(row=8, column=1, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='6', command=lambda: ClickButton('6')).grid(row=8, column=2, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='*', command=lambda: ClickButton('*')).grid(row=8, column=3, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='/', command=lambda: ClickButton('/')).grid(row=8, column=4, sticky="NSEW")

Button(calculator, NumberButtonConfig, text='1', command=lambda: ClickButton('1')).grid(row=9, column=0, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='2', command=lambda: ClickButton('2')).grid(row=9, column=1, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='3', command=lambda: ClickButton('3')).grid(row=9, column=2, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='+', command=lambda: ClickButton('+')).grid(row=9, column=3, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='-', command=lambda: ClickButton('-')).grid(row=9, column=4, sticky="NSEW")

Button(calculator, NumberButtonConfig, text='0', command=lambda: ClickButton('0')).grid(row=10, column=0, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='.', command=lambda: ClickButton('.')).grid(row=10, column=1, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='EXP', command=lambda: ClickButton(E)).grid(row=10, column=2, sticky="NSEW")
Button(calculator, NumberButtonConfig, text='=', command=EqualButton).grid(row=10, columnspan=2, column=3, sticky="NSEW")

# Start main Tkinter event loop (this keeps the window open)
calculator.mainloop()

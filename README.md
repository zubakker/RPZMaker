# How to install

## 1. Downloading

[Mac/Linux] If you have git installed:

```
$ git clone https://github.com/zubakker/RPZMaker.git && cd RPZMaker
```

Otherwise download the .zip file and unzip it.

## 2. Installing modules

* Firstly install python
* (Optionally) Create a virtual environment and activate it:
  ```
  [Mac/Linux] $ python -m venv venv && source venv/bin/activate
  [Windows] $ python -m venv venv && venv\Scripts\activate.bat
  ```
* Install required modules:
  ```
  $ pip install -r requirements.txt
  ```
## 3. Installing pandoc

Rendering .md files to .html files is handled by default by using pandoc, for a smooth user expirience recommend installing it, otherwise you will be forced to modify po_run.sh changing the .md->.html renderer
able to render equations in KaTeX to your desired one.

# How to use

By default the program is set up for BMSTU's gearbox design settlement note which consists of design and verification calculations.

## If you want to design a gearbox

There are four files you'd want to change:
* kp_1_c.json and kp_2_c.json house all the user-defined constants used in the calculation such as engine parameters,
  parameters of the technical specifications, constants obtained from GOST and literature as well as design solutions such as gear ratios and shaft diameters,
  kp_1_c and kp_2_c are for the design and verification parts respectively. Files are structured as lists of pairs of strings in json format. The first string
  defines the constant in LaTeX format and the second string is used for clarification purposes, not at all included included in final document. If you want
  to create an empy line (e.g. for devision into subsections) you should leave the first string in a pair empty. Example of a minimalistic kp_1_c.json:
  ```
  [
    [""          "--- Earth planet parameters ---"],
    ["R = 6.371 \\cdot 10^6",   "meters, radius of planet earth"],
    ["\\mu = 5.972",            "e24 kg, mass of planet earth"]
  ]
  ```
* kp_1_f.json and kp_2_f.json contain all the formulae including equations, inequations and declarations, used for design and verification calculations respectively
  in a list of strings in LaTeX format. Unlike constant files in here formulae are strictly ordered and will be inserted into the document in the same order they are
  listed. Formulae come in three main types:
  1. Declarations contain only one equal sign (following the previous example): ``` "\\rho = \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}"``` results in: $\rho = \frac{4}{3} \frac{\pi \cdot R^3}{\mu}$, which are not calculated and used to declare
     how a variable is calculated, which will be later broken down into smaller parts (e.g. $A = \frac{B}{C}$, where $B = D \cdot E$, where $E = K^{F}$ and so on, and A
     can not be calculated directly from constants and needs intermediate calculations)
  2. Equations contain multiple equal signs (following the previous example): ``` "\\rho = \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu} =="``` results in: $\rho = \frac{4}{3} \frac{\pi \cdot R^3}{\mu} =
     \frac{4}{3} \frac{3.1415 \cdot (6.371 \\cdot 10^6)^3}{5.972} = 4468518.97745$.
  3. Inequations contain no equal signs (hopefully contain ">", "<", "\leq", "\geq", etc.) (following the previous example): ``` "\\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu} =="``` will result in one of two things:
       if all the variables in inequation are already known (imported from constants or calculated in previdous equations (not declarations)) it will result in a checkup: ```"\\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}"``` results in
       $$\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}$$ $$(8.88 \geq 5.51)$$ (with $\rho = 8.88$)
       if not all variables in inequation are already known it will result without checkup: ```"\\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}"``` results in just  $$\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}$$
     
## If you want a custom settlement note

Besides teh above mentioned constant and formula files you'd want to edit kp_r_1_clean.md and kp_r_2_clean.md files, which are written in markdown format. Two things to consider:
1. The formulas will only be inserted in parts of .md file marked with "\$\$\$\$" (must be separated by a newline in the middle), only in the order listed in _f files
2. If needed values of constants and previously calculated variablies  may be inserted into the document with "\$" on both sides (e.g. in tables or paragraphs of texts like " $A = B \cdot C$, with $B = 6.6743 \cdot 10^{-11} m^3 \cdot kp^{-1} \cdot sec^{-2}$, the gravitational constant"
   can be dynamically achieved by rendering .md file "\$\$\n\$\$, with \$B = \$ \$ B \$ \$ m^3 \cdot kp^{-1} \cdot sec^{-2} \$, the gravitational constant", with "\n" as newline symbol)

## How to run

To run the program on MacOs/Linux you need to be in the right directory, activate venv and run 
```
$ bash po_run.sh
```
After loading all the constans the program will demand a user input -- the number of the line to start from. For the first time I suggest to leave it blank and simply press the enter key twice.
If you are handling a large settlement note with full calculation time nearing tens of minutes and you know that you changed something only used in the very end you can specify the exact formula number
to recalculate from (the numbers of currently calculated formulae are displayed in the left of the lines of the ouput), the reculculation will start around the number you inputed (plus or minus one line)
Incase you want to combine both calculations into one, you'd have to modify the source code of lang_f.py, lang_c.py and main.py to reflect the exclusion of the second part.

## An important notice

Because of technical limitations the main.py can't work with files containing anything but ascii characters, so I've had to write supplementory lang_c.py and lang_f.py and lang.py programms to convert unicode
characters into ascii (using alt-codes) and back, but because of that no formula can contain the uppercase Z, otherwise the translation back-and-forth between ascii and unicode will be broken. Feel free to
fix my code and solve this problem.

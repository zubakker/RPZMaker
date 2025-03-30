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

Rendering .md files to .html files is handled by pandoc by default, for 
a smooth user expirience installing it is recommended, otherwise you will be
forced to modify po_run.sh changing the .md->.html renderer able to render 
equations in KaTeX to your desired one.

# How to use

By default the program is set up for BMSTU's monocular design settlement 
note.


There are three files you'd want to change:

* inp_constants.json houses all the user-defined constants used in the 
  calculation such as engine parameters, parameters of the technical 
  specifications, constants obtained from GOST and literature as well as 
  design solutions such as gear ratios and shaft diameters. The order of
  constants does not affect the finished document.

  The file is structured as a list of three of strings in json format: 
  1. The first string defines the constant, it can be filled out in four 
     ways: 
     a) An empty string will make the whole line being ignored, 
     it can be used for structuring a document and for writing comments; 
     b) An equation int LaTeX format defines the value of a constant, the 
     right side should be a number (e.g. ```"A = 12.3"```);
     c) A declaration of a constant meaning, used in "with" blocks detailed
     below, for this purpose the value should be \NULL 
     (e.g. ```"B = \\NULL"```);
     d) A declaration of a constant value, when it is not a number, used in
     insertion of values, detailed below, the name of the constant should be
     followed by a colon (e.g. ```"C: MyValue"```).
  2. The second string is used for comments, as a part of a "with" block,
     clarification of document structure purposes, depending on the first
     string.   
  3. The third string will be ignored by program, but can be used for 
     additional comments that will not be used in a "with" block, it can
     be anything you want, for example units of measurement.

  ```
  [
    [""          "--- Earth planet parameters ---",         ""],
    ["R = 6.371 \\cdot 10^6",   "radius of planet earth",   "m"],
    ["\\mu = 5.972",            "mass of planet earth",     "e24 kg"],
    ["planet_name: earth",      "the name of the planet",   ""],
    ["G = \\NULL",              "the value of gravity",     ""]
  ]
  ```

* inp_formulas.json houses all the formulas including equations, inequations
  and declarations, used for the calculations. The formulas will be inserted
  into the resulting document in the order they are listed here.

  The file is structured as a list of five strings or numbers in json 
  format: 
  1. The first string defines a formula, it can be filled out in three ways:
     a) An equation contains two or more equals signs, the variables will
     be replaced by their number values in the output document and the 
     value will be calculated, rounded to the needed precision, detailed
     below
     (e.g. ```"\\rho = \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu} ="``` 
     results in: 
     $$\rho = \frac{4}{3} \frac{\pi \cdot R^3}{\mu} =
     \frac{4}{3} \frac{3.1415 \cdot (6.371 \cdot 10^6)^3}{5.972} = 
     4468518.97745$$
     );
     b) A declaration contains exactly one equals sign, the constants will
     not be replaced by their number values in the output document and will
     be inserted unchanged. It can be used as a thing you want to calculate
     later in the document but don't have the variable values yet 
     (e.g. ```"A = B \\cdot C"``` will result in $A = B \cdot C$)
     c) An inequation contains no equals signs (hopefully it contains one 
     ">", "<", "\leq" or "\geq", etc.). If all the variables in inequation 
     are already known (imported from constants or calculated in previdous 
     equations (not declarations)) it will result in a checkup: 
     ```"\\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}"``` 
     results in:

       $$\rho \geq \frac{4}{3} \frac{\pi \cdot R^3}{\mu} \\
       (8.88 \geq 5.51) \\
        True $$
     if not all variables in inequation are already known it will stay 
     without checkup: 
     ```"\\rho \\geq \\frac{4}{3} \\frac{\\pi \cdot R^3}{\\mu}"``` 
     results in just $$\rho \geq \frac{4}{3} \frac{\pi \cdot R^3}{\mu}$$
  2. The second string contains a comment used in a "with" block. If the 
     "with" block is enabled for this formula (currently supported for 
     equations and declarations) after the formula a "with" block will be
     inserted into the document, (e.g. following the example from above,
     a line like 
     ```["A = R \\cdot \\mu", "the meaning of A", ...]``` will result in
     $$A = R \cdot \mu,$$
     with $A$ -- the meaning of A; <br>
     $R$ -- radius of planet earth; <br>
     $\mu$ -- mass of planet earth.
     ) So the second string is used for the meaning of the variable on the
     left side of the first equals sign. Don't forget to change the WITH
     constant in main.py to your version of the word used in this block.
  3. The third element is a "with" block flag, if it is false 
     (e.g. an empty string, the number zero, false, none, etc.)
     a "with" block will not be generated, if the flag is true, it will be
     generated and inserted into the document.
  4. The fourth element is the rounding precision, if it is an integer, the
     result of the equation will be rounded to the number of decimal points
     specified in this element. It can be negative, which will result in the
     rounding beyond the decimal point (e.g. a number 123.4 rounded to 0 
     decimal points will result in 123, rounded to -1 decimal points will 
     result in 120). By default the rounding precision is set to 5. The 
     rounding precision is purely for the formula rendering, internally all
     variables are stored unrounded and placed in next calculations and as
     value inserts also without rounding.
  5. The fifth element is a LaTeX string containing the units of measurement
     for this formula, which will be added to the end of the equation 
     exactly (e.g. if B = 3 and C = 4, 
     ```["A = B + C =","","","","(mm)^{-1}"]``` 
     will result in
     $$ A = B + C = 3 + 4 = 7(mm)^{-1} $$
     ).

* inp_template.md as the name implices houses the template of the resulting
  document, for the most part the output is the input template with the 
  following changes:
  1. A formula block is an empty line, followed by a line of two dollar 
     signs, then two more dollar signs on the next line and an empy line
     afterwards, so ```"\n$$\n$$\n"``` with ```"\n"``` -- denoting a 
     linebreak. In the output document a formula will be inserted between
     the four dollar signs, the contents described above. Formula blocks
     can be chained together not requiring multiple empty lines, so two of
     them in a row can look like this ```"\n$$\n$$\n\n$$\n$$\n"```.
  2. An insertion of a value is the butchered name of the variable in curly
     brackets. The butchering is detailed below. So, following the example
     above if you wanted to have the value of $R$ and the planet name 
     inserted into the text the input template should contain something 
     like this: 
     ```"And as for the {planet_name}, it's mass is {mu} kg"```
     which will be rendered as: 
     "And as for the earth, it's mass is 5.972 kg".
     Value insertion can be used anywhere in the input template, including
     text, tables, paragraphs, etc. Inserted values can come from both
     constants and previous formula calculations. Value insertion happens 
     before the formula calculation, so it cannot be used inside a "with" 
     block, or anywhere else inside the formula. 
  3. Because the curly brackets are used for value insertion, if you want
     to use them in text, you have to use doubled brackets: so if you wanted
     to get "And the $R_{earth}$ is" in the output document, you'd have to
     have ```'And the $R_{{earth}}$ is"``` in the input template.


## How to run

To run the program on MacOs/Linux you need to be in the right directory, 
activate venv and run 
```
$ bash po_run.sh
```
After loading all the constans the program will demand a user input -- the 
number of the line to start from. For the first time it should be left 
blank by pressing the enter key.

If you are handling a large settlement note with full calculation time 
nearing tens of minutes and you know that you changed something only used at
the very end you can specify the exact formula number to recalculate from 
(the numbers of currently calculated formulas are displayed in the beginning 
of the lines of the ouput), the reculculation will start around the number 
you inputed (plus or minus one line)

The program will output a out.html and out_calculated.md documents which can
then be modified to suit your needs, **be warned**: the changes to both 
documents are temporary and will be removed when running the program again, 
to change the output permanently you should reflect the desired changes in 
the inp_template.md document.


## Limitations

1. Because of technical limitations the main.py can't work with files 
   containing anything but ascii characters, so I've had to write 
   supplementory lang_c.py and lang_f.py and lang.py programms to convert 
   unicode characters into ascii (using alt-codes) and back, but because of 
   that no formula can contain the uppercase Z, otherwise the translation 
   back-and-forth between ascii and unicode will be broken. Feel free to fix
   my code and solve this problem.
2. The RPZMaker is able to comprehend and perform only simple calculations: 
   addition, subtraction, multiplication, fractions, roots, exponentiation
   and trigonotry. It cannot calculate matrices, deriviatives and other
   advanced calculus and will break when faced with such things. If you want
   to use the summation operator $\sum$ you'd have to use capital sigma 
   $\Sigma$ instead and you'd have to also clarify the full formula, 
   e.g. $$\sum_{i = 1}^{3} 2^i$$ will have to be changed to 
   $\Sigma_{i = 1}^{3} 2^i = 2^1 + 2^2 + 2^3$ and if a variable is declared 
   by using a summation $A = \Sigma_{i = 1}^{10} B_i \cdot C_i^{3}$ you'd
   have to substitute the summation with a full sequence 
   $A = B_1 \cdot C_1^3 + B_2 \cdot C_2^3 + .. + B_{10} \cdot C_{10}^3$. 
   Similar substitutions will have to be made for advanced calculus. If you 
   are not satisfied with ```"\Sigma"``` and want a ```"\sum"``` you'll have
   to manually replace it in the output document or change the po_run.sh.
3. The longer the variable name and formula the more time the RPZMaker will 
   take to decipher it (the deciphering time rises by ~ the square of 
   length), so consider avoiding variable names like 
   ```"Mode_{production}"``` and replacing it with something like 
   ```"M_{p}"``` or ```"M_{pr}"```.
4. The automated insertion of constant values is not fully consistent when 
   it comes to subscripts and the aforementioned ```"M_{production}"``` may 
   be internally represented like ```"M_{ooprductin}"``` (the above 
   mentioned name butchering) and so when attempting to insert the value of 
   ```"M_{production}"``` the program will break as it does not have this 
   value and only has ```"M_{ooprductin}"```, to fix that you will have to 
   specify the butchered name in your template document like so 
   ```"{M_(ooprductin)}"```. To check for such name butchering carefully 
   read the "outname" of the program's output or "var" when reading the 
   constants
5. Fractions are weirdly displayed: ```"\frac{3.3}{2.2}"``` in the forumula 
   file will be displayed as $3.3 \cdot 2.2^{-1}$, it only works like that 
   when a fraction consists entirely of numbers (e.g. in equation when 
   substituting variable names for their values). Sadly there is nothing I 
   can do about it, it is just a quirk of sympy.
6. Multiple numbers in subscripts seem to also break sympy, so 
   ```"A_{00}"``` might not work, consider avoiding it or replacing with 
   less a elegant ```"A_{O0}"```.
7. Sadly sympy doesn't like variable names with apostrophes, because of that
   in the monocular calculations provided here have the unelegant solution
   of changing the apostrophe to a subscript capital letter Omicron. Similar
   (maybe smarter) solutions would have to be implemented if your 
   calculations require special characters like apostrophes.

# Plans for the future

1. I hope in one day adding the ability to adaptively calculate similar 
   equations iteratively, so ```"A_{1} = B_{1} \cdot C_{1} =="```, 
   ```"A_{2} = B_{2} \cdot C_{2} =="``` and so on could be written 
   something like ```"A_{i} = B_{i} \cdot C_{i} == with 0 > i > 99"``` and 
   the program would automatically generate the apropriate number of 
   equations depending on how many ```"C_{i}"``` and ```"B_{i}"``` you have 
   in your constant and previous formula files, so if you have up to 
   ```"C_{16}"``` it would create sixteen identical equations and make 
   space for them in the .md document.
2. Specifying the rounding precision in inserted values.
3. External calculation of formulas. It goes a bit away from the philosopy
   of only the input files dictating the output, but the way it is now, to
   fully recalculate the whole document from step zero with a different set
   of initial data would require constant restarts and human intervention.
   So imagine you have a calculation of a person's shoe size and the formula
   results in 23.743, but the settlement note demands an integer number and
   the only options are 17 and 25, so you have to calculate to this point, 
   then go to the constants file and set the decided shoe size = 25. It
   could become tedious as there can be multiple things like that and they
   require checking every time you tweak the previous ones, so I had the 
   idea of support for external calculations. The way I have invisioned it
   it would be another python file with a function that is called when 
   the formula line in the formula file starts with for example "EXT:",
   the variable name after the "EXT:" would be sent to the function as well
   as the dict of all currently calculated values, then based on which 
   variable name specifically was passed, the function would calculate them
   in their individual ways. You could go crazy with this concep, making
   the external function create plots based on data and save them in the 
   directory, or running advanced calculus or consulting some regulatory 
   tables, or anything else with external libraries.

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

# In-class exercise 1

Modify stock price example as follows:  Instead of only reporting maximum increase, report
both max decrease and max increase; give the absolute value of each, with decrease first.
If the stock had no decrease or no increase, fill in -1 for that value.

E.g. for input file

Goog, 230, 240
Apple, 100, 98
MS, 300, 250
MS, 250, 260
MS, 270, 280
Goog, 220, 215
Goog, 300, 350
IBM, 80, 90
IBM, 90, 85

output is:

Apple	0.020000, -1.000000
Goog	0.022727, 0.166667
IBM	0.055556, 0.125000
MS	0.166667, 0.040000

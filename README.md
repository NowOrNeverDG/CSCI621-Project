# CSCI621-Project
CSCI621_Programming Language code

Instrutor: Dr.Lee

------
InfixToProfix

 Examples:
| INFIX     | POLISH POSTFIX  |
| --------- | ------------    |
| a*b+c     | ab*c+           |
| a+b*c     | abc*+           |

------

Non-recursive Predictive Parser & Recursive Descent Parser

Parse table for this parser is shown as follows:

|      | d             | ^     | ,              | $         |
|------| --------------|-------|----------------|-----------|
|elist |elist→ e elist’|       |                |           |
|elist’|               |       |elist’ → , elist|elist’ → ε |
|e     |               |e’→ ^ e|e’ → ε          |e’ → ε     |
|n     |n → d n’       |       |                |           |
|n’    |n’ →n          |n’ → ε|n’ → ε           |n’ → ε     |

Design and implement a Non-recursive Predictive Parser (NPP) for the following
grammar:
<elist> → <elist> , <e> | <e>
<e> → <n> ^ <e> | <n>
<n> → <n> <d> | <d>
<d> → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
  
-------

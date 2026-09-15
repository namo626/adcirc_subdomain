# adcirc-subdomain

Creates in the current directory a copy of `fort.14` called `fort.14.renum` which has the correct numbering of nodes.
This is used to renumber a mesh belonging to an ADCIRC subdomain which by default still contains the full-domain numbering, and hence cannot be
read by programs like FigureGen.

## Installation and usage

Clone this repo and run
```
pip install .
```

Then simply call 
```
adcirc-subdomain
```

in the directory containing the `fort.14` to be renumbered. This does not modify the original file.

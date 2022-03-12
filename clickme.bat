@echo off
:SAMPLE
echo building HTML file at out/ ...
py -m nbconvert src/AI_CA1.ipynb --execute --to "html" --theme "dark" --output-dir "out"
echo done
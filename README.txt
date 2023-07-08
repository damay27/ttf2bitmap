This is a helper script written in python for converting TrueType fonts to
rasterized glyph sheets.

Setup Instructions:
    1. Create a python virtual enviroment.
        python -m venv venv
    2. Source the virtual enviroment.
    3. Install the required packages with this command
        pip install -r ./requirements.txt

Usage Instructions:
    Show the help message:
        python ./ttf2bitmap.py --help
    Create a glyph sheet using the default scale factor and output name:
        python ./ttf2bitmap.py <path to ttf file>
    Create a glyph sheet using a custom scale factor and output name:
        python ./ttf2bitmap.py <path to ttf file> --scale 10 --output custom.png

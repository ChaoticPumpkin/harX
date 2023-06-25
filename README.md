# HAR eXtractor
`.har` file extractor for *Pikmin 1+2* on switch. It should work with *Super Mario 3D All-stars*, but that is currently untested.

# Usage
`python harX.py file_path`

# About
The `.har` file format appears to just be multiple PNGs concatenated together, with a little extra padding and information. This script searches for the PNG magic headers and extracts them based off that.

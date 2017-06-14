# Server script for [OSDTetris](https://github.com/thy2134/OSDTetris)

## Prequisites
- flask 
- tinydb
- This program uses port 5000, so this port should be open both inbound / outboundß
## Installation
1. Install dependencies with 

    `pip install flask cython tinydb` (Windows / Linux)
    
    `pip3 install flask cython tinydb` (macOS)

2. Start server with command 

    `FLASK_APP = server.py python -m flask run --host=0.0.0.0` (Linux)

    `FLASK_APP = server.py python3 -m flask run --host=0.0.0.0` (macOS)

    (Windows: idk u figure out)
        

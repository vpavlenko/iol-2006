#!/bin/bash

set -x

cd ILO4_Team1
python3 gen.py
cd ..

cd ILO4_Team2
python3 gen.py
cd ..

cd ILO4_Team3
python3 gen.py
cd ..

cd ILO4_Team4
python3 gen.py
cd ..

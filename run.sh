#!/bin/bash
padsp julius -input mic -C $HOME/project/julius-grammer/julian.jconf | python -u $HOME/project/pythonControls/getcommand.py

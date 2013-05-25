#!/bin/bash
#nohup 
padsp julius -input mic -C $HOME/project/julius-grammer/julian.jconf | python $HOME/project/pythonControls/getcommand.py
#nohup python main.py &

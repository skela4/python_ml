#!/bin/bash

curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" && sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH && conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle && conda activate 42AI-$USER && source ~/.zshrc

#! /bin/bash

cd ..
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
export PATH="/projects/$(echo ${PWD##*/})/miniconda3/bin:$PATH" >>~/.bash_profile
cd CV-Notebooks-Summer-2022
conda env create -f CVReq.yml -n cv_env

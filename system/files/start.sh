#!/bin/bash
/etc/init.d/atd start     # to detect file changes
/etc/init.d/xinetd start  # for rsync test
echo "alias ll='ls -alF'" > ~/.bash_profile
echo "export EDITOR=vi" >> ~/.bash_profile
echo "export WZDAT_CFG=$WZDAT_CFG" >> ~/.bash_profile
echo "export WZDAT_DIR=$WZDAT_DIR" >> ~/.bash_profile
mkdir -p /logdata/_var_
cd /wzdat
pip install -e .
# Re-install of requirements to apply changes after base image build.
pip install -r requirements.txt
python -m wzdat.rundb create
python -m wzdat.jobs cache-all
/usr/bin/supervisord
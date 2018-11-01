#!/bin/bash

if [ -d 'ENV' ]; then
	echo 'ENV seems to be created. Remove if you want to refresh it'
	exit 1
fi

if [ ! -f /usr/bin/pyvenv ]; then
    echo 'Install python3-venv package to get /usr/bin/pyvenv executable'
    exit 1
fi

echo '* Creating the ENV'
python3 -m venv ENV || exit 1

echo '* Installing requirements'
. ./ENV/bin/activate

pip3 install --upgrade setuptools pip || exit 1
pip3 install wheel || exit 1
pip3 install -r backend/requirements.txt || exit 1
pip3 install -r backend/requirements-dev.txt || exit 1

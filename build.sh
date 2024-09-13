#! /bin/bash

rm -r build
pip install poetry

poetry install --no-dev
mkdir build && cd build
cp -r $(poetry env info -p)/lib/*/site-packages/* .
cp -r ../data_importer .
cp ../handler.py .
zip -r ../cr-ai-data-importer-dev.zip .
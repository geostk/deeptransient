#!/usr/bin/env sh

echo "Downloading TransientNet models..."

wget http://cs.uky.edu/~rbalten/transient/data/transientnet_models.tar

echo "Extracting TransientNet models..."

tar -xvf transientnet_models.tar
rm transientnet_models.tar

echo "Done."

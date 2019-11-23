#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb

EXAMPLE=./
DATA=./dataset
TOOLS=../build/tools

$TOOLS/compute_image_mean $EXAMPLE/train_lmdb \
  $DATA/mean.binaryproto

echo "Done."

#!/usr/bin/env sh

name='tetris-clone'
cd "files"      # move into directory to set it as root of the archive
zip -9 -r "../bin/${name}.love" .

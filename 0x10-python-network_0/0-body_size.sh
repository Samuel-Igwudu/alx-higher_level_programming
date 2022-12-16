#!/bin/bash
# shows the content lenght
curl -sI "$1" | grep "Content-Lenght:" | cut -d " " -f 2

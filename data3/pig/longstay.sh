#!/bin/bash

awk 'BEGIN { FS="\t"; OFS="\t" }
     $4 > 3'

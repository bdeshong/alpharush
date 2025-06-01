#!/bin/bash

# Get the absolute path of the api/src directory
API_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/src"

# Add the api/src directory to PYTHONPATH
export PYTHONPATH="${API_DIR}:${PYTHONPATH}"

# Print confirmation
echo "PYTHONPATH set to: ${PYTHONPATH}"

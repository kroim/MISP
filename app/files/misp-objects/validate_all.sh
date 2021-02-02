#!/bin/bash

set -e
set -x

./jq_all_the_things.sh

diffs=`git status --porcelain | wc -l`

if ! [ $diffs -eq 0 ]; then
	echo "Please make sure you run ./jq_all_the_things.sh before commiting."
	exit 1
fi

# remove the exec flag on the json files
find -name "*.json" -exec chmod -x "{}" \;

diffs=`git status --porcelain | wc -l`

if ! [ $diffs -eq 0 ]; then
    echo "Please make sure you run remove the executable flag on the json files before commiting: find -name "*.json" -exec chmod -x \"{}\" \\;"
    exit 1
fi


for dir in objects/*/definition.json
do
  echo -n "${dir}: "
  jsonschema -i ${dir} schema_objects.json
  echo ''
done

jsonschema -i relationships/definition.json schema_relationships.json

./unique_uuid.py

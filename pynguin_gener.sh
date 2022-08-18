#!/bin/bash
source ./venv/bin/activate
export PYNGUIN_DANGER_AWARE=1
for i in $(ls src/models/*); do
    module_name=$(basename src/models/$i | cut -f1 -d\.)
    pynguin   --project-path . --output-path tests/pynguin -v --module-name src.models.$module_name

done
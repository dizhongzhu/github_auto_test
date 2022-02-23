#!/bin/bash


# run unit tests in virtualenv
python3 -m pytest --verbose \
  --junitxml=test-reports/pytest.xml \
  test/utils/UT_simple_math.py \
  --disable-warnings

if [ $? -ne 0 ]; then
  echo -e " ${RED}unit tests failed${NC}"
  exit 1
fi

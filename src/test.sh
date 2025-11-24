#!/bin/bash

output=$(node src/app.js "Youssef")

expected="Hello, Youssef"


echo "Running greet.js..."
echo "Output: $output"

if [ "$output" = "$expected" ]; then
    echo "Test Passed ✔️"
    exit 0
else
    echo "Test Failed ❌"
    echo "Expected: $expected"
    exit 1
fi

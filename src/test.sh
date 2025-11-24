#!/bin/bash

# شغّل السكريبت وتحقق من الناتج
output=$(node app.js)

# النتيجة المتوقعة
expected="Hello, World"

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

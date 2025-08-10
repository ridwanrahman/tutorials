#!/bin/bash

user_input_number() {
    echo "Please enter a number: "
    read number # number is available globally
}

valida_user_input() {
    if [[ "$number" =~ ^[+-]?[0-9]+$ ]]; then
        echo "it is a number"

    else
        echo "it is not a number you have to enter a number"
        exit 1
    fi
}

# Main execution
user_input_number
if valida_user_input; then
    echo "You entered: $number"

    # Demonstrate number usage
    if [[ "$number"  -gt 0 ]]; then
        echo "The number is postive"
    elif [[ "$number" -lt 0 ]]; then
        echo "The number is negative"
    else
        echo "The number is zero"
    fi
else
    echo "Validation failed"
    exit 1
fi

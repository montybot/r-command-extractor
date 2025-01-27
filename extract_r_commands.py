#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  extractRfromOrg.py
#  
#  Copyright 2025 Michaël Gilbert <https://github.com/montybot>
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
import re
import sys

def extract_r_commands(org_file):
    """Extract all R commands from an Org mode file."""
    try:
        with open(org_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regular expression to identify R code blocks
        r_code_blocks = re.findall(r'#\+BEGIN_SRC R.*?\n(.*?)#\+END_SRC', content, re.DOTALL)

        # Extract R commands from each block
        r_commands = []
        for block in r_code_blocks:
            # Remove empty lines and strip whitespace
            commands = [line.strip() for line in block.split('\n') if line.strip()]
            r_commands.extend(commands)

        return r_commands

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{org_file}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading '{org_file}': {str(e)}")

def save_r_commands_to_file(r_commands, output_file):
    """Save the extracted R commands to a destination file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for command in r_commands:
                file.write(command + '\n')
    except Exception as e:
        raise Exception(f"An error occurred while writing to '{output_file}': {str(e)}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python extract_r_commands.py <source_file.org> <destination_file.txt>")
        print("Example: python extract_r_commands.py example.org r_commands.txt")
        sys.exit(1)

    # Get the arguments
    org_file = sys.argv[1]  # Source Org mode file
    output_file = sys.argv[2]  # Destination file

    try:
        # Extract R commands
        r_commands = extract_r_commands(org_file)

        # Save the R commands to the destination file
        save_r_commands_to_file(r_commands, output_file)

        print(f"R commands have been extracted and saved to '{output_file}'.")

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()

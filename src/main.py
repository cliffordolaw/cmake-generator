"""
src/main.py

This script serves as the entry point for the CMake Generator tool. It
parses a provided build log file, extracts compiler and linker options,
and generates a CMakeLists.txt file based on the parsed data.

Usage:
    python main.py --log <path_to_build_log> --output <output_file>

Command-line Arguments:
- --log: Path to the build log file to parse (required).
- --output: Path for the generated CMakeLists.txt file (optional, defaults to CMakeLists.txt).
"""

import argparse
from log_parser import parse_build_log
from cmake_generator import generate_cmake_content

def main():
    """Parse command line arguments and generate CMakeLists.txt from build logs."""
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate CMakeLists.txt from build logs.")
    parser.add_argument(
        "--log",
        required=True,
        help="Path to the build log file to parse."
    )
    parser.add_argument(
        "--output",
        default="CMakeLists.txt",
        help="Output path for the generated CMakeLists.txt file."
    )
    args = parser.parse_args()

    # Parse the build log
    print(f"Parsing build log: {args.log}")
    build_data = parse_build_log(args.log)
    if not build_data:
        print("Error: No valid data parsed from build log.")
        return

    # Generate CMake content
    print("Generating CMakeLists.txt content...")
    cmake_content = generate_cmake_content(build_data)

    # Write the CMakeLists.txt file
    try:
        with open(args.output, "w",encoding="utf-8") as cmake_file:
            cmake_file.write(cmake_content)
        print(f"CMakeLists.txt generated successfully at: {args.output}")
    except IOError as e:
        print(f"Error writing to output file {args.output}: {e}")

if __name__ == "__main__":
    main()

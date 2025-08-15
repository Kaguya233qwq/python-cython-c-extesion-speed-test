# python-cython-c-extension-speed-test

[English](./README.en.md) | [中文](./README.md)

## Overview

A benchmark project comparing the execution speed of pure Python, C extensions, and Cython.

The structure of this project is also designed to serve as a starter template for developers building Python C extensions and Cython modules in VS Code.

## Prerequisites

1.  **Python Installation**: Make sure you have Python installed, including the development headers. You can verify this by checking for the existence of the `python.h` file.

2.  **VS Code Extension**: This project is configured for VS Code. Please install the official [C/C++ extension from Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools).

3.  **Package Manager**: Install `uv`, a high-performance Python package installer and resolver.

## Configuration

In the project's `.vscode` directory, open the `c_cpp_properties.json` file.

Find the line with `"path/to/your/python/include"` and replace it with the actual path to your Python installation's `include` directory.

## Sync Dependencies

Run the following command to install the necessary dependencies using `uv`:

```bash
uv sync
```

## Building the C Extension and Cython Module
On Windows:

```cmd
.\build.bat
```

On Linux/macOS:

```bash
chmod +x build.sh
./build.sh
```

This script will compile the code and generate the binary extension modules (e.g., .pyd on Windows or .so on Linux/macOS) in the src directory. These files can then be directly imported by Python.

## Running the Test
To run the speed benchmark, execute:

```bash
uv run main.py
```

## Results

Both the Cython and C extension versions deliver comparable and significant performance gains, running 50-70 times faster than the pure Python implementation.
In most test runs, the Cython version shows a slight edge, outperforming the C extension by an additional 2%-8%.
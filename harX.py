import os
import sys

def find_png_chunks(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        magic = b'\x89\x50\x4E\x47'  # PNG magic value

        start = 0
        chunk_count = 1
        while True:
            # Find the next occurrence of the PNG magic
            chunk_start = data.find(magic, start)
            if chunk_start == -1:
                break

            # Find the end of the chunk
            chunk_end = data.find(magic, chunk_start + 1)
            if chunk_end == -1:
                chunk_end = len(data)

            # Extract the chunk
            chunk = data[chunk_start:chunk_end]
            start = chunk_end

            # Save the chunk as a PNG file
            filename = f"extracted{chunk_count}.png"
            with open(filename, 'wb') as output_file:
                output_file.write(chunk)

            chunk_count += 1

            # If the chunk end is the end of the file, break the loop
            if chunk_end == len(data):
                break


# Check if the file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("== HAR eXtractor ==")
    print("Usage: python harX.py file_path")
else:
    file_path = sys.argv[1]
    with open(file_path, 'rb') as file:
        header = file.read(4)

    if header == b'\x48\x41\x52\x43':
        find_png_chunks(file_path)
    else:
        print("Invalid file.")


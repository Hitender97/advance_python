def read_last_n_lines(file_name, n):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Check if n is greater than the number of lines
        if n > len(lines):
            n = len(lines)  # If n is too large, just return all lines

        # Get the last n lines
        last_n_lines = lines[-n:]

        # Print each line
        for line in last_n_lines:
            print(line, end='')

# Example usage:
file_name = "example.txt"
n = 5  # Number of lines to read from the end of the file
read_last_n_lines(file_name, n)


def read_last_n_lines(file_name, n):
    with open(file_name, 'rb') as file:
        file.seek(0, 2)  # Go to the end of the file
        file_size = file.tell()
        
        # Move backward in the file to read the last n lines
        buffer = bytearray()
        count = 0
        for i in range(file_size - 1, -1, -1):
            file.seek(i)
            byte = file.read(1)
            if byte == b'\n':
                count += 1
                if count > n:
                    break
            buffer.extend(byte)
        
        # Reverse the buffer since we read backward
        last_lines = buffer[::-1].decode('utf-8')
        print(last_lines)
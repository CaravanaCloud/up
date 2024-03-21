def parse_doclets(file_path):
    # Define the list of Docker keywords
    docker_keywords = [
        "FROM", "LABEL", "RUN", "CMD", "EXPOSE", "ENV", "ADD", "COPY", "ENTRYPOINT",
        "VOLUME", "USER", "WORKDIR", "ARG", "ONBUILD", "STOPSIGNAL", "HEALTHCHECK", "SHELL"
    ]
    
    # Define the list of comment delimiters
    comment_delimiters = ['#', '//', '*', '/*']
    
    # Initialize an empty dictionary to hold the results
    docker_declarations = {}
    
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line starts with any of the comment delimiters
            if any(line.lstrip().startswith(delimiter) for delimiter in comment_delimiters):
                # Remove the comment delimiter and leading/trailing whitespace
                uncommented_line = line.lstrip().lstrip(''.join(comment_delimiters)).strip()
                tokens = uncommented_line.split()
                # Split the uncommented line into words and get the first word
                head = tokens[0] if tokens else None
                # tail is the rest of line without first workd
                tail = ' '.join(tokens[1:])
                # Check if the first word is a Docker keyword
                
                if head in docker_keywords:
                    # Add the uncommented line to the dictionary, keyed by the Docker keyword
                    # This allows for multiple comments for the same keyword to be concatenated
                    
                    docker_declarations.setdefault(head, []).append(tail)
    
    # Convert lists of lines back to single string entries for each keyword
    for key in docker_declarations:
        docker_declarations[key] = '\n'.join(docker_declarations[key])
    
    return docker_declarations

# Example usage (you would replace 'example.txt' with your actual file path):
# docker_declarations = parse_docker_comments('example.txt')
# print(docker_declarations)

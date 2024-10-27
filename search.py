import re

# Function to search for SSNs in a given text
def search_for_ssn(text):
    # Regular expression pattern for SSN (XXX-XX-XXXX)
    # ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}'
    
    # Find all occurrences of the SSN pattern
    matches = re.findall(ssn_pattern, text)
    
    return matches

# Main function to read a text file and search for SSNs
def main(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            ssns_found = search_for_ssn(text)
            
            if ssns_found:
                print("SSNs found:")
                for ssn in ssns_found:
                    print(ssn)
            else:
                print("No SSNs found.")
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage

file_path = 'text_file.txt'
main(file_path)

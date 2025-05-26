import re

def extract_yt_term(query):
    #Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #use research to find the match in the command
    match = re.search(pattern, query, re.IGNORECASE)
    #If match found, return extracted song else return none
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    # split the input string into words
    words = input_string.split()

    #remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    #join the remaining words back into string
    results_string = ' '.join(filtered_words)

    return results_string

# #Example usage
# input_string = "make a phone call to atika"
# words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp','']

# result = remove_words(input_string, words_to_remove)
# print(result)
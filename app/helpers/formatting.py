# Helper to decrease the number of duplicated code

# Function to capitalize all words in a string
def capitalize_all_words(text):
    if isinstance(text, str):
        words = text.strip().split()
        return ' '.join([word.capitalize() for word in words])
    else:
        error_message = "The text must be a string"
        raise IOError(error_message)

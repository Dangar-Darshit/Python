def reverse_text(text):
    if text == "":
        return text
    
    return text[-1] + reverse_text(text[:-1])

print(reverse_text("cat"))  # "tac"
print(reverse_text("a"))    # "a"
print(reverse_text(""))     # ""
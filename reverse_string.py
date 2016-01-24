def reverse(text):
    new = []
    for i in range(len(text)-1,-1,-1):
        new.append(text[i])
    return "".join(new)
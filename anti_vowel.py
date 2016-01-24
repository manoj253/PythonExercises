def anti_vowel(text):
        anti = ""
        for char in text:
            if char not in 'aeiouAEIOU':
                anti += char
        return anti
            
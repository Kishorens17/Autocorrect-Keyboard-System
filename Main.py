from spellchecker import SpellChecker

def autocorrect_text(input_text):
    spell = SpellChecker()
    
    words = input_text.split()
    lowercase_words = [word.lower() for word in words]
    misspelled = spell.unknown(lowercase_words)

    corrections = {}
    for word in misspelled:
        suggestions = spell.candidates(word)
        best_guess = spell.correction(word)
        corrections[word] = {
            'suggestions': suggestions,
            'best_guess': best_guess
        }

    corrected_text = []
    for word in words:
        word_lower = word.lower()
        if word_lower in corrections:
            corrected_word = corrections[word_lower]['best_guess']
            corrected_text.append(corrected_word)
        else:
            corrected_text.append(word)

    count = 0
    print("\n--- Corrections ---")
    for word, data in corrections.items():
        print(f"Total corrections available: {len(data['suggestions'])}")
        print(f"Misspelled: {word}")
        print(f"Suggestions: {data['suggestions']}")
        print(f"Autocorrected to: {data['best_guess']}")
        print()
        count += 1

    return ' '.join(corrected_text), count

# Example Usage
if __name__ == "__main__":
    input_text = "hi helo how arg you"
    corrected, total = autocorrect_text(input_text)
    print(f"Total words corrected: {total}")
    print("Corrected Sentence:", corrected)


from spellchecker import SpellChecker

class spellcheckerapp:
    def __init__(self):
        self.spell=SpellChecker()

    def correct_text(self,text):
        words=text.split()
        corrected_words=[]


        for word in words:
            corrected_words=self.spell.correction(word)
            if corrected_words!=words.lower():
                print(f'Correcting "{word}" to "{corrected_words}"')
                corrected_words.append(corrected_words)


        return " ".join(corrected_words)
    
    def run(self):
        print("\n---Spell checker")

        while True:
            text=input("enter text to check (or type exit to quit)")

            if text.lower()=='exit':
                print("Closing the prgram")
                break

            corrected_text=self.correct_text(text)
            print(f"corrected text :{corrected_text}")

if __name__=="__main__":
    spellcheckerapp().run()
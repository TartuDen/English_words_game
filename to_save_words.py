

class WordsToSave():
    def __init__(self, theWord=None) -> None:
        self.wordToSave = theWord
        with open(".\\wordFiles\\difWords.txt","r", encoding='utf-8') as data:
            self.currentFile = data.read()

    def writeUp(self):
        if self.currentFile:
            if self.wordToSave not in self.currentFile.split("\n"):
                with open(".\\wordFiles\\difWords.txt","a", encoding='utf-8') as data:
                    data.write(f"{self.wordToSave}\n")
        
        else:
            with open(".\\wordFiles\\difWords.txt","w",encoding='utf-8') as data:
                data.write(f"{self.wordToSave}\n")


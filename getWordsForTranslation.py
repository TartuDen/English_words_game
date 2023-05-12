import docx


class ReadDocx():
    def __init__(self) -> None:
        pass
        # Open the Word file
        doc = docx.Document('.\\wordFiles\\test.docx')

        # Get the first table in the document
        self.table = doc.tables[0]
        self.read_words()
    def read_words(self):
        final_dic = {}
        # Get the second column of the table
        column2 = self.table.columns[1]
        column3 = self.table.columns[2]
        list_ = ["–","-", "/"]
        # Loop through each cell in the column
        count=0
        for cell_eng,cell_rus in zip(column2.cells,column3.cells):
            # Get the text from the cell
            text_eng = cell_eng.text.strip()
            text_rus = cell_rus.text.strip()
            # Find the index of the "-/" characters in the text
            for i in list_:
                index = text_eng.find(i)
                if index > -1:
                    break
            # If the characters are found, print out the text before them
            if index != -1:
                # print(text_eng[:index].strip(),text_rus)
                final_dic[text_eng[:index].strip()]=text_rus
                count+=1
        print(final_dic.keys())
        return(final_dic)
s=ReadDocx()
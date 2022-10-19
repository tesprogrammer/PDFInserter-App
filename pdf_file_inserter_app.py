#!/usr/bin/python3
# from openpyxl import *
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox
import time
from PyPDF2 import PdfFileReader, PdfFileWriter
root = Tk()

root.geometry('604x360+0+200')
root.title("PDF Inserter")

f1 = ""
f2 = ""


class Compare():
    def __init__(self):
        self.file1 = ""
        self.file2 = ""

    def setFile1(self, file1):
        print("File 1 set")
        self.file1 = file1
        self.change_pic1()
        return self.file1

    def setFile2(self, file2):
        print("File 2 set")
        self.file2 = file2
        return self.file2

    def __str__(self):
        return str(self.file1 + '\t' + self.file2)

    def process(self):
        # Opening up the files
        file1 = self.file1
        file2 = self.file2

        print(file1)
        print(file2)

        pdf_writer = PdfFileWriter()

        mainFile = file1
        insertFile = file2

        try:
            insertFile_pdf_reader = PdfFileReader(insertFile)
            insert = insertFile_pdf_reader.getPage(0)
        except UnicodeDecodeError:
            messagebox.showinfo("", "Incorrect file type.")

        for i in range(1):
            try:
                pdf_reader = PdfFileReader(mainFile)
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(insert)
                    pdf_writer.addPage(pdf_reader.getPage(page))
            except UnicodeDecodeError:
                messagebox.showinfo("", "Incorrect file type.")

        # Write out the merged PDF
        with open('merged.pdf', 'wb') as out:
            pdf_writer.write(out)


        C.finalMessage()  # notifies user process is completed

    def change_pic1(self):
        photo1 = PhotoImage(file=r'images/thumbnail_file_clicked.png')
        compose_button.configure(image=photo1)
        compose_button.photo = photo1
        print("updatedbutton1")

    def change_pic2(self):
        photo1 = PhotoImage(file=r'images/thumbnail_file_clicked.png')
        compose_button2.configure(image=photo1)
        compose_button2.photo = photo1
        print("updatedbutton2")


    def finalMessage(self):
        C.change_pic2()
        root.update()  # refreshes UI to update checked box thumbnail
        time.sleep(2)
        messagebox.showinfo("", "Merged and exported")
        C.reset()

    def reset(self):
        C.resetOne()
        C.resetTwo()

    def resetOne(self):
        photo1 = PhotoImage(file=r'images/thumbnail_file.png')
        compose_button.configure(image=photo1)
        compose_button.photo = photo1
        print("updatedbutton1")
        root.update()

    def resetTwo(self):
        photo2 = PhotoImage(file=r'images/thumbnail_file.png')
        compose_button2.configure(image=photo2)
        compose_button2.photo = photo2
        print("updatedbutton2")
        root.update()

C = Compare()


def OpenFile() -> object:
    file1 = askopenfilename(initialdir="C:/Users/Grant/Documents/Text/",
                            filetypes=(("All Files", "*.*"), ("All Files", "*.*")), title="Select a file (modded).")
    print("here", file1)

    if ".pdf" not in file1 and file1 != "":
        messagebox.showinfo("", "Incorrect file type.")
        C.resetOne()
        return
    elif ".pdf" not in file1 and file1 == "":
        C.resetOne()
        return
    else:
        f1 = C.setFile1(file1)
        print("f1", f1)


frame3 = Frame(root, width=200, height=150, background="white")
frame3.grid(row=0, column=1, rowspan=1, columnspan=50, sticky='w')


def OpenFile2() -> object:
    file2 = askopenfilename(initialdir="C:/Users/Grant/Documents/Text/",
                            filetypes=(("All Files", "*.*"), ("All Files", "*.*")), title="Select a file (modded).")

    if ".pdf" not in file2 and file2 != "":
        messagebox.showinfo("", "Incorrect file type.")
        C.resetTwo()
        return
    elif ".pdf" not in file2 and file2 == "":
        C.resetTwo()
        return
    else:
        f2 = C.setFile2(file2)
        print("f2", f2)

    if f2 is not None:
        C.process()



prof_img = PhotoImage(file=r'images/background.png')
file1image1 = PhotoImage(file=r'images/thumbnail_file.png')
file1image2 = PhotoImage(file=r'images/thumbnail_file.png')

lbl1 = Label(frame3, image=prof_img, compound=TOP)
lbl1.grid(rowspan=10, columnspan=40, column=0, row=0)

compose_button = Button(frame3, text="Select File 1", image=file1image1, command=OpenFile)
compose_button.grid(column=17, row=5)

compose_button2 = Button(frame3, text="Select File 2", image=file1image2, command=OpenFile2)
compose_button2.grid(column=27, row=5)

root.mainloop()

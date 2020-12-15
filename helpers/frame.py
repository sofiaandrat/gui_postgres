import sys, os
import tkinter as tk
from tkinter import ttk
import database as postgres
import guihelper as guihelper

fontstyle = ("Helvetica", 18)

def View(self, parent, controller, table_name=None):

    self.treeview = None

    label_text = "View a Table"
    if table_name:
        label_text = label_text + " " + table_name[14:-1]
    label = tk.Label(self, text=label_text, font=fontstyle)
    label.pack(pady = (15, 75), padx = 100)

    # Text input area and Submission button
    if not table_name:
        textbox = tk.Text(self, height = 1, width = 25)
        label = ttk.Label(self, text="Find Table by Name")
        output = ttk.Label(self, textvariable=self.console)
        label.pack()
        textbox.pack()
        output.pack(pady=(30, 10))

    table = tk.Frame(self)

    
    guihelper.drawTable(table)
    prev = ttk.Button(table, text = "Previous 50",  command = lambda: guihelper.loadPrev(self, table, table_name if
                                                                                        table_name else textbox))
    next = ttk.Button(table, text = "Next 50",  command = lambda: guihelper.loadNext(self, table, table_name if
                                                                                    table_name else textbox))
    table.pack(fill = "none", expand = True)
    if table_name:
        guihelper.loadTable(self, table, table_name)
    else:
        zonebutton = ttk.Button(self, text="View Table by Zone Name", command=lambda: guihelper.loadTable(self, table,
                                                                                                          textbox))
        zonebutton.pack(pady=15)

    prev.pack()
    next.pack()


def Create(self, parent, controller):

    label = tk.Label(self, text="Create A Table", font=fontstyle)
    label.pack(pady = 100, padx = 100)
    bottom = tk.Frame(self)
    bottom.pack(side = 'bottom')

    # Text input area and Submission button
    textbox = tk.Text(self, height = 1, width = 25)
    label = ttk.Label(self, text="Create Table by Name")
    label.pack()
    textbox.pack()
    zonebutton = ttk.Button(self, text = "Create", command = lambda: guihelper.getName(textbox))
    zonebutton.pack(pady=15)

def Upload(self, parent, controller):

    label = tk.Label(self, text="Upload a table from CSV", font=fontstyle)
    label.pack(pady = 100, padx = 100)

    # Text input area and Submission button
    textbox = tk.Text(self, height = 1, width = 25)
    label = ttk.Label(self, text="Upload a CSV file")
    label.pack()
    textbox.pack()
    zonebutton = ttk.Button(self, text = "Upload", command = lambda: guihelper.getName(textbox))
    zonebutton.pack(pady=15)

def Delete(self, parent):

    label = ttk.Label(self, text="Delete A Table", font=fontstyle)
    label.pack(pady = 100, padx = 100)

    # Text input area and Submission button
    textbox = tk.Text(self, height = 1, width = 25)
    label = ttk.Label(self, text="Delete Table by Name")
    label.pack()
    textbox.pack()
    zonebutton = ttk.Button(self, text = "Delete", command = lambda: guihelper.getName(textbox))
    zonebutton.pack(pady=15)

def Connection(self, parent):

    label = tk.Label(self, text="Set Connection Parameters", font=fontstyle)
    label.pack(pady = 50, padx = 100)
     # Text input area and Submission button
    self.host = tk.Text(self, height = 1, width = 25)
    hostLabel = ttk.Label(self, text="Host:")
    self.dbname = tk.Text(self, height = 1, width = 25)
    dbnameLabel = ttk.Label(self, text="Dbname: ")
    self.user = tk.Text(self, height = 1, width = 25)
    userLabel = ttk.Label(self, text="User:")
    self.password = tk.Text(self, height = 1, width = 25)
    passwordLabel = ttk.Label(self, text="Password:")
    self.port = tk.Text(self, height = 1, width = 25)
    portLabel = ttk.Label(self, text="Port (optional):")

    create = ttk.Button(self, text = "Submit", command = lambda: guihelper.setConfig(self))
    output = ttk.Label(self, textvariable=self.connectionstr)

    hostLabel.pack()
    self.host.pack()
    dbnameLabel.pack()
    self.dbname.pack()
    userLabel.pack()
    self.user.pack()
    passwordLabel.pack()
    self.password.pack()
    portLabel.pack()
    self.port.pack()

    create.pack(pady=25)
    output.pack()

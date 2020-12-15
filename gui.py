import sys, os
from sys import path

import tkinter as tk
from tkinter import ttk

path.append(path[0] + '\helpers')

import database as postgres
import guihelper as guihelper
import frame as frame

fontstyle = ("Helvetica", 18)

class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        # Set icons and title
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='./icons/now-black.ico')
        tk.Tk.wm_title(self, 'PostgreSQL Developer')

        # Setup frame layout for application
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frame "Router" for use in the index
        self.frames = {}

        for Frame in (Index, View, ViewDrugTable, ViewExperimentTable, ViewExperimentalSampleTable,
                      ViewTestMaterialTable, ViewTypeOfTestMaterialTable, ViewValidationExperimentTable,
                      ViewValidationExperimentSchemeTable, Connection):

            frame = Frame(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[Frame] = frame

        self.show_frame(Index)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Index(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup frame layout
        self.connectionstr = tk.StringVar()

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PostgreSQL Developer", font=fontstyle)
        label.pack(pady=80, padx=100)
        bottom = tk.Frame(self)
        bottom.pack(side='bottom')

        view_button = ttk.Button(self, text="View", command=lambda: controller.show_frame(View))
        drug_view_button = ttk.Button(self, text="View Drug", command=lambda: controller.show_frame(ViewDrugTable))
        experiments_view_button = ttk.Button(self, text="View Experiments", command=lambda:
                                            controller.show_frame(ViewExperimentTable))
        experimental_sample_view_button = ttk.Button(self, text="View Experimental sample", command=lambda:
                                                    controller.show_frame(ViewExperimentalSampleTable))
        test_material_view_button = ttk.Button(self, text="View Test material", command=lambda:
                                                controller.show_frame(ViewTestMaterialTable))
        type_of_test_material_view_button = ttk.Button(self, text="View Type of test material", command=lambda:
                                                        controller.show_frame(ViewTypeOfTestMaterialTable))
        validation_experiment = ttk.Button(self, text="View Validation experiment", command=lambda:
                                                        controller.show_frame(ViewValidationExperimentTable))
        validation_experiment_scheme = ttk.Button(self, text="View Validation experiment scheme", command=lambda:
                                                        controller.show_frame(ViewValidationExperimentSchemeTable))
        test = ttk.Button(bottom, text="Test Connection", command=lambda: guihelper.connectionTest(self))
        output = ttk.Label(self, textvariable=self.connectionstr)
        editconn = ttk.Button(bottom, text="Edit Connection Details", command=lambda: controller.show_frame(Connection))
        defaultconn = ttk.Button(bottom, text="Use default connection", command=lambda: guihelper.setdefaultconfig(self))

        view_button.pack(pady=5)
        drug_view_button.pack(pady=5)
        experiments_view_button.pack(pady=5)
        experimental_sample_view_button.pack(pady=5)
        test_material_view_button.pack(pady=5)
        type_of_test_material_view_button.pack(pady=5)
        validation_experiment.pack(pady=5)
        validation_experiment_scheme.pack(pady=5)
        output.pack(pady = 50)

        test.pack(pady=(10, 10))
        editconn.pack(pady=(10, 10))
        defaultconn.pack(pady = (10, 100))

class View(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewDrugTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Drug"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewExperimentTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Experiment"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewExperimentalSampleTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Experimental sample"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewTestMaterialTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Test material"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewTypeOfTestMaterialTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Type of test material"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewValidationExperimentTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Validation experiment"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class ViewValidationExperimentSchemeTable(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar()
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller, '"Laboratory"."Validation experiment scheme"')

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class Create(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Create(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)

class Upload(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Upload(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class Delete(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Delete(self, parent)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)
        
class Connection(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        self.connectionstr = tk.StringVar()

        tk.Frame.__init__(self, parent)       
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        frame.Connection(self, parent)

        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)


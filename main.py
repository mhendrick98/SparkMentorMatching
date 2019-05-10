from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import formatInput
from match import Matcher
import os


def mentor_matching_fellows():
    filepath = askopenfilename()
    formatInput.prepareTeams(filepath)

def mentor_matching_mentors():
    filepath = askopenfilename()
    formatInput.prepareMentors(filepath)

def generateOptimalMatches():
    # the men and their list of ordered spousal preferences
    M = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                    for line in open('Teams.txt')))

    # the women and their list of ordered spousal preferences
    W = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                    for line in open('Mentors.txt')))

    # initialize Matcher with preference lists for both men and women
    match = Matcher(M, W)
    wives = match()
    os.remove("Mentors.txt")
    os.remove("Teams.txt")
    file = "Optimal Output.txt"
    with open(file, 'w') as f:
        f.write(str(match.pairs))
        f.close()

def main():
    root = Tk()
    root.title("Mentor Matching Algorithm")

    row = Frame(root)
    Label(row, width=1000, text="Mentor Matching - Students (Responses)", anchor='w').pack(side=LEFT)
    row.pack(side=TOP, fill=X)

    row = Frame(root)
    Label(row, width=1000, text="https://docs.google.com/spreadsheets/d/1QViaS9TlW-5rFkk8wAgwhehgtEIgZcZVEgDX_2qQSY8/edit#gid=2111577187", anchor='w').pack(side=LEFT)
    row.pack(side=TOP, fill=X, padx=5, pady=5)

    row = Frame(root)
    Label(row, width=1000, text="Mentor Matching - Mentor (Responses)", anchor='w').pack(side=LEFT)
    row.pack(side=TOP, fill=X)

    row = Frame(root)
    Label(row, width=1000, text="https://docs.google.com/a/bu.edu/spreadsheets/d/1fgKFACChlMfZYBV7PNitkIa9hyb3mqYlID7xxTrmUfk/edit?usp=forms_web_b#gid=314162645", anchor='w').pack(side=LEFT)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    buttonTTK = ttk.Button(root, text='Import Fellowship Preferences', command=(lambda: mentor_matching_fellows() )).pack(side=LEFT)
    buttonTTK2 = ttk.Button(root, text='Import Mentor Preferences', command=(lambda: mentor_matching_mentors() )).pack(side=LEFT)
    buttonTTK3 = ttk.Button(root, text='Generate Optimal Matches', command=(lambda: generateOptimalMatches() )).pack(side=LEFT)
    # hyper_text = Label(root, text="File Format", fg="blue", cursor="hand2")
    # hyper_text.pack(side=TOP, padx=5, pady=5)
    # hyper_text.bind("<Button-1>", globalfunctions.display_file_format)
    root.mainloop()

main()


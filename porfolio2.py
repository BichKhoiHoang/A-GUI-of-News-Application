# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  ITD104, "Building IT Systems", TP2, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#

student_number = 10578919  # put your student number here as an integer
student_name = "Bich Khoi Hoang"  # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Assignment Description-----------------------------------------#
#
#  Check the Headlines
#
#  In this assignment you will combine your knowledge of HTML/CSS
#  mark-up languages with your skills in Python scripting, pattern
#  matching and Graphical User Interface design to produce
#  a useful application that allows the user to compare news stories
#  from multiple sources and save them for later perusal.
#
#  See the client's requirements accompanying this file for full
#  details.
#
# --------------------------------------------------------------------#


# -----Initialisation Steps-------------------------------------------#
#

# Import standard Python 3 modules needed to complete this assignment.
# [No other modules are needed for your solution.
# Your solution MUST NOT rely on any other modules.]
#
# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function below.)
from urllib.request import urlopen

# Some standard Tkinter functions.  (You WILL need to use
# SOME of these functions in your solution.)  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: DON'T import all of the "tkinter.tkk" functions
# using a "*" wildcard because this module includes alternative
# versions of standard widgets like "Label".)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  (You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  (You WILL need to use this function
# in your solution.)
from webbrowser import open as urldisplay

# Confirm that the student has declared their authorship.
# You must NOT change any of the code below.
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()


#
# --------------------------------------------------------------------#


# -----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  (You are not required to use this function, but it may
# save you some effort.)
#
# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
def download(url='http://www.wikipedia.org/',
             target_filename='downloaded_document',
             filename_extension='html',
             save_file=True,
             char_set='UTF-8'):
    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding=char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# create a window
the_window = Tk()

# give a title for the window
the_window.title('Art and Culture News')

# set the window's size
the_window.geometry('600x800')

# set the background's color
the_window['bg'] = 'darkslategrey'

# insert the photo
wallpaper = PhotoImage(file='wallpaper.gif')
# Add the image to the root window as a Label widget
label_image = Label(the_window, image=wallpaper, width=500, height=200)
label_image.pack(pady=10)

# Add title on GUI
label_title = Label(label_image, text='ART & CULTURE', font=('Arial', 40), fg="black")
label_title.place(bordermode=INSIDE, x=100, y=50)

# Define a function to display news's content when click on each Radiobutton
def source_download():
    if source_group.get() == 1:
        # Call download() function to download and save a web document
        download(url='https://www.abc.net.au/news/arts-culture', target_filename='abcnews_document')
        # Open and read the downloaded document
        file = open('abcnews_document.html')
        file_contents = file.read()
        # Find headines, decriptions, source info from the document and insert in the text field
        headlines = findall('data-component="Link">([\w\s.,;:?!\&#x27;—-]+)</a></span></h3>', file_contents)
        headline_text.delete(0.0, END)
        headline_text.insert(END, headlines[0].replace("&#x27;", "'")) # replace html entity into a readable character
        descriptions = findall('data-component="CardDescription">([\w\s.,;:?!\&#x27;—-]+)', file_contents)
        description_text.delete(0.0, END)
        description_text.insert(END, descriptions[0].replace("&#x27;", "'"))
        dates = (findall('href="/news/([\d-]+)', file_contents))
        source_info = ('Date: ' + dates[0] + '\n'
                       'News source: ABC News \n'
                       'Host name:www.abc.net.au \n'
                       'Url:https://www.abc.net.au/news/arts-culture/')
        source_text.delete(0.0, END)
        source_text.insert(END, source_info)
        # Close the file
        file.close()
    if source_group.get() == 2:
        download(url='https://www.theguardian.com/au/culture', target_filename='theguardian_document')
        file = open('theguardian_document.html')
        file_contents = file.read()
        headlines = findall(
            'data-link-name="article"><span class="fc-item__kicker">'
            '(.+)'
            '</span> <span class="u-faux-block-link__cta fc-item__headline"> <span class="js-headline-text">'
            '(.+)'
            '</span></span> </a></h3>', file_contents)
        print(headlines)
        headline = headlines[0]
        headline_text.delete(0.0, END)
        headline_text.insert(END, headline[0] + ': \n' + headline[1])
        descriptions = findall('<div class="fc-item__standfirst">\n\s+(.+)', file_contents)
        description_text.delete(0.0, END)
        description_text.insert(END, descriptions[0])
        dates = findall('class="fc-item__title"><a href="https://www.theguardian.com/culture/(\d+/[a-z]+/\d+)', file_contents)
        source_info = ('Date: ' + dates[0] + '\n'
                       'News source: The Guardian \n'
                       'Host name: www.theguardian.com \n'
                       'Url: https://www.theguardian.com/au/culture')
        source_text.delete(0.0, END)
        source_text.insert(END, source_info)
        file.close()

# create a frame for radiobutton
select_frame = LabelFrame(the_window, text="Select magazine source",
                          bg='bisque', font=('Arial', 15),relief="sunken")
select_frame.pack(pady=5)
# Create radiobutton conataing options
source_group = IntVar()
Radiobutton(select_frame, text='ABC NEWS',bg='bisque', variable=source_group, value=1, command=source_download).pack()
Radiobutton(select_frame, text='THE GUARDIAN',bg='bisque', variable=source_group, value=2, command=source_download).pack()

#
# create a function to open a live website
def open_url():
    if source_group.get() == 1:
        url = 'https://www.abc.net.au/news/arts-culture/'
    elif source_group.get() == 2:
        url = 'https://www.theguardian.com/au/culture'
    urldisplay(url)
     

# Create a button to check the source
check_source = Button(the_window, text='Check source',bg='cadetblue', relief=GROOVE, command=open_url)
check_source.pack(pady=10)

# Create frame
text_frame = LabelFrame(the_window, text="Art&Culture News", bg='cadetblue', font=('Arial', 20))
text_frame.pack(pady=5)

# Create text fields
text_font = ('Arial', 15)
headline_text = Text(text_frame, height=5, width=60, font=text_font)
headline_text.insert(END, 'This is a headline')
headline_text.pack(padx=5, pady=5)

description_text = Text(text_frame, height=5, width=60, font=text_font)
description_text.insert(END, 'This is a description')
description_text.pack(padx=5, pady=5)

source_text = Text(text_frame, height=10, width=60, font=text_font)
source_text.insert(END, 'This is a source of the news')
source_text.pack(padx=5, pady=5)

# start the event loop
the_window.mainloop()


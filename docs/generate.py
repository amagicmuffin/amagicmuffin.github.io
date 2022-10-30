# TODO wait instead of going through every single file, you could just do smth like os.run("cp *.js").
# figure out how that works

from os import listdir

from typing import List

"""generate.py
when ran, takes all html files in this directory and formats them with stuff and puts that in the upper directory
"""


def doubleIndent(text: str) -> str:
    """formats the input text with four spaces (two indents of two spaces)"""
    return text.replace("\n", "\n    ")


def getFilesRecur(filepath: str):
    """
    YOOOO i think i can make this recursive
    returns a list of strings that are filenames, recursively from filepath
    first call should be "."
    """

    items: List[str] = listdir(filepath)

    ans = []

    for item in items:
        if "." in item:  # then, it is a file
            ans.append(f"{filepath}/{item}")
        else:  # is a file
            ans += getFilesRecur(item)

    return ans


def shouldExport(file: str) -> bool:
    """UNUSED RN: should this file be exported? returns true if file is a html, css, or js file"""
    return file[-5:] == ".html" or file[-4:] == ".css" or file[-3:] == ".js"


def formatText(text: str, file: str) -> str:
    """
    formats a .css, .js, or .html file to be written.
    css and js files are just copied over but html files need the header and footers.
    """
    ABOVE: str = """<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8">
    <title>amuffin's corner</title>
    <meta name="description" content="a personal webbed site">
    <link href="{layers}style.css" rel="stylesheet" type="text/css">
    <link rel="icon" type="image/png" sizes="16x16" href="{layers}assets/heart16x16.png">
  </head>

  <body>
    <div class="left-spacer"></div>

    <div class="navbar">
      <a href="{layers}index.html">home</a>
      <a href="{layers}blog.html">blog</a>
      <a href="{layers}projects.html">projects</a>
      <a href="{layers}stuff.html">stuff</a>
      <a class="settings-btn" href="{layers}settings.html">settings</a>
      <img src="{layers}assets/nighttime.png">
    </div>

    """

    BELOW: str = """

  </body>
</html>"""

    if len(file) >= 5:
        if file[-5:] == ".html":
            # an absolute mess I am so sorry
            # this figures out how deep in the folder structure file is
            # and adjusts how many layers of "../" to put into the template html
            # for example, "../index.html" instead of "index.html" if needed

            longFile = file  # such as "./blog.html" or "blog-posts/keepingMemories.html"
            shortFile = longFile.replace("./", "")  # such as "blog.html" or "blog-posts/keepingMemories.html"
            levelsDeep = shortFile.count("/")
            replaceLayers: str = "../" * levelsDeep
            return ABOVE.format(layers=replaceLayers) + doubleIndent(text) + BELOW.format(layers=replaceLayers)

    return text

        
def genFiles():
    """generate files"""
    filesToExport = getFilesRecur(".")

    print(f"detected files: {filesToExport}\n")

    # generate files in parent (/doc) directory
    for file in filesToExport:
        print(f"Working on output file ../{file}")

        text: str = ""

        # save the text from inputFile into string variable text
        with open(file, "r") as inputFile:
            text = inputFile.read()
            if "<p>written 29 O" in text:
                print("YESYESYESYESLKSDJFLKFDJSSLDKFJLSDKFJ")
                print(text) # TODO rm this
            else:
                print("NONONONOLKSADJFLKSAJDFLKSJFLSKDJFLSKDFJSLKDJF")
            print(f"  Input text ./{file} read")

        # write into output file
        with open(f"../{file}", "w") as outputFile:
            outputFile.write(formatText(text, file))

            print(f"  Text in output file ../{file} replaced")

        print("  Done")

    print("Done")


def main():
    genFiles()


if __name__ == "__main__":
    main()

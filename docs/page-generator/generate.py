from os import listdir

"""generate.py
when ran, takes all html files in this directory and formats them with stuff and puts that in the upper directory
"""

ABOVE: str = """<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8">
    <title>amuffin's corner</title>
    <meta name="description" content="a personal webbed site">
    <link href="style.css" rel="stylesheet" type="text/css">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/heart16x16.png">
  </head>

  <body>
    <div class="left-spacer"></div>

    <div class="navbar">
      <a href="index.html">home</a>
      <a href="temp.html">interests</a>
      <a href="blog.html">blog</a>
      <a href="projects.html">projects</a>
      <a href="stuff.html">stuff</a>
      <a class="settings-btn" href="settings.html">settings</a>
      <img src="assets/nighttime.png">
    </div>

    """

BELOW: str = """

  </body>
</html>"""


def doubleIndent(text: str) -> str:
    """formats the input text with four spaces (two indents of two spaces)"""
    return text.replace("\n", "\n    ")


def shouldExport(file: str) -> bool:
    """should this file be exported?"""
    return file[-5:] == ".html" or file[-4:] == ".css" or file[-3:] == ".js"


def formatText(text: str, file: str) -> str:
    """
    formats a .css, .js, or .html file to be written.
    css and js files are just copied over but html files need the header and footers.
    """
    if len(file) >= 5:
        if file[-5:] == ".html":
            return ABOVE + doubleIndent(text) + BELOW

    return text

        
def genFiles():
    """generate files"""
    # get html files to generate
    filesInDirectory: list[str] = listdir()
    filesToExport: list[str] = [file for file in filesInDirectory if (shouldExport(file))]

    print(f"detected files: {filesToExport}\n")

    # generate files in parent (/doc) directory
    for file in filesToExport:
        print(f"Working on output file ../{file}")

        text: str = ""

        # save the text from inputFile into string variable text
        with open(file, "r") as inputFile:
            text = inputFile.read()
            print(f"  Input text ./{file} read")

        # write into output file
        with open(f"../{file}", "w") as outputFile:
            outputFile.write(formatText(text, file))

            print("  Text in output file replaced")

        print("  Done")

    print("Done")


def main():
    genFiles()


if __name__ == "__main__":
    main()

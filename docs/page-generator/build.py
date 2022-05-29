from os import system

"""build.py
to be run every time something changes to compile the code
"""

def main():
    """
    things to do:
    compile scss to css
    generate all files
    """
    system("sass style.scss style.css")
    system("python generate.py")

if __name__ == '__main__':
    main()
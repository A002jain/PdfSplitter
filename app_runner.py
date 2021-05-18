import argparse
from pdf.pdf_services import split, merge

VERSION = "1.1.0"
parser = argparse.ArgumentParser(description="PDF Services :)")


parser.add_argument("-i", "--input_pdf", help="Input PDF file or files", nargs="+", metavar="")
parser.add_argument("-v", "--version", help="App version", action="store_true")
parser.add_argument("-m", "--merge", help="merge PDFs", action="store_true")
parser.add_argument("-s", "--split", help="split PDFs", action="store_true")


def get_input_files():
    files = []
    while True:
        file = input("(press n for exit)Enter file path: ")
        if file == "n":
            break
        files.append(file)
    return files


if __name__ == '__main__':
    args = parser.parse_args()
    if args.version:
        print(f"App Version {VERSION}")
    else:
        input_file = args.input_pdf if args.input_pdf is not None else get_input_files()
        if args.split:
            split(input_pdf=input_file)
        elif args.merge:
            merge(pdf_file_lists=input_file)
        else:
            print("either user -s(Split) or -m(Merge) service")

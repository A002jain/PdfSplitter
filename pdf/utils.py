import os
import random


def get_out_pdf_name():
    out_path = f"outpdf{random.randint(0,20)}.pdf"
    if os.path.exists(out_path):
        out_path = get_out_pdf_name()
    return out_path

#!/usr/bin/env python3
"""Junior IT Officer, LinkedIn Easy Apply under Cleave global e services (Nairobi, contract, oil and gas client).
Same advert as the Stratostaff pack, so the CV and cover letter text come from there.
Run: python3 "applications/Cleave Global Junior IT Officer/build.py"
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
SOURCE = os.path.abspath(os.path.join(HERE, "..", "Stratostaff Junior IT Officer", "build.py"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

spec = importlib.util.spec_from_file_location("stratostaff_pack", SOURCE)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)


if __name__ == "__main__":
    files = br.pack_files(HERE)
    original = br.CONTACT
    br.CONTACT = src.CONTACT
    br.build(src.cv, files["cv_docx"])
    br.build_cover(src.COVER_BODY, src.COVER_TITLE, files["cover_docx"], src.CONTACT)
    br.build_application(src.cv, src.COVER_BODY, src.COVER_TITLE, files["combined_docx"], src.CONTACT)
    pb.build_cv_pdf(src.cv, files["cv_pdf"], src.CONTACT)
    pb.build_cover_pdf(src.COVER_BODY, files["cover_pdf"], src.CONTACT, src.COVER_TITLE)
    pb.build_application_pdf(src.cv, src.COVER_BODY, files["combined_pdf"], src.CONTACT, src.COVER_TITLE)
    br.CONTACT = original
    print("Generated:", HERE)

#!/usr/bin/env python3
"""Site MEL Assistant (REF: SMEL/001/2026), Abt Global Central Mechanism (PMI Evolve Kenya),
IRS in Siaya and Busia counties. 78 posts (Busia 38, Siaya 40). Open to either county.
IRS = one campaign, IT Assistant, Homa Bay County, 2023, ODK/Kobo. No employer name.
Do not write "1 year of IRS". Do not claim DHIS2, GPS, sticker tracking or spray-tracker
ownership on the IRS campaign. Dholuo only (no Luhya, no Ateso).
The portal takes one document: submit "Meshack Ariri Cover Letter and CV".
Run: python3 "applications/Abt Global MEL Assistant/build.py"
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESUMES = os.path.abspath(os.path.join(HERE, "..", "..", "resumes"))
sys.path.insert(0, RESUMES)
import build_resumes as br
import pdf_builder as pb

CONTACT = br.CONTACT
COVER_TITLE = "Site MEL Assistant  |  IRS Siaya and Busia (REF: SMEL/001/2026)"

cv = {
"headline": "Site MEL Assistant  |  IRS Data Quality  ·  ODK / Kobo  ·  DHIS2  ·  Field Team Mentoring",
"metrics": [
    ("IRS", "2023 campaign"),
    ("80+", "staff trained on tools"),
    ("DHIS2", "hands-on + academy"),
    ("Dholuo", "Swahili · English"),
],
"summary": ("MEL and health data professional with 3+ years at PATH supporting field data collection, data "
    "quality and reporting for health programmes. I train field teams on data tools, keep devices and "
    "submissions working, verify data against source, and turn it into weekly Excel and Power BI reports. "
    "Worked the 2023 IRS campaign in Homa Bay County as IT Assistant on ODK/Kobo Collect. DHIS2 Academy "
    "certificate. BSc Applied Computing. Based in Kisumu, ready to live in any assigned sub-county in Siaya "
    "or Busia and work six days a week."),
"skills": [
    ("MEL and data quality", "Point-of-collection checks for accuracy and completeness, DQA, source verification, error follow-up with field teams, indicator reporting"),
    ("Mobile data platforms", "ODK / Kobo Collect, DHIS2, KenyaEMR/TaifaCare; form setup, submissions, sync troubleshooting, field device and connectivity support"),
    ("Training and mentoring", "80+ health workers and staff trained on data tools and data quality; job aids; on-site coaching of field teams"),
    ("Analysis and reporting", "Excel (formulas, pivots, Power Query, VBA), Power BI dashboards, trackers, weekly progress and summary reports, Word, SQL"),
    ("Field readiness", "Six-day campaign weeks, local transport, English, Swahili and Dholuo with community and field teams"),
],
"experience": [
    {"org": "PATH", "title": "Health Informatics / HMIS Officer", "dates": "Mar 2025 to Present",
     "loc": "Kisumu/Nyamira, Kenya", "bullets": [
        "Run data collection, cleaning and analysis for care and treatment, PMTCT and E-TEC indicators, and produce the Excel and Power BI reports programme teams review.",
        "Built SQL validation and data-quality checks that catch incomplete and inconsistent entries early; errors go back to source with a clear list, and reporting time fell about 40%.",
        "Support DHIS2 and KenyaEMR/TaifaCare across facilities, sustaining >98% uptime so field and facility data keep flowing.",
        "Train facility staff and programme teams on DHIS2, data tools and data quality; write SOPs and job aids that teams use after training.",
    ]},
    {"org": "PATH", "title": "ICT Associate", "dates": "Jan 2024 to Mar 2025",
     "loc": "Kisumu, Kenya", "bullets": [
        "Supported OVC and DREAMS field teams as the ICT person: devices, connectivity, data tools and reporting so mentors and case workers could submit on time.",
        "Resolved device, application and access problems for 120+ users under ITIL/SLA ticketing; trained and onboarded new users.",
        "Wrote SQL scripts and automated validation that improved surveillance data accuracy.",
    ]},
    {"org": "PATH", "title": "ECD Programme MIS and ICT", "dates": "2024 to 2025",
     "loc": "Kenya  |  programme closed 2025", "bullets": [
        "Ran digital and manual MIS: collection tools, Excel and Kobo trackers, cleaning and Power BI packs, with field staff onboarded and coached on late entry.",
    ]},
    {"org": "PATH", "title": "ICT Intern", "dates": "Apr 2023 to Dec 2023",
     "loc": "Homa Bay, Kenya", "bullets": [
        "Assisted facility data-system deployment and digitalisation for surveillance and reporting readiness.",
    ]},
    {"org": "Indoor Residual Spraying (IRS) Campaign", "title": "IT Assistant", "dates": "2023  |  one campaign",
     "loc": "Homa Bay County, Kenya", "bullets": [
        "Supported IRS field teams on ODK / Kobo Collect: forms on the phones, daily submissions, and sync problems fixed so spray data reached the server.",
        "Worked alongside spray operators and team leaders and learned the campaign data chain from household to site to programme.",
    ]},
],
"certs": ("DHIS2 Academy certificate  |  Microsoft Data Analysis  |  Google IT Support  |  "
          "IBM Technical Support  |  CCNA  |  Microsoft Azure Fundamentals (AZ-900)"),
"compact_education": True,
"languages": "English (fluent)  ·  Swahili (fluent)  ·  Dholuo (fluent)",
"referees": [
    "Patrick Ondieki, ICT Officer, PATH  |  pondieki@path.org",
    "Marvin Ngosa, Systems Administrator, PATH  |  mngosa@path.org",
    "Gadaffi Ochieng, Procurement Officer, Ampath  |  ochienggadaffi@gmail.com",
],
}

COVER_BODY = [
    "Dear Hiring Manager,",
    "",
    "Re: Site MEL Assistant (REF: SMEL/001/2026), IRS Siaya and Busia Counties",
    "",
    "I am applying for a Site MEL Assistant position (REF: SMEL/001/2026) on the Siaya and Busia IRS campaign. I have worked an IRS "
    "campaign before, as IT Assistant on the 2023 campaign in Homa Bay County, supporting spray teams on ODK and "
    "Kobo Collect. I speak Dholuo, Swahili and English, I am based in Kisumu, and I am ready to live in whichever "
    "sub-county you assign me in Siaya or Busia.",
    "",
    "For more than three years at PATH I have done MEL and data work close to where data is collected. I "
    "supported OVC and DREAMS field teams as their ICT person, keeping devices, connectivity and data tools "
    "working so mentors and case workers could submit on time. I have trained more than 80 health workers and "
    "staff on data tools and data quality, and I write short job aids so the training holds after I leave. As "
    "Health Informatics / HMIS Officer I support DHIS2 and KenyaEMR, run data-quality checks that cut our "
    "reporting time by about 40%, and build the Excel and Power BI reports programme teams read every week.",
    "",
    "That is the work at a spray site. Before the spray I can help train spray operators and team leaders on "
    "the tools and indicators, get phones ready and synced, and check that teams are assigned to the right "
    "areas. During the spray I will check data at the point of collection for accuracy and completeness, fix "
    "sync problems on the spot, keep the spray performance tracker current with the site coordinator, report "
    "sticker shortages early, and send weekly progress reports. After the spray I will make sure every device "
    "is synced and cleared before it goes back to the store, and help clean what remains.",
    "",
    "I hold a BSc in Applied Computing from KCA University and a DHIS2 Academy certificate. I can work six days "
    "a week, Monday to Saturday, travel to field sites on local transport, and commit to the full campaign.",
    "",
    "Thank you for considering my application.",
    "",
    "Sincerely,",
    "Meshack Ariri",
]


if __name__ == "__main__":
    files = br.pack_files(HERE)
    br.build(cv, files["cv_docx"])
    br.build_cover(COVER_BODY, COVER_TITLE, files["cover_docx"], CONTACT)
    br.build_application(cv, COVER_BODY, COVER_TITLE, files["combined_docx"], CONTACT)
    pb.build_cv_pdf(cv, files["cv_pdf"], CONTACT)
    pb.build_cover_pdf(COVER_BODY, files["cover_pdf"], CONTACT, COVER_TITLE)
    pb.build_application_pdf(cv, COVER_BODY, files["combined_pdf"], CONTACT, COVER_TITLE)
    print("Generated:", HERE)

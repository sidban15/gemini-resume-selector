import os
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document

# Define output directory
output_dir = "Unread"
os.makedirs(output_dir, exist_ok=True)

# Helper function to create a PDF resume
def create_pdf(filename, content):
    c = canvas.Canvas(os.path.join(output_dir, filename), pagesize=letter)
    width, height = letter
    text = c.beginText(40, height - 40)
    text.setFont("Helvetica", 12)
    
    for line in content.splitlines():
        text.textLine(line)
        
    c.drawText(text)
    c.save()

# Helper function to create a DOCX resume
def create_docx(filename, content):
    doc = Document()
    for line in content.splitlines():
        if line.strip():
            doc.add_paragraph(line)
    doc.save(os.path.join(output_dir, filename))

# Helper function to create a corrupted file
def create_corrupted(filename):
    with open(os.path.join(output_dir, filename), "wb") as f:
        f.write(os.urandom(1024)) # Write random bytes

# Resume Content Generators
def generate_strong_match(name):
    return f"""
{name}
123 Construction Lane, City, State
(555) 123-4567 | {name.lower().replace(' ', '')}@email.com

OBJECTIVE
Experienced Paralegal with 5+ years in construction law seeking to leverage expertise in mechanics liens, contract administration, and litigation support at a mid-sized construction firm.

EXPERIENCE
Construction Paralegal | Big Build Corp | 2019 - Present
- Managed over 50 active mechanics lien filings per year, ensuring 100% compliance with state deadlines.
- Drafted and reviewed AIA contracts, subcontracts, and change orders.
- Assisted general counsel in litigation preparation, including discovery and exhibit organization.
- Maintained corporate records and license renewals for 5 entities.

Legal Assistant | Smith & Jones Construction Law | 2016 - 2019
- Supported 3 attorneys specializing in construction defect litigation.
- Prepared pleadings, motions, and discovery requests.
- Communicated with clients, courts, and opposing counsel.

EDUCATION
- Paralegal Certificate, ABA Approved Program
- B.A. Legal Studies, State University

SKILLS
- Mechanics Liens & Bond Claims
- Contract Review (AIA, ConsensusDocs)
- Litigation Support
- Notary Public
"""

def generate_medium_match(name):
    return f"""
{name}
456 General St, City, State
(555) 987-6543 | {name.lower().replace(' ', '')}@email.com

OBJECTIVE
Detail-oriented Paralegal with a background in family law and estate planning seeking a new challenge in a corporate environment.

EXPERIENCE
Paralegal | Family Law Associates | 2018 - Present
- Managed caseload of 30+ active divorce and custody files.
- Drafted petitions, decrees, and settlement agreements.
- Conducted legal research and prepared memos for attorneys.
- Organized client files and maintained the firm's calendar.

Legal Secretary | Corporate Legal Services | 2015 - 2018
- Provided administrative support to the corporate governance team.
- Scheduled meetings, managed travel, and processed expense reports.
- Proofread legal documents and correspondence.

EDUCATION
- Associate Degree in Paralegal Studies
- Certified Paralegal (CP)

SKILLS
- Legal Research (Westlaw, LexisNexis)
- Document Drafting
- Microsoft Office Suite
- Case Management Software
"""

def generate_weak_match(name):
    return f"""
{name}
789 Random Rd, City, State
(555) 555-5555 | {name.lower().replace(' ', '')}@email.com

OBJECTIVE
Motivated individual looking for an entry-level position to utilize my organizational and customer service skills.

EXPERIENCE
Barista | Coffee Bean Shop | 2020 - Present
- Provide excellent customer service in a high-volume environment.
- Manage cash register and daily deposits.
- Train new employees on store procedures.

Retail Associate | Clothing Store | 2018 - 2020
- Assisted customers with product selection and fitting.
- Maintained store cleanliness and visual merchandising standards.
- Processed shipments and managed inventory.

EDUCATION
- High School Diploma
- Some College Coursework in General Studies

SKILLS
- Customer Service
- Cash Handling
- Teamwork
- Time Management
"""

# Names list
names = [
    "James Smith", "Maria Garcia", "Robert Johnson", "Lisa Brown", "Michael Davis",
    "Jennifer Wilson", "William Miller", "Elizabeth Taylor", "David Anderson", "Barbara Thomas",
    "Richard Jackson", "Susan White", "Joseph Harris", "Jessica Martin", "Thomas Thompson",
    "Sarah Martinez", "Charles Robinson", "Karen Clark", "Christopher Lewis", "Nancy Lee",
    "Daniel Walker", "Margaret Hall", "Matthew Allen", "Betty Young", "Anthony King",
    "Dorothy Wright", "Donald Scott", "Sandra Torres", "Mark Nguyen", "Ashley Hill",
    "Paul Green", "Kimberly Adams", "Steven Baker", "Emily Nelson", "Andrew Carter"
]

# Generate Files
# Strategy: 10 Strong, 15 Medium, 10 Weak = 35 valid. 5 Corrupted.

print("Generating Strong Matches...")
for i in range(10):
    name = names[i]
    content = generate_strong_match(name)
    filename = f"Resume_{name.replace(' ', '_')}.{'pdf' if i % 2 == 0 else 'docx'}"
    if filename.endswith('.pdf'):
        create_pdf(filename, content)
    else:
        create_docx(filename, content)

print("Generating Medium Matches...")
for i in range(10, 25):
    name = names[i]
    content = generate_medium_match(name)
    filename = f"Resume_{name.replace(' ', '_')}.{'pdf' if i % 2 == 0 else 'docx'}"
    if filename.endswith('.pdf'):
        create_pdf(filename, content)
    else:
        create_docx(filename, content)

print("Generating Weak Matches...")
for i in range(25, 35):
    name = names[i]
    content = generate_weak_match(name)
    filename = f"Resume_{name.replace(' ', '_')}.{'pdf' if i % 2 == 0 else 'docx'}"
    if filename.endswith('.pdf'):
        create_pdf(filename, content)
    else:
        create_docx(filename, content)

print("Generating Corrupted Files...")
corrupted_names = ["Corrupted_File_1", "Broken_Doc_2", "Error_File_3", "Invalid_Format_4", "Bad_Data_5"]
for i, name in enumerate(corrupted_names):
    filename = f"{name}.{'pdf' if i % 2 == 0 else 'docx'}"
    create_corrupted(filename)

print("Done.")

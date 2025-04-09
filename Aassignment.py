import os
import pandas as pd
from fpdf import FPDF
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tabulate import tabulate

# Create the 'payslips' folder if it doesn't exist
if not os.path.exists("payslips"):
    os.makedirs("payslips")
    print("Folder 'payslips' created successfully!")
else:
    print("Folder 'payslips' already exists.")

# Open the Excel file
data = pd.read_excel("employees.xlsx")

# Add a new column for net salary
data["Net Salary"] = data["Basic Salary"] + data["Allowances"] - data["Deductions"]

# Function to display employee details in the terminal
def display_employee_details(employee):
    print("=" * 50)  # Clear divider before each record
    print(f"Payslip created for {employee['Name']} at payslips/{employee['Employee ID']}.pdf")
    print(f"Employee ID: {employee['Employee ID']}")
    print(f"Name: {employee['Name']}")
    print(f"Email: {employee['Email']}")
    print(f"Basic Salary: ${employee['Basic Salary']:,.2f}")
    print(f"Allowances: ${employee['Allowances']:,.2f}")
    print(f"Deductions: ${employee['Deductions']:,.2f}")
    print(f"Net Salary: ${employee['Net Salary']:,.2f}")
    print("=" * 50)  # Clear divider after employee details

# Define the function to create a **modern, readable payslip**
def create_payslip(employee):
    # Format numeric values with a dollar sign
    formatted_basic_salary = f"${employee['Basic Salary']:,.2f}"
    formatted_allowances = f"${employee['Allowances']:,.2f}"
    formatted_deductions = f"${employee['Deductions']:,.2f}"
    formatted_net_salary = f"${employee['Net Salary']:,.2f}"

    # Start a new PDF with a **modern design**
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)  # Larger, bolded title font
    
    # Title section
    pdf.cell(200, 15, txt=f"PAYSLIP - {employee['Name']}", ln=True, align="C", border=0)
    pdf.ln(5)  # Add space

    # Employee details section
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, txt="Employee Information", ln=True, align="C", fill=True)
    pdf.cell(100, 10, txt=f"Employee ID:", border=1)
    pdf.cell(100, 10, txt=f"{employee['Employee ID']}", border=1, ln=True)
    pdf.cell(100, 10, txt=f"Email:", border=1)
    pdf.cell(100, 10, txt=f"{employee['Email']}", border=1, ln=True)
    pdf.ln(5)  # Add space
    
    # Salary breakdown
    pdf.set_fill_color(230, 230, 230)  # Light gray background for clarity
    pdf.cell(200, 10, txt="Salary Breakdown", ln=True, align="C", fill=True)
    pdf.cell(100, 10, txt="Basic Salary:", border=1)
    pdf.cell(100, 10, txt=f"{formatted_basic_salary}", border=1, ln=True, align="R")
    pdf.cell(100, 10, txt="Allowances:", border=1)
    pdf.cell(100, 10, txt=f"{formatted_allowances}", border=1, ln=True, align="R")
    pdf.cell(100, 10, txt="Deductions:", border=1)
    pdf.cell(100, 10, txt=f"{formatted_deductions}", border=1, ln=True, align="R")
    
    # Net Salary - Highlighting final amount
    pdf.set_fill_color(200, 250, 200)  # Light green for the final value
    pdf.cell(100, 10, txt="Net Salary:", border=1, fill=True)
    pdf.cell(100, 10, txt=f"{formatted_net_salary}", border=1, ln=True, align="R", fill=True)

    # Signature line
    pdf.cell(200, 20, txt="", ln=True)  # Add spacing
    pdf.cell(200, 10, txt="Authorized Signature: ____________________", ln=True, align="L")

    # Save the PDF in the 'payslips' folder
    file_name = f"payslips/{employee['Employee ID']}.pdf"
    pdf.output(file_name)

# Create the table data with formatting
table_data = []
for _, employee in data.iterrows():
    table_data.append([
        employee["Employee ID"],
        employee["Name"],
        employee["Email"],
        f"${employee['Basic Salary']:,.2f}",
        f"${employee['Allowances']:,.2f}",
        f"${employee['Deductions']:,.2f}",
        f"${employee['Net Salary']:,.2f}"
    ])

# Specify headers
headers = ["Employee ID", "Name", "Email", "Basic Salary", "Allowances", "Deductions", "Net Salary"]

# Print the formatted table using tabulate
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Define the function to send an email with the payslip attached
def send_email(employee, pdf_file):
    # Email details
    sender_email = "matthewsabeta0@gmail.com"
    sender_password = "dqvcregoxfycdpdg"

    # Access the correct column
    receiver_email = employee["Email"]

    # Email content
    subject = "Your Payslip for This Month"
    body = "Please find your payslip attached."

    # Set up email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach the PDF
    with open(pdf_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={pdf_file}")
        msg.attach(part)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Ensure correct SMTP details
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Send payslips and emails with properly aligned output
for _, employee in data.iterrows():
    pdf_file = f"payslips/{employee['Employee ID']}.pdf"
    
    # Create payslip and display employee details
    create_payslip(employee)
    display_employee_details(employee)
    
    # Send email immediately after details
    send_email(employee, pdf_file)
    
    print(f"Email sent successfully to {employee['Email']}")  # Now correctly placed inside block
    print("=" * 50)  # Divider for clarity between records
import streamlit as st
import pandas as pd
from io import BytesIO

# Same data as pehle
INSTITUTES = [
    {
        "name": "AIIMS Patna",
        "location": "Patna",
        "website": "https://www.aiimspatna.edu.in",
        "domains": ["Oncology", "Public Health"]
    },
    {
        "name": "IGIMS Patna",
        "location": "Patna",
        "website": "https://www.igims.org",
        "domains": ["Genomics", "Molecular Biology"]
    }
]

PERSONS = {
    "AIIMS Patna": [
        {
            "name": "Dr. Anjali Singh",
            "designation": "Professor",
            "email": "anjali.singh@aiimspatna.edu.in",
            "contact": "+91-9876543210",
            "linkedin": "https://linkedin.com/in/anjalisingh",
            "expertise": "Oncology",
            "department": "Oncology Department",
            "lab": "Oncology Research Lab"
        },
        {
            "name": "Dr. Ravi Kumar",
            "designation": "Research Scientist",
            "email": "ravi.kumar@aiimspatna.edu.in",
            "contact": "+91-9876543211",
            "linkedin": "https://linkedin.com/in/ravikumar",
            "expertise": "Public Health",
            "department": "Public Health Department",
            "lab": "Public Health Research Lab"
        }
    ],
    "IGIMS Patna": [
        {
            "name": "Dr. Sneha Sharma",
            "designation": "Assistant Professor",
            "email": "sneha.sharma@igims.org",
            "contact": "+91-9876543220",
            "linkedin": "https://linkedin.com/in/snehasharma",
            "expertise": "Genomics",
            "department": "Genomics Department",
            "lab": "Genomics Research Lab"
        },
        {
            "name": "Dr. Amit Verma",
            "designation": "Principal Investigator",
            "email": "amit.verma@igims.org",
            "contact": "+91-9876543221",
            "linkedin": "https://linkedin.com/in/amitverma",
            "expertise": "Molecular Biology",
            "department": "Molecular Biology Department",
            "lab": "Molecular Biology Research Lab"
        }
    ]
}

SERVICES_SOLUTIONS = [
    "Genomics Analysis", "Proteomics Services", "Metabolomics Profiling", 
    "Clinical Data Management", "Patient Diagnostics", "Bioinformatics Support"
]

FUNDING_AGENCIES = [
    "ICMR", "DBT", "DST", "CSIR", "BIRAC"
]

def create_rows():
    rows = []
    for inst in INSTITUTES:
        for person in PERSONS[inst["name"]]:
            row = {
                "Institute Name": inst["name"],
                "Location": inst["location"],
                "Institute Website": inst["website"],
                "Department Name": person["department"],
                "Lab/Unit Name": person["lab"],
                "Person Name": person["name"],
                "Designation": person["designation"],
                "Email": person["email"],
                "Contact": person["contact"],
                "LinkedIn": person["linkedin"],
                "Primary Focus Area": person["expertise"],
                "Ongoing Projects": "Exploring advanced omics integration in patient diagnostics.",
                "Funding Agencies": ", ".join(FUNDING_AGENCIES),
                "Recent Publications": "https://pubmed.ncbi.nlm.nih.gov/PMID12345678/",
                "Services": ", ".join(SERVICES_SOLUTIONS),
                "Matched Advait Solution(s)": ", ".join(SERVICES_SOLUTIONS),
                "Match Category": "High Relevance"
            }
            rows.append(row)
    return rows

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name="Sheet2")
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def main():
    st.title("AdvaitInsight - Patna Institutes Data Export")

    rows = create_rows()
    df = pd.DataFrame(rows)

    st.dataframe(df)

    excel_data = to_excel(df)

    st.download_button(
        label="Download Excel file",
        data=excel_data,
        file_name="Patna_Institutes_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == "__main__":
    main()

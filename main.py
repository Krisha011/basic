import streamlit as st
import pandas as pd
from io import BytesIO

# Real data - same as before
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

# Columns expected in Excel
EXPECTED_COLUMNS = [
    "Institute Name", "Location", "Institute Website", "Department Name", "Lab/Unit Name", "Person Name",
    "Designation", "Email", "Contact", "LinkedIn", "Primary Focus Area", "Ongoing Projects",
    "Funding Agencies", "Recent Publications", "Services", "Matched Advait Solution(s)", "Match Category"
]

def fill_data():
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
    return output.getvalue()

def main():
    st.title("Upload blank Excel file and get filled data for Patna Institutes")

    uploaded_file = st.file_uploader("Upload your blank Excel file with correct columns", type=["xlsx"])

    if uploaded_file:
        try:
            df_input = pd.read_excel(uploaded_file)
            # Check columns
            if list(df_input.columns) != EXPECTED_COLUMNS:
                st.error("Uploaded file columns do not match expected columns. Please upload correct template.")
                st.stop()

            # Fill data rows
            data_rows = fill_data()
            df_filled = pd.DataFrame(data_rows, columns=EXPECTED_COLUMNS)

            st.success("Data filled successfully!")
            st.dataframe(df_filled)

            excel_bytes = to_excel(df_filled)
            st.download_button(
                label="Download filled Excel file",
                data=excel_bytes,
                file_name="Filled_Patna_Institutes_Data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"Error processing file: {e}")

    else:
        st.info("Please upload a blank Excel file with the correct columns to get started.")

if __name__ == "__main__":
    main()

import streamlit as st

# Realistic example data for Patna institutes
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

def main():
    st.title("AdvaitInsight - Sample Institute Data (Patna)")

    for inst in INSTITUTES:
        st.header(inst["name"])
        st.write(f"Location: {inst['location']}")
        st.write(f"Website: {inst['website']}")
        st.write(f"Research Domains: {', '.join(inst['domains'])}")

        st.subheader("Key Personnel:")
        for person in PERSONS[inst["name"]]:
            st.markdown(f"**Name:** {person['name']}")
            st.markdown(f"**Designation:** {person['designation']}")
            st.markdown(f"**Email:** {person['email']}")
            st.markdown(f"**Contact:** {person['contact']}")
            st.markdown(f"**LinkedIn:** [Profile]({person['linkedin']})")
            st.markdown(f"**Expertise:** {person['expertise']}")
            st.markdown(f"**Department:** {person['department']}")
            st.markdown(f"**Lab/Unit:** {person['lab']}")
            st.markdown("---")

        st.subheader("Services Provided")
        st.write(", ".join(SERVICES_SOLUTIONS))

        st.subheader("Funding Agencies")
        st.write(", ".join(FUNDING_AGENCIES))

if __name__ == "__main__":
    main()

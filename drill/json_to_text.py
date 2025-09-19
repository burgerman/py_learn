import json

base_infer = {
    "work_experience": [
        {
            "role": "Information Technology Specialist",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "07/2004",
            "to_date": "Current",
            "description": [
                "Managed the assigned IT/communications environment with privileged access at the network level for the Wing, Geographically Separated Units (GSU), and Tenants.",
                "Planned, coordinated, installed, and continuously analyzed system design, hardware and software.",
                "Developed, recommended, and installed solutions and upgrades to ensure availability, integrity, efficiency, and reliability of all components of the assigned system."
            ]
        },
        {
            "role": "Cyber Transport/ Client Systems Workcenter Supervisor",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "02/2001",
            "to_date": "Current",
            "description": [
                "Managed Cyber Transport/Client Systems work center personnel.",
                "Set and adjusted work priorities, evaluated, and counseled subordinates.",
                "Documented training of personnel using Computer based training system (TBA).",
                "Sustained and operated systems through effective troubleshooting, repair, PMI's, system performance testing/analysis. Systems included network infrastructure equipment, cabling, voice systems, video systems, small computers, and printers.",
                "Maintained close working relationship with Communications Focal Point--production requirements/Remedy tickets."
            ]
        },
        {
            "role": "F-16 Ejection System Technician",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "07/1996",
            "to_date": "07/2000",
            "description": [
                "Troubleshot, removed, tested, inspected, repaired, modified, and installed explosive and non-explosive components and assemblies on ejection systems.",
                "Performed preventative maintenance on over ninety different electronically fired explosive devices ensuring proper wiring and termination.",
                "Foreign object damage monitor, briefed wing commander monthly on findings.",
                "Ran entire supply system ensuring all parts and supplies were readily available.",
                "Hazardous materials monitor. Explosive inspector. Ensured proper grounding points were present in shop to prevent electrostatic discharge to explosive components."
            ]
        }
    ]
}

predict_infer = {
    "work_experience": [
        {
            "role": "Information Technology Specialist",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "07/2004",
            "to_date": "Current",
            "description": [
                "Managed the assigned IT/communications environment with privileged access at the network level for the Wing, Geographically Separated Units (GSU), and Tenants.",
                "Planned, coordinated, installed, and continuously analyzed system design, ensuring documentation is sufficient to justify enhancements to keep systems current.",
                "Worked with the CFP/customers to resolve integration or configuration related issues.",
                "Ensured upgrades to the base IT infrastructure are identified. Assisted customers in developing/submitting recommendations for equipment and funds.",
                "Assisted personnel in planning/developing new or additional infrastructure/architecture capabilities.",
                "Conducted feasibility studies to identify and analyze system failures and analyzes data to determine if trends exist which forecast the need for future replacement or modification of system hardware and software."
            ]
        },
        {
            "role": "Cyber Transport/ Client Systems Workcenter Supervisor",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "02/2001",
            "to_date": "Current",
            "description": [
                "Managed Cyber Transport/Client Systems work center personnel. Set and adjusted work priorities, evaluated, and counseled subordinates.",
                "Documented training of personnel using Computer based training system (TBA). Sustained and operated systems through effective troubleshooting, repair, PMI's, system performance testing/analysis.",
                "Maintained close working relationship with Communications Focal Point--production requirements/Remedy tickets."
            ]
        },
        {
            "role": "F-16 Ejection System Technician",
            "company": "Company Name",
            "location": "City, State",
            "from_date": "07/1996",
            "to_date": "07/2000",
            "description": [
                "Troubleshot, removed, tested, inspected, repaired, modified, and installed explosive and non-explosive components and assemblies on ejection systems.",
                "Performed preventative maintenance on over ninety different electronically fired explosive devices ensuring proper wiring and termination. Foreign object damage monitor, briefed wing commander monthly on findings.",
                "Ran entire supply system ensuring all parts and supplies were readily available. Hazardous materials monitor. Explosive inspector. Ensured proper grounding points were present in shop to prevent electrostatic discharge to explosive components."
            ]
        }
    ]
}


print(json.dumps(base_infer))
print(json.dumps(predict_infer))

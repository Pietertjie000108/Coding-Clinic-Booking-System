# Coding-Clinic-Booking-System

# Getting started
Type: "source bash.sh" into your terminal from the project directory. This installs all required packages and sets aliases.

Type: 'wtc-clinic' into your terminal after the bash script was run. 

The user is is able to use the program by running any of the modules in either the clinicians 
or the patients module. But when running any of those modules the user will need to provide valid args.
Here is how you run each of the modules.

# Python modules/Packages

## Clinicians:
    python3 create_clinician_slot.py [date (yyyy/mm/dd)] [time e.g 14:00] - creates a slot as a clinician.
    python3 delete_clinician_slot.py [slot id] - deletes slot youve created as a clinician.
    python3 view_clinician_slots.py - views all the slots youve created as a clinician.

## Patients:
    python3 view_patient_slots.py - views all the slots youve signed up to as a patient.
    python3 view_slots_for_patient_slots.py - views all the slots you can sign up to as a patient.
    python3 delete_patient_slots.py [slot id] - removes you as a patient from the slot youve signed up to.
    python3 signup_to_patient_slot.py [description, what you need help with] [slot id] - signs you up as a patient to a slot of your choice.

## Authentication:
    python3 pass_auth.py
    python3 new_user.py
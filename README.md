# Coding-Clinic-Booking-System

# bin: all the shell scripts
# src: all python scripts etc


# Run the program:

Run the following code to install the rich module:
    pip3 install rich
The user is is able to use the program by running any of the modules in either the clinicians 
or the patients module. But when running any of those modules the user will need to provide valid args.
Here is how you run each of the modules.
Clinicians:
    python3 create_clinician_slot.py [user name] [month (e.g november)] [day e.g 8] [time e.g 14:00] - creates a slot as a clinician.
    python3 delete_clinician_slot.py [user name] [slot id] - deletes slot youve created as a clinician.
    python3 view_clinician_slots.py [user name] - views all the slots youve created as a clinician.
Patients:
    python3 view_patient_slots.py [user name] - views all the slots youve signed up to as a patient.
    python3 view_slots_for_patient_slots.py [username] - views all the slots you can sign up to as a patient.
    python3 delete_patient_slots.py [user name] [slot id] - removes you as a patient from the slot youve signed up to.
    python3 signup_to_patient_slot.py [username] [description, what you need help with] [slot id] - signs you up as a patient to a slot of your choice.
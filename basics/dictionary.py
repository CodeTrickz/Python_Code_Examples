# Een dictionary met studentinformatie
studenten = {
    'student1': {
        'naam': 'Jan Jansen',
        'leeftijd': 20,
        'studierichting': 'Informatica'
    },
    'student2': {
        'naam': 'Eva de Vries',
        'leeftijd': 22,
        'studierichting': 'Elektrotechniek'
    },
    'student3': {
        'naam': 'Piet Petersen',
        'leeftijd': 21,
        'studierichting': 'Werktuigbouwkunde'
    }
}

# Toegang tot en weergave van informatie over een specifieke student
student_id = 'student2'
gevonden_student = studenten.get(student_id)

if gevonden_student:
    print(f"Informatie over {student_id}:")
    print(f"Naam: {gevonden_student['naam']}")
    print(f"Leeftijd: {gevonden_student['leeftijd']}")
    print(f"Studierichting: {gevonden_student['studierichting']}")
else:
    print(f"Student met ID {student_id} niet gevonden.")

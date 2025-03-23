def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Invalid input type. Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Invalid input type. Attendees must be a list.")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Invalid input type. Attendees must be a list of dictionaries.")
            return
    
    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee and generate files
    for index, attendee in enumerate(attendees, start=1):
        processed_text = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = 'N/A'
            else:
                value = str(value)
            processed_text = processed_text.replace(f'{{{key}}}', value)
        
        filename = f'output_{index}.txt'
        with open(filename, 'w') as file:
            file.write(processed_text)

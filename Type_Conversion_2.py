# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

# TODO: Split the crew_data string into a list of individual crew member information using the appropriate delimiter
member_list = crew_data.split(';')
# TODO: Iterate over the list of crew member data
for member_data in member_list:
    # TODO: For each member, split their data string using commas as delimiters
    member = ' '.join([field.strip() for field in member_data.split(',')])
    # TODO: Print the crew member's details in a formatted string
    print(member)
# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM
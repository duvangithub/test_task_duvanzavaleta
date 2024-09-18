#Classes
class Contacts:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Leads:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

#Data
contacts_list = [
    Contacts("Alice Brown", None, "1231112223"),
    Contacts("Bob Crown", "bob@crowns.com", None),
    Contacts("Carlos Drew", "carl@drewess.com", "3453334445"),
    Contacts("Doug Emerty", None, "4564445556"),
    Contacts("Egan Fair", "eg@fairness.com", "5675556667"),
]

leads_list = [
    Leads(None, "kevin@keith.com", None),
    Leads("Lucy", "lucy@liu.com", "3210001112"),
    Leads("Mary Middle", "mary@middle.com", "3331112223"),
    Leads(None, None, "4442223334"),
    Leads(None, "ole@olson.com", None),
]

#Function registes_attendes
def register_attendees(registrants, contacts_list, leads_list):
    #Check registrants info
    for registrant in registrants:
        email = registrant["email"]
        phone = registrant["phone"]

        #Check email in contact_list
        if any(contact.email == email for contact in contacts_list):
            continue

        #Check phone in contact_list
        if phone and any(contact.phone == phone for contact in contacts_list):
            continue

        #Check email in lead_list
        found_lead = None
        for lead in leads_list:
            if lead.email == email:
                found_lead = lead
                break

        if found_lead:
            #Lead in  contact list added to contacts
            contacts_list.append(Contacts(found_lead.name or registrant["name"], found_lead.email, found_lead.phone))
            leads_list.remove(found_lead)  #Remove from leads
            continue

        ##Check phone in lead_list
        if phone:
            found_lead = None
            for lead in leads_list:
                if lead.phone == phone:
                    found_lead = lead
                    break

            if found_lead:
                #Add the lead to contacts and remove it from leads
                contacts_list.append(Contacts(found_lead.name or registrant["name"], found_lead.email, found_lead.phone))
                leads_list.remove(found_lead)  #Remove from lead_list
                continue 


        #If there is no match add in contact_list
        contacts_list.append(Contacts(registrant["name"], email, phone))


#Data demo
"""registrants = [
    {"name": "Lucy", "email": "lucy@liu.com", "phone": None},  #Existing lead by email
    {"name": "Doug Emerty", "email": "doug@emmy.com", "phone": "4564445556"},  #Existing contact by phone
    {"name": "Duvan Zavaleta", "email": "duvzavaleta@gmail.com", "phone": None},  #New contact not found in contact or leads
]

#Function to register attendeess
register_attendees(registrants, contacts_list, leads_list)

#Print the list of contacts
print("\nContacts:")
for contact in contacts_list:
    print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

#Print the updated list of leads
print("\nLeads:")
for lead in leads_list:
    print(f"Name: {lead.name}, Email: {lead.email}, Phone: {lead.phone}")"""
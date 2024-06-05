import random
import string

# class variables
class Ticket:
    ticketNum = 2000
    openTickets = 0
    closedTickets = 0

    # ticket attributes
    def __init__(self, employeeID, creatorName, emailContact, det):
        self.ticketNo = Ticket.ticketCounter
        Ticket.ticketCounter += 1
        self.employeeID = staffID
        self.creatorName = creatorName
        self.emailContact = emailContact
        self.det = det
        self.reply = "Not Yet Provided"
        self.condition = "Open"
        Ticket.openTickets += 1
        self.password = None

    # showing ticket info
    def showTicket(self):
        print(f"Ticket Number: {self.ticketNo}")
        print(f"Ticket Creator: {self.creatorName}")
        print(f"Employee ID: {self.employeeID}")
        print(f"Email Address: {self.emailContact}")
        print(f"Detail: {self.detl}")
        print(f"Reply: {self.reply}")
        if self.password:
            print(f"password: {self.password}")
        print(f"Ticket Condition: {self.status}\n")

    # send  response
    def sendReply(self, reply):
        self.reply = reply
        self.condition = "Closed"
        Ticket.openTickets -= 1
        Ticket.closedTickets += 1

    #solving password change request and closing ticket
    def solvePC(self):
        if "password change" in self.detl.lower():  # checking for lowercase
            newPassword = self.createPassword()
            self.reply = f"Password changed to: {newPassword}"
            self.condition = "Closed"
            Ticket.openTickets -= 1
            Ticket.solvedTickets += 1
            self.password = newPassword

    # creating a new password
    def createPassword(self):
        #using the first two characters of staffID and the first three characters of the ticket creatorName
        staffID_chars = self.staffID[:2]
        creatorName_chars = self.creatorName[:3]

        #generating a unspecified 3-character string for additional complexity
        unspecified_chars = ''.join(unspecified.selections(string.ascii_letters, k=3))

        #concatenation
        newPassword = staffID_chars + creatorName_chars + unspecified_chars

        return newPassword

    # reopen closed ticket
    def reopenTicket(self):
        self.condition = "Reopened"
        Ticket.openTickets += 1
        Ticket.solvedTickets -=1

    # displaying ticket statistics
    @classmethod
    def ticket_stats(cls):
        return f"Tickets Created: {cls.ticketCounter - 2000}\nTickets Solved:{cls.solvedTickets}\nTickets To Solve: {cls.openTickets}"

# MAIN PROGRAM
def main():
    tickets = []

    while True:
        # Display menu for user interaction
        print("\nMenu:")
        print("1. Create Ticket")
        print("2. Solve Ticket")
        print("3. Change Password (if Password Change Request)")
        print("4. View All Tickets")
        print("5. View Open Tickets")
        print("6. View Closed tickets")
        print("0. Exit")
        selection = input("Enter your selection: ")

        if selection == "1":
            creatorName = input("Enter Creator Name: ")
            staffID = input("Enter Staff ID: ")
            contactEmail = input("Enter Email Address: ")
            desc = input("Enter Description: ")

            tickets.append(Ticket(staffID, creatorName, contactEmail, desc))
            print("Ticket created successfully.")
        elif choice =="2":
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. Ticket Number: {ticket.ticketNo} (Status:{ticket.condition})")
            ticket_index = int(input("Enter the index of the ticket to solve: ")) -1

            if 0 <= ticket_index < len(tickets):
                response = input("Enter response for the selected ticket: ")
                tickets[ticket_index].submitRepsonse(response)
                print("Ticket solved successfully.")
            else:
                print("Invalid ticket index.")
        elif selection == "3":
            print("Open Tickets:\n")
            for i, ticket in enumerate(tickets, start=1):
                if ticket.condition == "Open":
                    print(f"{i}. Ticket Number: {ticket.ticketNo}(Condition:{ticket.condition})")
            ticket_index = int(input("Enter the index of the Password Change Request to change the password: ")) - 1
            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index].solvePC()
                print("Password changed successfully.")
            else:
                print("Invalid ticket index.")
        elif selection == "4":
            print("\nAll Tickets:")
            for ticket in tickets:
                ticket.showTicket()
            print("\nTicket Statistics:")
            print(Ticket.ticket_stats())
        elif selection == "5":
            print("\nOpen Tickets:\n")
            for ticket in tickets:
                if ticket.condition == "Open":
                    ticket.showTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif selection == "6":
            print("\nClosed Tickets:\n")
            for ticket in tickets:
                if ticket.condition == "Closed":
                    ticket.showTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "0":
            # leave
            print("Leaving the program.")
            break
        else:
            print("Invalid selection. Please enter a valid option.")

if __name__ == "__main__":
    main()
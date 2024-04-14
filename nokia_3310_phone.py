class Nokia3310Phone:
    def main(self):
        prompt = """
        Nokia menu map 
        List of menu functions

        1 -> Phone book 
        2 -> Messages
        3 -> Chat
        4 -> Call register
        5 -> Tones
        6 -> Settings
        7 -> Call divert
        8 -> Games
        9 -> Calculator
        10 -> Reminders
        11 -> Clock
        12 -> Profiles
        13 -> SIM services
        """

        phoneBookPrompt = """
        1 -> Search
        2 -> Services Nos. 
        3 -> Add name
        4 -> Erase
        5 -> Edit
        6 -> Assign tone
        7 -> Send b'card
        8 -> Options
        9 -> Speed dials
        10 -> Voice tags
        11 -> Back
        """

        optionsPrompt = """
        1 -> Type of view
        2 -> Memory status
        3 -> Back
        """

        messagesPrompt = """
        1 -> Write messages
        2 -> Inbox
        3 -> Outbox
        4 -> Pictures messages
        5 -> Templates
        6 -> Simleys
        7 -> Message settings
        8 -> Info service
        9 -> Voice mailbox number
        10 -> Service command editor
        11 -> Back
        """

        messageSettingsPrompt = """
        1 -> Set 1
        2 -> Common
        3 -> Back
        """

        set1Prompt = """
        1 -> Message centre number
        2 -> Message sent as
        3 -> Message validity
        4 -> Back
        """

        commonPrompt = """
        1 -> Delivery reports
        2 -> Reply via same centre
        3 -> Character support
        4 -> Back
        """

        callRegisterPrompt = """
        1 -> Missed calls
        2 -> Received calls
        3 -> Dialled numbers
        4 -> Erase recent call lists
        5 -> Show call duration
        6 -> Show call costs
        7 -> Call cost settings
        8 -> Prepaid credit
        9 -> Back
        """

        showCallDurationPrompt = """
        1 -> Last call duration
        2 -> All calls' duration
        3 -> Received calls' duration
        4 -> Dialled calls' duration
        5 -> Clear timers
        6 -> Back
        """

        showCallCostsPrompt = """
        1 -> Last call cost
        2 -> All calls' cost
        3 -> Clear counters
        4 -> Back
        """

        callCostSettingsPrompt = """
        1 -> Call cost limit
        2 -> Show costs in
        3 -> Back
        """

        tonesPrompt = """
        1 -> Ringing tone
        2 -> Ringing volume
        3 -> Incoming call alert
        4 -> Composer
        5 -> Message alert tone 
        6 -> Keypad tones
        7 -> Warning and game tones
        8 -> Vibrating alert
        9 -> Screen saver
        10 -> Back
        """

        settingsPrompt = """
        1 -> Call settings
        2 -> Phone settings
        3 -> Security settings
        4 -> Restore factory settings
        5 -> Back
        """

        callSettingsPrompt = """
        1 -> Automatic redial
        2 -> Speed dialling
        3 -> Call waiting options
        4 -> Own number sending
        5 -> Phone line in use 
        6 -> Automatic answer
        7 -> Back
        """

        phoneSettingsPrompt = """
        1 -> Language 
        2 -> Cell info display 
        3 -> Welcome note
        4 -> Network selection
        5 -> Lights
        6 -> Confirm SIM service actions
        7 -> Back
        """

        securitySettingsPrompt = """
        1 -> PIN code request
        2 -> Call barring service
        3 -> Fixed dailling
        4 -> Closed user group
        5 -> Phone security
        6 -> Change access codes
        7 -> Back
        """

        clockPrompt = """
        1 -> Alarm clock
        2 -> Clock setting
        3 -> Date setting
        4 -> Stopwatch
        5 -> Countdown timer
        6 -> Auto update of date and time
        7 -> Back
        """

        print(prompt)
        userInput = int(input("Enter your choice: "))
        count = 1

        while count <= 100:
            if userInput == 1:
                print("Phone book")
                count += 1
                print(phoneBookPrompt)
                digitEntered = int(input("Enter your choice: "))
                if digitEntered == 8:
                    print("Options")
                    print(optionsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 3:
                        print(phoneBookPrompt)
                elif digitEntered == 11:
                    print(prompt)
            elif userInput == 2:
                print("Messages")
                print(messagesPrompt)
                digitEntered = int(input("Enter your choice: "))
                if digitEntered == 7:
                    print("Message Settings")
                    print(messageSettingsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 1:
                        print("Set 1")
                        print(set1Prompt)
                        takeInput = int(input("Enter your choice: "))
                        if takeInput == 4:
                            print(messageSettingsPrompt)
                    elif digitInput == 2:
                        print("Common")
                        print(commonPrompt)
                        takeInput = int(input("Enter your choice: "))
                        if takeInput == 4:
                            print(messageSettingsPrompt)
                elif digitEntered == 11:
                    print(prompt)
            elif userInput == 4:
                print("Call register")
                print(callRegisterPrompt)
                digitEntered = int(input("Enter your choice: "))
                if digitEntered == 5:
                    print("Show call duration")
                    print(showCallDurationPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 6:
                        print(callRegisterPrompt)
                elif digitEntered == 6:
                    print("Show call costs")
                    print(showCallCostsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 4:
                        print(callRegisterPrompt)
                elif digitEntered == 7:
                    print("Call cost settings")
                    print(callCostSettingsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 3:
                        print(callRegisterPrompt)
                elif digitEntered == 9:
                    print(prompt)
            elif userInput == 5:
                print("Tones")
                print(tonesPrompt)
                digitEntered = int(input("Enter your choice: "))
                if digitEntered == 10:
                    print(prompt)
            elif userInput == 6:
                print("Settings")
                print(settingsPrompt)
                digitEntered = int(input("Enter your choice: "))
                if digitEntered == 1:
                    print("Call settings")
                    print(callSettingsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 7:
                        print(settingsPrompt)
                elif digitEntered == 2:
                    print("Phone settings")
                    print(phoneSettingsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 7:
                        print(settingsPrompt)
                elif digitEntered == 3:
                    print("Security settings")
                    print(securitySettingsPrompt)
                    digitInput = int(input("Enter your choice: "))
                    if digitInput == 7:
                        print(settingsPrompt)
            elif userInput == 11:
                print("Clock")
                print(clockPrompt)
                digitInput = int(input("Enter your choice: "))
                if digitInput == 7:
                    print(prompt)
            elif userInput == 3:
                print("Chat")
            elif userInput == 7:
                print("Call divert")
            elif userInput == 8:
                print("Games")
            elif userInput == 9:
                print("Calculator")
            elif userInput == 10:
                print("Reminders")
            elif userInput == 12:
                print("Profiles")
            elif userInput == 13:
                print("SIM services")
            else:
                print("Invalid input")

if __name__ == "__main__":
    Nokia3310Phone().main()

from pyscript import document

def eligibility(event):
    # Get values
    section = document.getElementById("section").value
    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')
    result = document.getElementById("result")

    if not registration or not medical: #not method
        result.innerText = "Please complete registration and medical clearance."
        return

    if registration.value == "no":
        result.innerText = "Please register online to join the Intramurals."
        return

    if medical.value == "no":
        result.innerText = "Please secure a medical clearance."
        return

    if section == "" or section == "other":
        result.innerText = "Not eligible to join the Intramurals."
        return
    
    if section == "10 Ruby":  #if-elif statements
        team = "Green Hornets"
    elif section == "10 Sapphire":
        team = "Red Bulldogs"
    elif section == "10 Emerald":
        team = "Green Hornets"
    elif section == "10 Topaz":
        team = "Yellow Tigers"

    elif section == "9 Sapphire":
        team = "Red Bulldogs"
    elif section == "9 Emerald":
        team = "Green Hornets"
    elif section == "9 Topaz":
        team = "Yellow Tigers"
    elif section == "9 Jade":
        team = "Blue Bears"
    elif section == "9 Ruby":
        team = "Red Bulldogs"

    elif section == "8 Sapphire":
        team = "Red Bulldogs"
    elif section == "8 Emerald":
        team = "Green Hornets"
    elif section == "8 Topaz":
        team = "Yellow Tigers"
    elif section == "8 Jade":
        team = "Blue Bears"
    elif section == "8 Ruby":
        team = "Red Bulldogs"

    elif section == "7 Sapphire":
        team = "Red Bulldogs"
    elif section == "7 Emerald":
        team = "Green Hornets"
    elif section == "7 Topaz":
        team = "Yellow Tigers"
    elif section == "7 Jade":
        team = "Blue Bears"
    elif section == "7 Ruby":
        team = "Red Bulldogs"
    else: #else statement if it doesn't satisfy the if statements above
        result.innerText = "Not eligible to join Intrams."
        return
   

    result.innerText = f"Congratulations! Your team is {team} 🏆!"
    #this the phrase that shows up when you are eligible to join, and when it shows you your team.

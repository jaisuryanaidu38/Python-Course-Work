#Blood Bank Management System

# 1. int
donor_id = int(input("Enter Donor ID: "))

# 2. str
donor_name = input("Enter Donor Name: ")

# 3. float
blood_quantity = float(input("Enter Blood Quantity Donated (ml): "))

# 4. list
donation_history = input("Enter previous donation dates (comma separated): ").split(",")

# 5. tuple
day = int(input("Enter Last Donation Day: "))
month = int(input("Enter Last Donation Month: "))
year = int(input("Enter Last Donation Year: "))
last_donation_date = (day, month, year)

# 6. set
blood_groups = set(input("Enter available blood groups (comma separated): ").split(","))

# 7. dict
donor_record = {
    "Donor ID": donor_id,
    "Donor Name": donor_name,
    "Blood Quantity (ml)": blood_quantity,
    "Donation History": donation_history,
    "Last Donation Date": last_donation_date,
    "Blood Groups Available": blood_groups
}

# Output
print("\n----- BLOOD DONOR DETAILS -----")
print("Donor ID:", donor_record["Donor ID"])
print("Donor Name:", donor_record["Donor Name"])
print("Blood Quantity (ml):", donor_record["Blood Quantity (ml)"])
print("Donation History:", donor_record["Donation History"])
print("Last Donation Date:", donor_record["Last Donation Date"])
print("Blood Groups Available:", donor_record["Blood Groups Available"])
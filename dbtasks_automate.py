import os

def main():
    while True:
        print("Press 1: Export data from campaign_context")
        print("Press 2: Export data from users")
        print("Press 3: Export data for disposition plan")
        print("Press q to quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            export_campaign_data()
        elif choice == "2":
            export_users_data()
        elif choice == "3":
            disposition_plan_name = input("Enter the disposition_plan_name: ")
            export_disposition_data(disposition_plan_name)
        elif choice.lower() == "q":
            print("Exiting the script...")
            break
        else:
            print("Invalid choice. Please try again.")

def export_campaign_data():
    cmd = """psql -U postgres -c "COPY (SELECT * FROM campaign_context) TO '/tmp/campaign.csv' DELIMITER ',' CSV HEADER;" """
    execute_command(cmd)

def export_users_data():
    cmd = """psql -U postgres -c "COPY (SELECT * FROM users) TO '/tmp/userslist.csv' DELIMITER ',' CSV HEADER;" """
    execute_command(cmd)

def export_disposition_data(disposition_plan_name):
    cmd = f"""psql -U postgres -c "COPY (SELECT dpd.disposition_plan_id, dp.disposition_plan_name, dc.disposition_class_name, dc.disposition_code_name FROM disposition_class dc INNER JOIN disposition_code dco ON dc.id = dco.disposition_class_id INNER JOIN disposition_plan_definition dpd ON dco.id = dpd.disposition_code_id INNER JOIN disposition_plan dp ON dpd.disposition_plan_id = dp.id WHERE dp.disposition_plan_name = '{disposition_plan_name}' ORDER BY dpd.disposition_plan_id ASC) TO '/tmp/September_2021_S1_Exclusion.csv' DELIMITER ',' CSV HEADER;" """
    execute_command(cmd)

def execute_command(cmd):
    try:
        os.system(cmd)
        print("Command executed successfully.")
    except Exception as e:
        print(f"Error executing command: {e}")

# Call the main function directly
if __name__ == "__main__":
    main()

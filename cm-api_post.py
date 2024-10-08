import subprocess
import json

def API_Operation():
    try:
        customer_leadid = int(input("Enter the customerLeadID: "))
        print("customerLeadid =", customer_leadid)
    except ValueError:
        print("Only integers are allowed")
        return  # Exit the function if input is invalid

    try:
        contact_number = input("Enter the phone number: ")
        if len(contact_number) == 10:
            print("Customer Contact Number:", contact_number)
        else:
            print("Enter a ten digit number")
            return  # Exit the function if the number is not valid
    except Exception as e:
        print(f"Error while taking input for contact number: {e}")
        return  # Exit the function if there is an exception

    # Build the data separately
    data = {
        "campaignId": 412,
        "customerAndCallbackRecords": [{
            "customerRecord": {
                "phone": contact_number,
                "leadid": customer_leadid,
                "pin_code": "400009",
                "state": "Maharashtra",
                "city": "Mumbai",
                "ucic": 11223,
                "first_name": "hiten",
                "last_name": "rahuja",
                "lead_source": "lovepreet",
                "online_drop_stage": "AL2",
                "product_code": "saving",
                "product_category": "MF SIP",
                "product_type": "MF SIP - Online",
                "ace_plegible_limit": "",
                "ace_playailable_limit": "",
                "requested_loan_amount": "",
                "tenure_in_days": "",
                "roi": "",
                "credit card type": "",
                "credit card offer amount": "",
                "credit card apr": "",
                "time_stamp": "",
                "email_address": "",
                "destination_country": "India",
                "current_city": "",
                "campaign_name": "",
                "affluence_band": "",
                "additional_fields2": "",
                "IFB_AUS1_First_Name__c": "",
                "IFB_AUS2_First_Name__c": ""
            }
        }],
        "leadId": 65517,
        "properties": {
            "update.customer": True,
            "migrate.customer": True
        },
        "attempts": 0
    }

    # Convert the data to a JSON string
    data_str = json.dumps(data)

    command = f"""curl --location --request POST 'https://contactcentreruat.ibnbank.com:843/ameyowebaccess/command?command=uploadContactAndAddCallback' \
    --header 'hash-key: fecace70bf6ea0450c5b2071dacf92' \
    --header 'policy-name: token-based-authorization-policy' \
    --header 'requesting-host: DCAMY0A0PUTR1' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'data={data_str}'"""

    response = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    print(response.stdout)
    if response.stderr:
        print("Error:", response.stderr)

API_Operation()

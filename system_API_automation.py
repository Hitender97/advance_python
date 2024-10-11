import logging
import subprocess
import requests

# Set up logging configuration
logging.basicConfig(filename="process_monitor.log", 
                    level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_message(level, message):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.debug(message)


def filter_and_log_processes(process_name):
    try:
        # Run ps aux and capture the output
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
        processes = [line for line in result.stdout.splitlines() if process_name in line]
        
        if processes:
            # Log and return the filtered processes
            log_message("info", f"Found {len(processes)} processes related to '{process_name}'.")
            for process in processes:
                log_message("info", f"Process: {process}")
            return processes
        else:
            log_message("info", f"No processes found for '{process_name}'.")
            return None
    except Exception as e:
        log_message("error", f"Error filtering processes: {e}")
        return None

def send_status_to_api(api_url, status_payload):
    try:
        response = requests.post(api_url, json=status_payload)
        response.raise_for_status()  # Raise an error for bad status codes
        log_message("info", f"API request successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        log_message("error", f"API request failed: {e}")

# Example usage of sending status
api_url = "https://example-monitoring.com/api/process-status"


def monitor_and_report_process_status(process_name, api_url):
    try:
        # Step 1: Filter and log processes
        processes = filter_and_log_processes(process_name)
        
        # Step 2: Prepare status payload for API
        if processes:
            status_payload = {
                "process_name": process_name,
                "status": "running",
                "count": len(processes),
                "details": [process.split() for process in processes]  # Send relevant process details
            }

        else:
            status_payload = {
                "process_name": process_name,
                "status": "not_running",
                "count": 0,
                "details": []
            }

        # Step 3: Send status to monitoring API
        send_status_to_api(api_url, status_payload)
    
    except Exception as e:
        # Log any unexpected errors in the entire monitoring process
        log_message("error", f"Error during process monitoring and reporting: {e}")

# Example usage
if __name__ == "__main__":
    # Define the process name to monitor and the API endpoint
    process_name = "NetworkManager"
    api_url = "https://example-monitoring.com/api/process-status"
    
    # Monitor the process and report status
    monitor_and_report_process_status(process_name, api_url)
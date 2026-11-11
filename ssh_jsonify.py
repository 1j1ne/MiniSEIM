import json
import re


SSH_log_pattern = r"^(?P<timestamp>\w{3}\s+\d{2}+\s+\d{2}+:\d{2}+:\d{2}+)\s(?P<hostname>\w+)\ssshd\[(?P<pid>\d{5})\]:\s(?P<message>.+)$"

SSH_log_example = ["Dec 10 07:28:35 LabSZ sshd[24271]: Failed password for root from 112.95.230.3 port 44900 ssh2"]



cleaned_log = []
def SSH_clean_log(SSH_log_example):
    for log in SSH_log_example:
        match = re.match(SSH_log_pattern, log)
        if match:
            cleaned_log.append({
                "timestamp": match.group("timestamp"),
                "hostname" : match.group("hostname"),
                "pid" : match.group("pid"),
                "message" : match.group("message")
            }
            )

        else :
            print("Log does not match expected format")
    return(cleaned_log)

# print(SSH_clean_log(SSH_log_example))


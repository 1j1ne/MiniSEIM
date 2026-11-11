import json
import re



Apache_log_pattern = r"^(?P<timestamp>\[\w{3}\s\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\s\d{4}\])\s(?P<loglevel>\[error\])\s(?:\[client\s(?P<ipaddress>\d+.\d+.\d+.\d+)\]\s)?(?P<message>\w.+)$"


Apache_raw_log = ["[Sun Jun 12 04:04:33 2005] [error] jk2_init() Can't find child 8728 in scoreboard",
           "[Fri Jun 10 11:40:14 2005] [error] [client 213.205.73.192] Invalid method in request get /scripts/..%e0%80%af../..%e0%80%af../..%e0%80%af../winnt/system32/cmd.exe?/c+dir",
           "[Fri Jun 10 14:21:15 2005] [error] [client 61.10.7.8] Directory index forbidden by rule: /var/www/html/"
           ]

def Apache_clean_log(raw_log):
    cleaned_log = []
    for log in raw_log:
        match = re.match(Apache_log_pattern, log)
        if match:
            cleaned_log.append({
                "timestamp": match.group("timestamp"),
                "loglevel" : match.group("loglevel"),
                "client_ip" : match.group("ipaddress"),
                "message" : match.group("message")
            }
            )

        else :
            print("Log does not match expected format")
    return(cleaned_log)


print(Apache_clean_log(Apache_raw_log))
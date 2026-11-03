import json
import re



Apache_log_example = re.compile(
    r'^\[([^\]]+)\]\s+'
    r'\[([^\]]+)\]\s+'
    r'(?:\[client\s+([^\]]+)\]\s+)?'
    r'(.*)$'
)


Apache_raw_log = ["[Fri Jun 10 11:32:39 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties",
           "[Fri Jun 10 11:40:14 2005] [error] [client 213.205.73.192] Invalid method in request get /scripts/..%e0%80%af../..%e0%80%af../..%e0%80%af../winnt/system32/cmd.exe?/c+dir",
           "[Fri Jun 10 14:21:15 2005] [error] [client 61.10.7.8] Directory index forbidden by rule: /var/www/html/"
           ]

def Apache_clean_log(raw_log):
    cleaned_log = []
    for log in raw_log:
        match = re.match(Apache_log_example, log)
        if match:
            timestamp = match.group(1)
            loglevel = match.group(2)
            client_ip = match.group(3)
            message = match.group(4)
            cleaned_log.append({
                "timestamp": timestamp,
                "loglevel" : loglevel,
                "client_ip" : client_ip,
                "message" : message
            }
            )

        else :
            print("Log does not match expected format")
    return(cleaned_log)

print(Apache_clean_log(Apache_raw_log))




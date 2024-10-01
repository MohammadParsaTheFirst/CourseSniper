import requests, time, random
from termcolor import colored, cprint

cprint("Hello!", "green")

auth = input(colored("Authorization Key: ", "yellow"))

courses = {
    # ADD Course 0
    # Move Group 1
    # Remove 2
    "25746-2": [0,'1'],
    "25746-3": [0,'1']
    #"25751-1" : [1, '3'],
    #"25741-1" : [2, '4'],
    #"25733-2" : [0, '3'],
    #"25769-1" : [0, '3'],
    #"25729-1" : [0, '3']
}

headers = {
    "Authorization": auth,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://my.edu.sharif.edu/courses/offered",
    "Origin": "https://my.edu.sharif.edu",
}

a=input("just hit a key!")

while True:
    for course in courses:
        if (courses[course][0] == 0):
            cprint(
                "[+] Sending ADD request for: " + course + " -> " + courses[course][1] + " units",
                "blue",
            )

            requests.post(
                "https://my.edu.sharif.edu/api/reg",
                headers=headers,
                json={"action": "add", "course": course, "units": courses[course][1]},
            )
            cprint("[+] Sent", "green")

        elif (courses[course][0] == 1):
            cprint(
                "[+] Sending MOVE request for: " + course + " -> " + courses[course][1] + " units",
                "cyan",
            )

            requests.post(
                "https://my.edu.sharif.edu/api/reg",
                headers=headers,
                json={"action": "move", "course": course, "units": courses[course][1]},
            )
            cprint("[+] Sent", "green")

        elif (courses[course][0] == 2):
            cprint(
                "[+] Sending REMOVE request for: " + course + " -> " + courses[course][1] + " units",
                "light_blue",
            )

            requests.post(
                "https://my.edu.sharif.edu/api/reg",
                headers=headers,
                json={"action": "remove", "course": course, "units": courses[course][1]},
            )
            cprint("[+] Sent", "green")

    cprint("[+] Waiting ...",'yellow')

    randAm = random.uniform(0,0.05) + 5

    time.sleep(randAm)

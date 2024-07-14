from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from colorama import Fore
import time
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
b = Fore.LIGHTBLUE_EX
m = Fore.MAGENTA
w = Fore.WHITE
list = []
ascii = '''
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                         
'''
def main():
    loading = f"{g}Loading...\n{y}Made by https://github.com/epickejclovek\n"
    for char in loading:
        print(char, flush=True, end="")
        time.sleep(0.1)
    print(f"{b}{ascii}")
    i = int(input(f"{y}How many user agents to generate>{m} "))
    e = input(f"{w}Generate to file? Y/N: ")
    if e.lower() == "y":
        print(f"{g}Generating please wait it can take a longer moment")
        for i in range(i):
            software_names = [
                SoftwareName.CHROME.value,
                SoftwareName.FIREFOX.value,
                SoftwareName.EDGE.value,
                SoftwareName.SAFARI.value,
                SoftwareName.OPERA.value
                ]

            operating_systems = [
                OperatingSystem.WINDOWS.value,
                OperatingSystem.LINUX.value,
                OperatingSystem.MAC.value,
                OperatingSystem.ANDROID.value,
                OperatingSystem.IOS.value
            ]

            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=None)
            user_agent = user_agent_rotator.get_random_user_agent()
            list.append(user_agent)
        with open("generated.txt", 'w') as file:
            generated = '\n'.join(list)
            file.write(generated)
            i += 1
            print(f"{g}Succesfully generated and saved {y}{i} {g}user agents")
    elif e.lower() == "n":
        for i in range(i):
            software_names = [
                SoftwareName.CHROME.value,
                SoftwareName.FIREFOX.value,
                SoftwareName.EDGE.value,
                SoftwareName.SAFARI.value,
                SoftwareName.OPERA.value
                ]

            operating_systems = [
                OperatingSystem.WINDOWS.value,
                OperatingSystem.LINUX.value,
                OperatingSystem.MAC.value,
                OperatingSystem.ANDROID.value,
                OperatingSystem.IOS.value
            ]

            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=None)
            user_agent = user_agent_rotator.get_random_user_agent()
            print(f"{g}Your generated user agent is:\n{y}{user_agent}")
    else:
        print(f"{r}Invalid choice. Try again!")
        main()
main()
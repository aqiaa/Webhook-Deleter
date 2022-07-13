import requests
import time
from pystyle import Colors, Colorate, Write


print(Colorate.Horizontal(Colors.blue_to_purple, """
╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗╦═╗
║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗   ║║║╣ ║  ║╣  ║ ║╣ ╠╦╝
╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  ═╩╝╚═╝╩═╝╚═╝ ╩ ╚═╝╩╚═
Legionalitty#1337""", 1))

webhook = Write.Input("\nEnter Webhook ->", Colors.blue_to_purple, interval=0.1)

r = requests.get(f"{webhook}")
if r.status_code == 200:
  Write.Print(f"Valid Webhook Deleting...", Colors.blue_to_purple, interval=0.1)
if r.status_code == 404:
  Write.Print(f"Invalid Wenhook", Colors.blue_to_purple, interval=0.1)

if r.status_code == 200:
  requests.delete(f"{webhook}")
  time.sleep(1)
  Write.Print(f"\nDeleted Webhook", Colors.blue_to_purple, interval=0.1)

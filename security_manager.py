import subprocess
import asyncio
import ctypes
from winsdk.windows.devices import radios
import os

# Disable USB ports by modifying power management settings
def block_usb_ports():
    # Get a list of all USB devices
    devices = os.listdir('/sys/bus/usb/devices')

    # Disable each USB device
    for device in devices:
        os.system('echo -n 0 > /sys/bus/usb/devices/{}/power/autosuspend'.format(device))


# Disable Bluetooth radios asynchronously
async def disable_bluetooth():
    # Get a list of all available radios
    all_radios = await radios.Radio.get_radios_async()
    
    # Iterate through radios and turn off Bluetooth if available
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            await this_radio.set_state_async(radios.RadioState.OFF)


# Disable Command Prompt by modifying the Windows Registry
def disable_command_prompt():
    try:
        # Registry key and value information
        key = r"HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System"
        value_name = "DisableCMD"
        value_data = 2  # 2 means disable

        # Set the registry key value to disable Command Prompt
        ctypes.windll.advapi32.RegSetKeyValueW(None, key, value_name, ctypes.c_ulong(value_data), 4)
        print("Command Prompt disabled successfully.")
    except Exception as e:
        print("Error:", e)


# Block access to specific websites by modifying the hosts file
def block_websites():
    # Path to the hosts file on Windows
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"  # Loopback IP address
    website_list = ["www.facebook.com", "facebook.com"]

    # Open the hosts file for reading and writing
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                print(f"{website} is already blocked.")
            else:
                # Write redirect entry to block the website
                file.write(redirect + " " + website + "\n")
                print(f"{website} is now blocked.")
    print("Blocking completed.")


# Main entry point of the script
if __name__ == "__main__":
    # Call functions to perform the desired tasks
    block_usb_ports()        # Disable USB ports
    asyncio.run(disable_bluetooth())  # Disable Bluetooth radios
    disable_command_prompt()          # Disable Command Prompt
    block_websites()         # Block specific websites

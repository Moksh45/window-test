import subprocess
import asyncio
import ctypes
from winsdk.windows.devices import radios
import os

def block_usb_ports():
    # Get a list of all USB devices
    devices = os.listdir('/sys/bus/usb/devices')

    # Disable each USB device
    for device in devices:
        os.system('echo -n 0 > /sys/bus/usb/devices/{}/power/autosuspend'.format(device))


async def disable_bluetooth():
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            await this_radio.set_state_async(radios.RadioState.OFF)


def disable_command_prompt():
    try:
        key = r"HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System"
        value_name = "DisableCMD"
        value_data = 2  # 2 means disable

        ctypes.windll.advapi32.RegSetKeyValueW(None, key, value_name, ctypes.c_ulong(value_data), 4)
        print("Command Prompt disabled successfully.")
    except Exception as e:
        print("Error:", e)


def block_websites():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Path for Windows
    redirect = "127.0.0.1"
    website_list = ["www.facebook.com", "facebook.com"]

    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                print(f"{website} is already blocked.")
            else:
                file.write(redirect + " " + website + "\n")
                print(f"{website} is now blocked.")
    print("Blocking completed.")

if __name__ == "__main__":
    block_usb_ports()
    asyncio.run(disable_bluetooth())
    disable_command_prompt()
    block_websites()


# System Automation Script

This repository contains a Python script designed to automate various system-related tasks on a Windows 10 virtual machine. The script aims to block USB ports, disable Bluetooth, restrict Command Prompt access, and block specific websites. Please note that these operations can have significant effects on system functionality, so use this script with caution and only in controlled environments.

## Prerequisites

- Windows 10 Virtual Machine: Ensure you have a Windows 10 virtual machine set up for testing purposes.
- Python: The script requires Python to be installed on the virtual machine.
- Python Libraries: The script relies on several Python libraries, including `winsdk.windows.devices` for managing radios. Install the required packages using the following command:
  ```
  pip install pywin32 asyncio
  ```

## Usage

1. **Clone the Repository**: Clone this repository to your Windows 10 virtual machine.

   ```bash
   git clone https://github.com/Moksh45/window-test.git

2. **Navigate to the Directory**: Change into the cloned repository's directory.

   ```bash
   cd window-test
   ```

3. **Run the Script**: Execute the script using the following command:

   ```bash
   python security_manager.py
   ```

   This will initiate the script and perform the specified system tasks.

## Script Overview

### `block_usb_ports()`

This function attempts to disable USB ports by modifying the power management setting of each USB device present on the system. It iterates through USB devices and sets their autosuspend power management parameter to 0.

### `disable_bluetooth()`

This asynchronous function disables Bluetooth radios by utilizing the `winsdk.windows.devices.radios` module. It retrieves a list of all radios and turns off the Bluetooth radio if available.

### `disable_command_prompt()`

This function modifies the Windows Registry to disable the Command Prompt for the current user. It uses the `ctypes` library to interact with Windows API functions.

### `block_websites()`

This function aims to block access to specific websites by modifying the `hosts` file located in the Windows system directory. It adds entries to redirect the listed websites to the loopback IP address (127.0.0.1), effectively blocking access to those sites.

## Important Notes

- **Caution**: The script performs powerful actions that can affect system behavior. Run the script in a controlled testing environment to understand its effects.
- **Permissions**: Ensure the script is executed with administrative privileges to modify system settings.
- **Error Handling**: The script lacks comprehensive error handling. Enhance error handling mechanisms before using in a production setting.
- **Safety Precautions**: Provide users with clear warnings about the potential risks and how to revert changes.


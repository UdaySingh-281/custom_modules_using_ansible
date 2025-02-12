This repository demonstrates how to create and use custom Ansible modules written in Python.

* Overview - Ansible provides built-in modules for various automation tasks, but sometimes you need custom modules to extend functionality. Here, I have implemented two custom modules:

  * User Greeting Module – Prints a personalized greeting message.
  * System Information Module – Retrieves system details such as hostname, OS version, CPU architecture, and memory usage.
### Project Structure

  * custom_modules_using_ansible/
  * │── library/
   * │   ├── user_greeting.py
   * │   ├── system_info.py
  * │── inventory.ini
  * │── playbook.yml
  * │── README.md

* library/ – Contains the custom Python modules.
* inventory.ini – Defines target hosts for Ansible execution.
* playbook.yml – Calls the custom modules and processes their output.
* README.md – Project documentation.

### Prerequisites
Before running the playbook, ensure:

* Ansible is installed on your control node.
* Python 3 is available on both the control node and target machines.
* The target machine has psutil installed (for system information module)

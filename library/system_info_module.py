from ansible.module_utils.basic import AnsibleModule
import platform
import psutil
import os

def main():

    module = AnsibleModule(argument_spec={})

    system_specs = {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "cpu_cores": os.cpu_count(),
        "total_memory": round(psutil.virtual_memory().total / (1024 * 1024), 2)
    }

    module.exit_json(changed= False, **system_specs)

if __name__ == '__main__':
    main()

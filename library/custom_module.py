from ansible.module_utils.basic import AnsibleModule

def main():
    # Define arguments properly
    module_args = dict(
        name=dict(type='str', required=True)  # Ensure `name` is correctly defined
    )

    # Initialize AnsibleModule correctly
    module = AnsibleModule(argument_spec=module_args)

    # Retrieve the parameter
    name = module.params['name']

    # Prepare response
    response = {"message": f"Hello, {name}!"}

    # Return response
    module.exit_json(changed=False, **response)

if __name__ == '__main__':
    main()


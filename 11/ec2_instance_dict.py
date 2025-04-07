## dictionary start with 0
ec2_instance_dictionary_list = [ ## list
    { ## dictionary
        "name": "dev-instance",
        "id": "instance-001",
        "type": "t2.micro"
    },
    {
        "name": "test-instance",
        "id": "instance-002",
        "type": "t2.medium"
    },
    {
        "name" : "preprod-instance",
        "id": "instance-003",
        "type": "t2.large"
    }
    ]

print(ec2_instance_dictionary_list[1]["id"])
print(ec2_instance_dictionary_list[1]["name"])
print(ec2_instance_dictionary_list[1]["type"])
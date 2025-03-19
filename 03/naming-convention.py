# Naming convention

# prefer small letters
# _ or - underscore or dash in the middle to divide the string
# snake casing - name_of_the_ec2 = myec2, env_ec2, ec2_instance_name, etc
# camel casing - nameOfTheEc2 = myEc2, envEc2, ec2InstanceName, etc


name_of_the_server = ("prod_server", "ec2_env_stage", "ec2_instance_name")
print(name_of_the_server)

nameOfTheMachine = ("prodServer", "ec2EnvStage", "ec2InstanceName")
print(nameOfTheMachine)
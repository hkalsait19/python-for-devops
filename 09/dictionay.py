# ## Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed.
# ## Dictionary is defined by curly braces {} and each item is separated by comma(,).
# ## Key and value are separated by colon.
# ## Key should be unique and immutable.
# ## Value can be of any type.
# ## Dictionary is mutable, we can add, remove and update elements.
# ## Dictionary is unordered, so we can't access elements using index.


# my_dictionary = {'name': 'John', 
#                  'age': 25, 
#                  'city': 'New York'
#     }
# print(my_dictionary['city'])

# ## Update element
# my_dictionary['age']= 28
# print(my_dictionary['age'])


# ## Add element
# my_dictionary['occupation'] = 'Engineer'
# print(my_dictionary)

# ## Remove element
# del my_dictionary['city']
# print(my_dictionary)

# my_dictionary.pop('occupation')
# print(my_dictionary)

## ec2_instance_info

ec2_instance_info = [
    {
        'instance_id': 'i-123456',
        'instance_type': 't2.micro'
    },
    {
        'instance_id': 'i-789012',
        'instance_type': 't2.small'
    },
    {
        'instance_id': 'i-345678',
        'instance_type': 't2.medium'
    },
    {
        'instance_id': 'i-901234',
        'instance_type': 't2.large'
    }
]

print(ec2_instance_info[0]['instance_type'])
print(ec2_instance_info[2]['instance_type'])
print(ec2_instance_info[1]['instance_id'])
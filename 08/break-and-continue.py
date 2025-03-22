## break and continue
# break: To stop the loop

numbers=[1,2,3,4,5]
for number in numbers:
    if number==3:
        break
    print(number)

# continue: To skip the current iteration and continue with the next iteration

numbers=[1,2,3,4,5]
for number in numbers:
    if number==3:
        continue
    print(number)
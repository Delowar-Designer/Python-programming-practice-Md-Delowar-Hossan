# Light on-off Project
check = ""
light_on = False
while(check != 'sleep'):
    check = input("> ").lower()
    if check == 'on':
        if light_on:
            print("Light is already in on Mode")
        else:
            light_on = True
            print("Light turned on mode")
    elif check == 'off':
        if not light_on:
            print("Light is already in off Mode")
        else:
            light_on = False
            print("Light turned off mode")
    elif check == 'sleep':
        break
    elif check == 'help':
        print("""1. on - Light on 
2. off - Light off
3. Sleep - exit program
        """)
    else:
        print("I don't understand your commnd.....")

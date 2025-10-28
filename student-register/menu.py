def select_multi_option(options: list, title = ""):
    while True:

        print()

        if title:
            print(title)

        for idx in range(len(options)):
            print(f"{idx+1}. {options[idx]}")

        try:
            selected_options_str = input("select: ").split()
        except KeyboardInterrupt:
            return []

        selected_options_int = []

        is_invalid = False

        for idx in range(len(selected_options_str)):
            opt = selected_options_str[idx]
            try:
                opt = int(opt)
            except ValueError:
                print(f"Option \"{opt}\" is not a number.")
                is_invalid = True
                break

            if 0 < opt <= len(options) and opt-1 not in selected_options_int:
                selected_options_int.append(opt-1)
            else:
                print(f"Number {opt} is not in range.")
                is_invalid = True
                break

        if is_invalid:
            continue

        return sorted(selected_options_int)

def confirm_return(title = ""):
    try:
        input(f"{title}Press <Enter> to return. ")
    except KeyboardInterrupt:
        pass

def select_int_range(title, min, max):
    while True:
        num = ""
        try:
            num = input(title)
        except KeyboardInterrupt:
            return -1

        try:
            num = int(num)
        except ValueError:
            print("Not a number!\n")
            continue
        if min <= num <= max:
            return num
        else:
            print(f"Number not in range ({min}-{max})\n")

def confirm(question):
    while True:
        ans = ""

        try:
            ans = input(f"{question} (Y/n): ")
        except KeyboardInterrupt:
            return False
        
        match ans.lower():
            case "" | "y":
                return True
            case "n":
                return False

def select_action(actions, title = ""):
    options = []

    for action in actions.keys():
        options.append(action)

    print()

    if title:
        print(title)

    idx = 0
    for opt in options:
        print(f"{idx+1}. {opt}")

        idx += 1

    selected_option_idx = select_int_range(f"Select option (1-{len(options)}): ", 1, len(options)) -1

    if selected_option_idx < 0: # if you pressed <Ctrl+c>
        return True

    selected_option = options[selected_option_idx]

    action = actions[selected_option]

    if action:
        exit_loop = action()

        if exit_loop:
            return True

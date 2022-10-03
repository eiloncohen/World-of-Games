def check_input_validation(choose, start_range, end_range):
    """
    check_input_validation check if the input is valid or not
    param choose: get the chosen value of player
    param start_range: the first number of the range
    param end_range: the last number of the range that exclude from range
    return: if the input is valid or not
    """
    if not choose.isdigit():
        return False
    elif float(choose) not in range(start_range, end_range):
        return False
    else:
        return True
def sum_numbers(*values):
    '''
    takes a varable number of inputs and adds them together
    :param args:
    :return:
    '''
    result = 0
    for numb in values:
        result += numb
    return result


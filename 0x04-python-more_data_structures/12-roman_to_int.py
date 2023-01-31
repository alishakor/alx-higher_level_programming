#!/usr/bin/python3
def roman_to_int(roman_string):
    """ Converts a roman numeral to an integer


    Args:
        roman_string(str): contains roman numerals

    Returns:
        int: The return value. int for success,
        if the roman_string is not a string or 
            None, return 0



        converts I to 1
        converts V to 5
        converts X to 10
        converts L to 50
        converts C to 100
        converts D to 500
        converts M to 1000 

        if the next roman numeral alphabet is greater than the 
        succeeding one,add the current numeral and subtract if otherwise. 
    """


    int_value = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


    for i in range(len(roman_string)):
        if roman_string[i] in roman_dict.keys():
            if roman_dict.get(roman_string[i], 0) == 0:
                return (0)
            if i != len(roman_string) - 1 and 
					roman_dict.get(roman_string[i+1]) > roman_dict.get(roman_string[i]):
    			int_value -= roman_dict.get(roman_string[i])
            else: 
                int_value += roman_dict.get(roman_string[i])
    return (int_value) 

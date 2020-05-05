#Lab3

def average_number(s):
    '''
    (str) -> float

    Given s, a string representation of a sequence of four floating
    point numbers formatted as 'number1,number2,number3,number4',
    e.g., '1.0,12.0,13.0,2.0', remove the largest and smallest number,
    calculate the average of the remaining two numbers, which in this case are
    (13.0, 2.0), and return the average in s as a floating point number (e.g. 7.5).

    >>> average_number('10.0,20.0,30.0,0.0')
    15.0
    '''
    number1 = float(s[0:3])
    number2 = float(s[5:8])
    number3 = float(s[10:13])
    number4 = float(s[15:18])
    if number1>number2>number3>number4 or number1>number3>number2>number4 or number4>number2>number3>number1 or number4>number3>number2>number1:
        average_number = (number2+number3)/2
    elif number1>number2>number4>number3 or number1>number4>number2>number3 or number3>number2>number4>number1 or number3>number4>number2>number1:
        average_number = (number2+number4)/2
    elif number3>number1>number2>number4 or number3>number2>number1>number4 or number4>number1>number2>number3 or number4>number2>number1>number3:
        average_number = (number1+number2)/2
    elif number2>number1>number3>number4 or number2>number3>number1>number4 or number4>number1>number3>number2 or number4>number3>number1>number2:
        average_number = (number1+number3)/2
    elif number2>number1>number4>number3 or number2>number4>number1>number3  or number3>number1>number4>number2 or number3>number4>number1>number2:
        average_number = (number1+number4)/2
    elif number2>number3>number4>number1 or number2>number4>number3>number1 or number1>number3>number4>number2 or number1>number4>number3>number2:
        average_number = (number3+number4)/2

    return average_number


def first_name_last_name_to_email(name):
    '''
    (str) -> str

    Given a string name with the format "last_name first_name", return a string
    "first_name.last_name@mail.utoronto.ca", where all letters are lowercase.

    >>> first_name_last_name_to_email('Hastings Hana')
    'hana.hastings@mail.utoronto.ca'
    '''
    strAll = name
    strTarget = ' '
    place = strAll.find(strTarget)
    firstName = strAll[place+1:]
    lastName = strAll[:place]
    first_name=firstName.lower()
    last_name=lastName.lower()
    return first_name+"."+last_name+"@mail.utoronto.ca"

    


def student_midterm_mark(name, test_marks):
    '''
    (str, str) -> str

    Given a student's name, with the format "last_name first_name", test
    marks formatted as 'floating_point_number1, floating_point_number2,
    floating_point_number3, floating_point_number_4', return a string
    "<email_address,midterm_mark>", where email_address has the format
    first_name.last_name@utoronto.ca and the midterm_mark is the average number
    in the sequence test_marks excluding the largest and smallest scores.
    All letters in email_address are lowercase. Note: return the string
    with no space after the comma

    >>> student_midterm_mark("Hastings Hanna",'10.0,20.0,30.0,0.0')
    '<hanna.hastings@mail.utoronto.ca,15.0>'
    '''
    strAll = name
    strTarget = ' '
    place = strAll.find(strTarget)
    firstName = strAll[place+1:]
    lastName = strAll[:place]
    first_name=firstName.lower()
    last_name=lastName.lower()
    email_address =first_name+"."+last_name+"@mail.utoronto.ca"


    s = test_marks
    floating_point_number1 = float(s[0:3])
    floating_point_number2 = float(s[5:8])
    floating_point_number3 = float(s[10:13])
    floating_point_number4 = float(s[15:18])
    number1=floating_point_number1
    number2=floating_point_number2
    number3=floating_point_number3
    number4=floating_point_number4

    
    if number1>number2>number3>number4 or number1>number3>number2>number4 or number4>number2>number3>number1 or number4>number3>number2>number1:
        average_number = (number2+number3)/2
    elif number1>number2>number4>number3 or number1>number4>number2>number3 or number3>number2>number4>number1 or number3>number4>number2>number1:
        average_number = (number2+number4)/2
    elif number3>number1>number2>number4 or number3>number2>number1>number4 or number4>number1>number2>number3 or number4>number2>number1>number3:
        average_number = (number1+number2)/2
    elif number2>number1>number3>number4 or number2>number3>number1>number4 or number4>number1>number3>number2 or number4>number3>number1>number2:
        average_number = (number1+number3)/2
    elif number2>number1>number4>number3 or number2>number4>number1>number3  or number3>number1>number4>number2 or number3>number4>number1>number2:
        average_number = (number1+number4)/2
    elif number2>number3>number4>number1 or number2>number4>number3>number1 or number1>number3>number4>number2 or number1>number4>number3>number2:
        average_number = (number3+number4)/2
    midterm_mark = str(average_number)

    
    return "<"+email_address+","+midterm_mark+">" 
    
    
    


from challenge_tests import assert_equal


def day_of_year(day, month, year):
    """ A function to determine what day of the year it is
    Parameters
    ----------
    day : int
        The day of the month
    month : int
        The month of the year
    year : int
        The year which the day is being calculated
    """
    """
    The day of the year is 
        days that have passed in the current month + days in the prior months

    So that April 3, 2015 (non-leap year)
        3 (3rd day of month 4) + 31 (days in March) + 28 (days in Feb) + 31 (days in Jan)
    """

    # Start with total_days set the day of the month requested
    # for each month prior to the month asked for
    #   add the number of days in that month
    # if it's leap year and after Feb,  then add 1.

    # define the days in every month of the year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Start with total_days set the day of the month requested
    total_days = day

    # for each month prior to the month asked for
    #   add the number of days in that month
    for m in range(month - 1):
        total_days = total_days + days_in_month[m]

    # if it's leap year and after Feb,  then add 1.
    if (month > 2) and is_leap_year(year):
        total_days = total_days + 1

    return total_days


def is_leap_year(y):
    """
    Determine whether this is leap year

    Parameters:
    ----------
    y : int
        year to be checked

    Returns:
    -------
    bool
        True if it is a leap year, otherwise False
    """
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))


def relations(family_tree, relationship):
    """ Determine the relationship between two people in a given family
    
    Parameters
    ----------
    family_tree : list of tuple of str
        The family tree is defined by tuples of mother/daughter pairs 
        where the first item in the tuple is the mother of the second name in the tuple.
    relationship: tuple of str
        The relationship to be determined of the second person in the tuple to the first person in the tuple
        
    Returns
    -------
    str : {'Grandmother','Granddaughter','Mother','Daughter','Sister','Cousin','Aunt','Niece'}
        The relationship of the second person in the `relationship` tuple to the first person in the tuple
        
    """
    """
    ******
    I know that while mothers can have multiple daughters, each daughter can only have one mother
    therefore if I store the pair together, then I can lookup the daughters and find out who their mother is
    from there it's just a matter of looking at the types of relationships available
    ******
    """

    # Create a key:value pair where the child is the key and the parent is the value
    # Break out the tuple passed in into two variables
    # Find the mother of each of the names in tuple
    # Find the grandmother of each relationship in the tuple
    # If the mother of gen_1 == gen_2 then gen_2 is the MOTHER
    # If the mother of gen_2 == gen_1 then gen_2 is the DAUGHTER
    # If the mothers are the same, then they are SISTERS
    # If the grandmothers are the same, then they are COUSINS
    # If the grandmother of gen_2 == gen_1 then gen_2 is the GRANDDAUGHTER
    # If the grandmother of gen_1 == gen_2 then gen_2 is the GRANDMOTHER
    # If the grandmother of gen_1 = mother of gen_2 then gen_2 is an AUNT
    # If the mother of gen_1 == the grandmother of gen_2 then gen2 is a NIECE

    parents = {}

    for parent, child in family_tree:
        # Build a list of children by specifying the parent
        parents[child] = parent

    # Now get the targets
    gen_1 = relationship[0]
    gen_2 = relationship[1]

    # Find the mother of each of the names in tuple
    gen_1_parent = parents.get(gen_1)
    gen_2_parent = parents.get(gen_2)
    # Find the grandmother of each relationship in the tuple
    gen_1_parent_parent = parents.get(gen_1_parent)
    gen_2_parent_parent = parents.get(gen_2_parent)

    # I broke a rule here by `returning` in multiple places
    #  I've done this for clean code I didn't want a huge
    #  if-else tree
    # Also important - the order of comparisons, because we might have blank == blank
    if gen_2 == gen_1_parent:
        return "Mother"
    if gen_2 == gen_1_parent_parent:
        return "Grandmother"
    if gen_1 == gen_2_parent:
        return "Daughter"
    if gen_1 == gen_2_parent_parent:
        return "Granddaughter"
    if gen_1_parent == gen_2_parent:
        return "Sister"
    if gen_1_parent_parent == gen_2_parent_parent:
        return "Cousin"
    if gen_1_parent_parent == gen_2_parent:
        return "Aunt"
    if gen_1_parent == gen_2_parent_parent:
        return "Niece"


def monogram(full_name):
    """
    Creates a traditional monogram from a supplied full name
    """
    # Split the string (on spaces) but only split it twice
    first, middle, last = full_name.split(" ", 2)

    # Make sure the first/middle initial is lowercase, last is uppercase
    first_initial = first[0].lower()
    middle_initial = middle[0].lower()
    last_initial = last[0].upper()

    return f"{first_initial}.{last_initial}.{middle_initial}"


def dispense_cash(amount):
    """ Determine the minimum number of ATM bills to meet the requested amount to dispense
    
    Parameters
    ----------
    amount : int
        The amount of money requested from the ATM
        
    Returns
    -------
    int
        The number of bills needed, -1 if it can't be done
    """
    """
    If the amount isn't divisible by 10, then no need to bother cause it won't work
    Assuming it is divisible by 10, then let's fulfill the request starting with the 
    largest bills and moving to smaller bills
    """
    # Get the number of $500 bills that could be used
    # Total to dispense - (however much we gave in $500) figure out the 100s
    # Of what's left, how many $50 bills can we give
    # Again taking what's left, get the max number of 20s
    # Finally, if there is anything left it must be a 10
    total_bills = 0
    if amount % 10 != 0:
        return -1  # Can't be done, because it has to be a multiple of 10

    # How many $500 bills can we dispense
    b_500 = amount // 500  # The // operator does integer only division - such that 4 // 3 = 1
    left_over = amount % 500  # The 'mod' operator says give me the remainder of the division

    # How many $100 bills can we dispense
    b_100 = left_over // 100
    left_over = left_over % 100

    # How many $50 bills can we dispense
    b_50 = left_over // 50
    left_over = left_over % 50

    # How many $20 bills can we dispense
    b_20 = left_over // 20
    left_over = left_over % 20

    # How many $10 bills can we dispense
    b_10 = left_over // 10

    total_bills = b_500 + b_100 + b_50 + b_20 + b_10
    return total_bills


def fruit_calculator(question):
    # Set the quantity to zero
    # For each word in the string
    #   If the word is 'loses', then we are going to be subtracting
    #   If the word is a number, then convert it to an integer, if the
    #   If the previous word was a number (the value of number is not zero),
    #      then add this word to a dictionary as a key and add the number to the value
    # Find the last word, remove the '?' and look it up in dictionary - this is the value

    # Set the qty to zero
    qty = 0
    lose = False
    fruits = {}
    words = question.split(" ")
    # For each word in the string
    for w in words:

        # Since the split may include `.` or `,` we need to take these off
        w = w.rstrip(".").rstrip(",")
        if w == "loses":
            lose = True

        #   If the word is a number, then figure out if this is a gain, loss or just has
        if w.isdigit():
            qty = int(w)
            # Gains and Loses is 0 if there hasn't been a gain or loss
            if lose:
                qty = qty * -1
                # Need to reset the lose value to False
                lose = False

        else:
            #   If the previous word was a number (the value of qty is not zero),
            #      then add this word to a dictionary as a key and add the number to the value
            if qty != 0:
                fruits[w] = fruits.get(w, 0) + qty
                qty = 0

    # Find the last word, remove the '?' and look it up in dictionary - this is the value
    target_fruit = words[-1].rstrip("?")
    return fruits.get(target_fruit, 0)


def test_monogram():
    # Basic tests
    assert_equal(monogram("Dwight Kevin Shrute"), "d.S.k")
    assert_equal(monogram("Eye see deadpeople"), "e.D.s", hint="Did you check the case?")
    assert_equal(
        monogram("mers sadees benz II"), "m.B.s", hint="Did the extra suffix throw you off?"
    )


def test_atm():
    assert_equal(dispense_cash(1120), 4)
    assert_equal(dispense_cash(492), -1)
    assert_equal(dispense_cash(440), 6)
    assert_equal(dispense_cash(370), 5)
    assert_equal(dispense_cash(80), 3)


def test_family_tree():
    # Run this cell to test your work
    family_a = [("Enid", "Susan"), ("Susan", "Deborah")]
    family_b = [
        ("Enid", "Susan"),
        ("Susan", "Deborah"),
        ("Enid", "Dianne"),
        ("Dianne", "Judy"),
        ("Dianne", "Fern"),
    ]

    """
    Enid
    |
    Susan       Dianne
      |             |           |
    Deborah     Judy        Fern
    """

    assert_equal(relations(family_a, ("Enid", "Susan")), "Daughter")
    assert_equal(relations(family_b, ("Enid", "Judy")), "Granddaughter")
    assert_equal(relations(family_b, ("Enid", "Deborah")), "Granddaughter")
    assert_equal(relations(family_b, ("Enid", "Dianne")), "Daughter")
    assert_equal(relations(family_b, ("Enid", "Fern")), "Granddaughter")
    assert_equal(relations(family_b, ("Susan", "Enid")), "Mother")
    assert_equal(relations(family_b, ("Susan", "Deborah")), "Daughter")
    assert_equal(relations(family_b, ("Susan", "Dianne")), "Sister")
    assert_equal(relations(family_b, ("Susan", "Judy")), "Niece")
    assert_equal(relations(family_b, ("Susan", "Fern")), "Niece")
    assert_equal(relations(family_b, ("Fern", "Susan")), "Aunt")
    assert_equal(relations(family_b, ("Fern", "Judy")), "Sister")


def test_day_of_year():
    assert_equal(day_of_year(1, 1, 2000), 1, "Jan 1, 2000")
    assert_equal(day_of_year(15, 2, 2015), 46, "Feb 2, 2015")
    assert_equal(day_of_year(30, 6, 2020), 182, "June 30, 2020", "Did you check for leap year?")


def test_fruit():
    assert_equal(fruit_calculator("Panda has 8 apples and loses 2 apples.  How many apples?"), 6)
    assert_equal(
        fruit_calculator("Panda has 8 apples, 2 bananas and gains 3 bananas.  How many bananas?"),
        5,
    )
    assert_equal(
        fruit_calculator("Panda has 8 apples, 2 bananas and gains 3 bananas.  How many apples?"), 8
    )
    assert_equal(
        fruit_calculator(
            "Jim has 12 bananas. He loses 2 apples.  Then he gains 1 apple.  How many bananas?"
        ),
        12,
    )
    assert_equal(
        fruit_calculator("Jim has 2 bananas and gains 3 bananas.  How many watermelons?"), 0
    )


if __name__ == "__main__":
    test_day_of_year()
    test_monogram()
    test_family_tree()
    test_atm()
    test_fruit()


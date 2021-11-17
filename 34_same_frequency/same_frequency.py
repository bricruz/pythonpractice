def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1list = list(str(num1))
    num2list = list(str(num2))

    num1set = set(num1list)
    num2set = set(num2list)

    num1dict = dict(num1set,0)
    print(num1dict)

    count = 0
    # for num in num1set:
    #     target = num
    #     for numy in num1list:
    #         if target == numy:
    #             count+=1

same_frequency(12312,1231)

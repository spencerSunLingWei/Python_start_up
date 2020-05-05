def seasons(year, month, day):
    """
    (int, int, int) -> [str, int]
    A function that is passed a month and day, determines the season, and then 
    calculates the number of days since the current season begins and returns
    the season and days as a two element list.

    Students may assume that the seasons begin on the 21st day of March, June,
    September and December. Student SHOULD consider leap year. 

    Please refer to the handout for test cases and error conditions.
    """
    y=year
    m=month
    d=day
    lst=[y, m, d]

    if lst[0]>=0:
        if lst[0]%4==0:
            year= "leepyear"
        elif lst[0]%4==1 or lst[0]%4==2 or lst[0]%4==3:
            year= "normalyear"
    
    #decide the seasons
    if lst[1]<1 or lst[1]>12:
        a="invalid month"
    elif lst[1]<=12 and lst[1] >=1 and lst[2]>31 or lst[1]<=12 and lst[1] >=1 and lst[2]<1:
        a="invalid day"
    elif lst[1] == 4 and lst[2]>30 or lst[1] == 6 and lst[2]>30 or lst[1] ==9 and lst[2]>30 or lst[1] ==11 and lst[2]>30:
        a="invalid day"
    elif lst[1]==2:
        if year == "leepyear":
            if lst[2]>29:
                a="invalid day"
            elif lst[2]<=29 and lst[2]>=1:
                a="Winter"
        elif year == "normalyear":
            if lst[2]>28:
                a="invalid day"
            elif lst[2]<=28 and lst[2]>=1:
                a="Winter"
    elif lst[1]<=12 and lst[1] >=1:
        if lst[1] == 1 :
            a="Winter"
        elif lst[1]== 4 or lst[1] ==5:
            a="Spring"
        elif lst[1]== 8 or lst[1] ==7:
            a="Summer"
        elif lst[1]== 11 or lst[1] ==10:
            a="Autumn"
        elif lst[1]== 12 and lst[2] <21 and lst[2]>=1 or lst[1]==9 and lst[2]>=21 and lst[2]<=30:
            a="Autumn"
        elif lst[1]== 3 and lst[2] <21 and lst[2]>=1 or lst[1]== 12 and lst[2] >= 21 and lst[2]<=31:
            a="Winter"
        elif lst[1]== 6 and lst[2] <21 and lst[2]>=1 or lst[1]==3 and lst[2]>=21 and lst[2]<=31:
            a="Spring"
        elif lst[1]== 9 and lst[2] <21 and lst[2]>=1 or lst[1] == 6 and lst[2]>=21 and lst[2]<=30:
            a="Summer"
       
   
    #calculate the date
   
    if a == "invalid day":
        b = -1
    elif a == "invalid month":
        b = -1
    elif a == "Spring":
        if lst[1]==3:
            b=lst[2]-21
        elif lst[1]==4:
            b=31-21+lst[2]
        elif lst[1]==5:
            b=31-21+30+lst[2]
        elif lst[1]==6:
            b=31-21+30+31+lst[2]
    elif a == "Summer":
        if lst[1]==6:
            b=lst[2]-21
        elif lst[1]==7:
            b=30-21+lst[2]
        elif lst[1]==8:
            b=30-21+31+lst[2]
        elif lst[1]==9:
            b=30-21+31+31+lst[2]
    elif a == "Autumn":
        if lst[1]==9:
            b=lst[2]-21
        elif lst[1]==10:
            b=30-21+lst[2]
        elif lst[1]==11:
            b=30-21+31+lst[2]
        elif lst[1]==12:
            b=30-21+31+30+lst[2]
    elif a == "Winter":
        if lst[1]==12:
            b=lst[2]-21
        elif lst[1]==1:
            b=31-21+lst[2]
        elif lst[1]==2:
            b=31-21+31+lst[2]  
        elif lst[1]==3:
            if year=="leapyear":
                b=31-21+31+28+lst[2]
            elif year=="normalyear":
                b=b=31-21+31+29+lst[2]

    return [a,b]
 
         
        
    
    
        
        

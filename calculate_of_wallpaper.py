def calculate(lenght_room,wigth_room,lenght_wallpaper,wight_wallpaper,lenght_raport,room_height):

    """
    >>> calculate(2,2,10,1.06,0,2.75)#doctest:+ELLIPSIS
    2.15...

    >>> calculate(2,2,10,1.06,0,2)#doctest:+ELLIPSIS
    1.58...

    >>> calculate(2,2,10,1.06,0.32,2)#doctest:+ELLIPSIS
    1.82...
    """
    f = 0.1 #  safety factor
    perimetr = (lenght_room + wigth_room) * 2

    wallpaper_stripes = lenght_wallpaper / (lenght_raport + room_height + f )

    number_rolls = (perimetr / wight_wallpaper) / wallpaper_stripes

    return number_rolls

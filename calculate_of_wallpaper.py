
# lenght_room =  длина комнаты
# wiпgth_room =  ширина комнаты
# lenght_wallpaper = длина рулона
# wight_wallpaper = ширина рулона
# lenght_raport = рапорт
# room_height =  высота комнаты


def calculate(lenght_room,wigth_room,lenght_wallpaper,wight_wallpaper,lenght_raport,room_height):

    """
    >>> calculate(2,2,10,1.06,0,2.75)#doctest:+ELLIPSIS
    2.15...

    >>> calculate(2,2,10,1.06,0,2)#doctest:+ELLIPSIS
    1.58...

    >>> calculate(2,2,10,1.06,0.32,2)#doctest:+ELLIPSIS
    1.82...
    """

    perimetr = (lenght_room + wigth_room) * 2

    wallpaper_stripes = lenght_wallpaper / (lenght_raport + room_height + 0.1) #число полос

    number_rolls = (perimetr / wight_wallpaper) / wallpaper_stripes #число руллонов

    return number_rolls

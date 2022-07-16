def convert(day):
    match day % 7:
        case 0:
            day = 'Пн'
        case 1:
            day = 'Вт'
        case 2:
            day = 'Ср'
        case 3:
            day = 'Чт'
        case 4:
            day = 'Пт'
        case 5:
            day = 'Сб'
        case 6:
            day = 'Вс'
    return day
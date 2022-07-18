from aiogram.utils.helper import Helper, HelperMode, ListItem


class MessageStates(Helper):
    mode = HelperMode.snake_case

    PETROVA_STATE = ListItem()
    VOROJKOVA_STATE = ListItem()
    VASILEVA_STATE = ListItem()
    WAITING_STATE = ListItem()
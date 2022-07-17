from aiogram.utils.helper import Helper, HelperMode, ListItem


class MessageStates(Helper):
    mode = HelperMode.snake_case

    WAITING_STATE = ListItem()
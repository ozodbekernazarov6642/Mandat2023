from aiogram import Dispatcher

from loader import dp
from .Admin import Adminfilter


if __name__ == "filters":
    dp.filters_factory.bind(Adminfilter)


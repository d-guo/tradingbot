import datetime
import logging

import azure.functions as func

from ..bot.bot import TradingBot


def main(mytimer: func.TimerRequest) -> None:
    logging.info('executing main function...')

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    TradingBot().invoke()

    logging.info('main function successfully ended')

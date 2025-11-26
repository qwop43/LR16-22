import os

import sentry_sdk
from dotenv import load_dotenv


def init_sentry():
    load_dotenv()
    dsn = os.getenv("SENTRY_DSN")

    if not dsn:
        print("⚠️  Помилка: SENTRY_DSN не знайдено в .env файлі!")
        return

    sentry_sdk.init(
        dsn=dsn,
        traces_sample_rate=1.0,
        include_local_variables=False,  # для Python 3.12+
    )

    print("Sentry initialized with hidden DSN")

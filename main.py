from deta import app
from bot import send_update_to_channel
from db import check_staking_data, beautify
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


@app.lib.cron()
def cron_task(event):
    logging.info("Cron started")
    locked_staking_info = check_staking_data(staking_type='Locked')
    flexible_staking_info = check_staking_data(staking_type='Flexible')
    msg = ''
    if len(locked_staking_info) > 0:
        msg = beautify(asset_set=locked_staking_info, staking_type='Locked')
    if len(flexible_staking_info) > 0:
        msg += beautify(asset_set=flexible_staking_info, staking_type='Flexible')
    if len(locked_staking_info) > 0 or len(flexible_staking_info) > 0:
        send_update_to_channel(msg)

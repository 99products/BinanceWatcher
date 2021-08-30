from deta import Deta
import logging
import client

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

deta = Deta()
assets_db = deta.Base(name="assets")


def check_staking_data(staking_type, ):
    locked_staking_db = deta.Base(name=staking_type+"_staking")
    logging.info('Fetching information from Binance')
    staking_json = client.read_locked_staking() if staking_type == 'Locked' else client.read_flexible_staking()
    key_name = 'products' if staking_type == 'Locked' else 'projects'
    logging.info('Completed fetching from Binance')
    available_asset_set = set()
    for coin in staking_json['data']:
        for product in coin[key_name]:
            existing_asset = locked_staking_db.get(product['asset'])
            if existing_asset is not None and product['sellOut'] != existing_asset['sellOut']:
                data = {
                    "sellOut": product['sellOut'],
                }
                locked_staking_db.put(data, key=product['asset'])
                available_asset_set.add(product['asset'])
            elif existing_asset is None:
                data = {
                    "sellOut": product['sellOut'],
                }
                locked_staking_db.put(data, key=product['asset'])

    return available_asset_set


def beautify(staking_type, asset_set: set):
    msg = 'Assets currently availble in ' + staking_type + ' Staking\n\n'
    if len(asset_set) == 0:
        return msg + "None\n"
    for asset in asset_set:
        msg += "{:<5}".format(asset) + "\n"
    return msg


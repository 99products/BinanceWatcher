# Binance Watcher

To monitor and alert the available staking options in Binance
https://www.binance.com/en/pos

There is locked staking, flexible staking, and the options are available for multiple crypto assets.

Monitor the below urls

**Locked Staking:**
https://www.binance.com/bapi/earn/v1/friendly/defi-pos/groupByAssetAndPartnerNameList?pageSize=15&pageIndex=1&status=ALL

**Flexible Staking:**
https://www.binance.com/bapi/earn/v1/friendly/pos/union?pageSize=15&pageIndex=1&status=ALL

Check for the field
_asset,
annualInterestRate,
sellout_

to monitor

**Deployment**

Deta.sh is used for deployment

**Alerts**

Changes will be alerted through telegram channel

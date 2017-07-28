from src.common.database import Database
from src.models.alerts.alert import Alert

Database.initialize()
old_alerts = Alert.get_alerts_to_update()
for alert in old_alerts:
    alert.update()
    print(alert.check_price_limit_reached())
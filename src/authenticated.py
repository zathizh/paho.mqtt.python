import configparser
import paho.mqtt.publish as publish

try:
    config = configparser.ConfigParser(delimiters=(':'))
    config.optionxform = str
    config.read('config.cfg')
    c_id = config.items(config.sections()[0])[0][0]

    publish.single("house/main-light", "OFF", hostname="127.0.0.1", client_id=c_id)

except Exception as err:
    print(err)
    exit()

#!/usr/bin/python
import json
import ast

json_out = "{u'192.168.1.100': {u'24': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'25': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'26': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'27': {u'gpio_setting': u'DNC', u'active': False, u'type': u'DNC', u'action': u'<script>', u'description': u'DO NOT CONNECT!'}, u'20': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'21': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'22': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'23': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'28': {u'gpio_setting': u'DNC', u'active': False, u'type': u'DNC', u'action': u'<script>', u'description': u'DO NOT CONNECT!'}, u'29': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'40': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'1': {u'gpio_setting': u'3v', u'active': False, u'type': u'3v', u'action': u'<script>', u'description': u'The GPIO outputs continuous 3 volts.'}, u'3': {u'gpio_setting': u'I2c', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'/some/script/to/run', u'description': u'This is a I2C GPIO and always outputs.'}, u'2': {u'gpio_setting': u'5v', u'active': False, u'type': u'5v', u'action': u'<script>', u'description': u'The GPIO outputs continuous 5 volts.'}, u'5': {u'gpio_setting': u'I2c', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a I2C GPIOi and always outputs.'}, u'4': {u'gpio_setting': u'5v', u'active': False, u'type': u'5v', u'action': u'<script>', u'description': u'The GPIO outputs continuous 5 volts.'}, u'7': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'6': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'9': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'8': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'39': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'38': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'11': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'10': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'13': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'12': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'15': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'14': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'17': {u'gpio_setting': u'3v', u'active': False, u'type': u'3v', u'action': u'<script>', u'description': u'The GPIO delivers 3v continuously.'}, u'16': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'19': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'18': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'31': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'30': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'37': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'36': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'35': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'34': {u'gpio_setting': u'Ground', u'active': False, u'type': u'Ground', u'action': u'<script>', u'description': u'The GPIO is for ground.'}, u'33': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}, u'32': {u'gpio_setting': u'PUD_DOWN', u'active': False, u'type': u'<door|window|action|motion_sensor>', u'action': u'', u'description': u'This is a GPIO.'}}}"

#to_print = json.loads(json_out)
#print to_print
test_dict = ast.literal_eval(json_out)
#print test_dict
for key in test_dict:
   #print test_dict[key]["24"]["gpio_setting"]
   for key2 in test_dict[key]:
      #print key2
      print (key2 + " : " + test_dict[key][key2]["gpio_setting"] )


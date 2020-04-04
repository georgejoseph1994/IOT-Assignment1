from sense_hat import SenseHat
import time
import json


class TemperatureMonitor:
    sense = None

    def __init__(self):
        self.sense = SenseHat()

    def monitor_and_display(self):
        # colors
        red = (255, 0, 0)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        
        # Fetching data from config.json file
        temperature_thresholds = self.get_data_from_json()
        
        try:
            while(True):
                temp = self.sense.get_temperature()
                if(temp < temperature_thresholds['cold_max']):
                    color = blue
                elif (temp >= temperature_thresholds['comfortable_min'] and temp <= temperature_thresholds['comfortable_max']):
                    color = green
                else:
                    color = red
                self.sense.show_message(str(round(temp, 2)), text_colour = color)
                time.sleep(10)
        
        # Clearing sense hat display on keyboard interrupt
        finally:
            self.sense.clear()
    
    # Returns the JSON object from config.json 
    def get_data_from_json(self):
        with open('config.json') as json_file:
            try:
                data = json.load(json_file)
            except:
                print("--------------- USER WARNING ---------------")
                print("")
                print("  The JSON in config.json file is invalid.")    
                print("")
                print("--------------------------------------------")
                exit()
            return data


temperature_monitor = TemperatureMonitor()
temperature_monitor.monitor_and_display()

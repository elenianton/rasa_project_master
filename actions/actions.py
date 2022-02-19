from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from url import scraping_restaurants


class ValidateRestaurantForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_restaurant_form"

    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines."""

        return [
            "greek",
            "chinese",
            "french/international",
            "indian",
            "italian",
            "mexican",
            "mediterranean" 
        ]
        
    @staticmethod
    def location_db() -> List[Text]:
        """Database of supported locations."""

        return [
            "East Attica",
            "West Attica",
            "Central Attica",
            "North Attica",
            "South Attica"
        ]


    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"cuisine": value}
        
        else:
            dispatcher.utter_message(response="utter_wrong_cuisine")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cuisine": None}
        

    def validate_location(
        self,
        loc: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate location value."""

        if loc in self.location_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"location": loc}

        else:
            dispatcher.utter_message(response="utter_wrong_location")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"location": None}
 

    def validate_outdoor_seating(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate outdoor_seating value."""

        if isinstance(value, str):
            if "out" in value:
                # convert "out..." to True
                return {"outdoor_seating": True}
            elif "in" in value:
                # convert "in..." to False
                return {"outdoor_seating": False}
            else:
                dispatcher.utter_message(response="utter_wrong_outdoor_seating")
                # validation failed, set slot to None
                return {"outdoor_seating": None}

        else:
            # affirm/deny was picked up as True/False by the from_intent mapping
            return {"outdoor_seating": value}


class Actionsgetrestaurants(Action):
    """Example of a form validation action."""
    def name(self):
        return 'action_get_restaurants'
        
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            cuisine= tracker.get_slot("cuisine")
            location=tracker.get_slot("location")

            if cuisine == 'greek' and location == 'East Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.anatolikiattiki/elliniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'greek' and location == 'West Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.dytikaproastia+attiki.dytikiattiki/elliniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'greek' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/elliniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'greek' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/elliniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'greek' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/elliniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'chinese' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/kineziki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'chinese' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/kineziki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'chinese' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/kineziki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international' and location == 'East Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.anatolikiattiki+attiki.athina/diethnis"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international' and location == 'West Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.dytikaproastia+attiki.dytikiattiki/diethnis"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/diethnis"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/diethnis"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/diethnis"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'indian' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.athina/indiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'indian' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/indiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'indian' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.athina+attiki.kentrikanotiaproastia/indiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'italian' and location == 'East Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.anatolikiattiki/italiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'italian' and location == 'West Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.dytikaproastia+attiki.dytikiattiki/italiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'italian' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/italiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'italian' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/italiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'italian' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/italiki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mexican' and location == 'West Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.dytikaproastia+attiki.dytikiattiki/mexikaniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mexican' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.athina+attiki.kentrikanotiaproastia/mexikaniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mexican' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/mexikaniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mexican' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.athina+attiki.kentrikanotiaproastia/mexikaniki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean' and location == 'East Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.anatolikiattiki/mesogeiaki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean' and location == 'West Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.dytikaproastia+attiki.dytikiattiki+attiki.peiraiasperichora/mesogeiaki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean' and location == 'Central Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.athina/mesogeiaki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean' and location == 'North Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.voreiaproastia+attiki.voreiodytikaproastia/mesogeiaki"
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean' and location == 'South Attica':
                url_res= "https://www.e-table.gr/en/restaurants/attiki.kentrikanotiaproastia/mesogeiaki"          
                restaurant, loc= scraping_restaurants(url_res)
                response= """What about {0} at {1}?""".format(restaurant, loc)
                dispatcher.utter_message(response) 
            else:
                response_not= """I can not find any restaurant based on your preferences"""
                dispatcher.utter_message(response_not)
            
            
            
class ActionGetInformation(Action):
    """Example of a form validation action."""
    def name(self):
        return 'action_get_information'
        
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            cuisine= tracker.get_slot("cuisine")
            infos=[]
            with open ("cuisines.csv", encoding='utf-8')as file:
                file= file.readlines()
                for line in file:
                    infos.append([line])
            Italian=' '.join(infos[1])
            French =' '.join(infos[2])
            Greek = ' '.join(infos[3])
            Indian= ' '.join(infos[4])
            Mexican=' '.join(infos[5])
            Chinese= ' '.join(infos[6])

            if cuisine == 'greek':
                response= """Im gonna give you some really interesting information about {}""".format(Greek)
                dispatcher.utter_message(response)
            elif cuisine == 'chinese':
                response= """Im gonna give you some really interesting information about {}""".format(Chinese)
                dispatcher.utter_message(response)
            elif cuisine == 'french/international':
                response= """Im gonna give you some really interesting information about {}""".format(French)
                dispatcher.utter_message(response)
            elif cuisine == 'italian':
                response= """Im gonna give you some really interesting information about {}""".format(Italian)
                dispatcher.utter_message(response)
            elif cuisine == 'indian':
                response= """Im gonna give you some really interesting information about {}""".format(Indian)
                dispatcher.utter_message(response)
            elif cuisine == 'mexican':
                response= """Im gonna give you some really interesting information about {}""".format(Mexican)
                dispatcher.utter_message(response)
            elif cuisine == 'mediterranean':
                response= """Im sorry but I have no idea about this type of cuisine. The only thing I know is that\n
                        greek cuisine is a type of mediterranean cuisine. So, let me give you some information about\n 
                        greek food. {}""".format(Greek)
                dispatcher.utter_message(response)

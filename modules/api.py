import asyncio
import websockets 
import json
from modules.config import config
from modules.classes import Match

class WebsocketHandler:
    """
    A PubSub-based class that manages websocket connections
    """
    
    def __init__(self) -> None:
        # Updates hosts a list of all server events to be notified to the relevant, key=eventNumber
        self.updates = dict()

        # Websockets hosts connected clients as its key and value involves 2 lists of subs and events
        self.websockets = dict()

        # EventNumber holds the number of the latest event to ensure each has a unique ID
        self.eventNumber = 0
    
    def prep_data(self, type: str, data) -> str:
        """Takes type and data and transforms it first into
        a dict, then a stringifyed json for sending over the websocket"""

        return json.dumps({"type" : type, "data" : data})
    
    def add_update(self, type: str, data = None) -> str:
        """Subscribed websockets to be notified of an event by adding an entry for each
        websocket's dictionary entry"""
        
        # Update the data based on the type
        match type:
            case "0":
                data = self.function()
            case "1":
                data = self.function()
            case "2":
                data = self.function()
            case "3":
                data = self.function()
            case _ :
                data = None
    
        # If data is present, add an update
        if data:

            # Add the update into the updates dict
            self.updates[self.eventNumber]["data"] = data
            self.updates[self.eventNumber]["type"] = type
            # Listeners is the number of websockets that are subscribed to this event type
            self.updates[self.eventNumber]["listeners"] = 0 
            
            # Add event ID to the subbed websockets
            for websocket in self.websockets:
                if type in self.websockets[websocket]["subscriptions"]:
                    
                    self.websockets[websocket]["updates"].append(self.eventNumber)
    
            self.eventNumber += 1

    def subscribe(self, data, websocket) -> str:
        """Message from websocket requests a subscription,
        so add it to the appropriate dict entry. Subs can be sent
        in list format, requiring only 1 message from websocket to subscribe
        to more than one service"""
        
        for sub in data:
            if sub not in self.websockets[websocket]["subscriptions"]:
                self.websockets[websocket]["subscriptions"].append(sub)
        return  f"subscribed to {data}"
 
    def publish(self, websocket) -> list:
        """Returns the full list of updates for a specific websocket and removes them"""
        
        updates_list = []
        for eventID in self.websockets[websocket]["updates"]:
            updates_list.append(self.updates[eventID])
            self.remove_listener(websocket, eventID)
               

        return updates_list

    def remove_listener(self, websocket, eventID) -> None:
        """Reduces the number of listeners for the event by 1"""

        self.updates[eventID]["listeners"] -= 1
        if self.updates[eventID]["listeners"] == 0:
            del self.updates[eventID]

    def read_message(self, message, websocket) -> str:
        """Message received by the websocket, return appropriate data"""
        
        message = json.loads(message)
        match message["type"]:
            case "sub":
                rtn = self.subscribe(message["subId"], websocket)
                return self.prep_data("notification", rtn)
            case "getMatch":
                return self.get_match(message["matchId"])
            case _:
                return self.prep_data("Unknown", {"message" : f"Unknown type '{type}'"})
    
    def add_websocket(self, websocket) -> None:
        """Generates a dict entry for the websocket"""

        self.websockets[websocket] = {
            "subscriptions" : list(),
            "updates" : list()
        }
    
    def get_websockets(self) -> dict:
        """Returns the websockets dict"""

        return self.websockets
    
    def remove_websocket(self, websocket) -> None:
        """Remove a websocket and its subscriptions"""
        
        del self.websockets[websocket]
    
    def request_data(self, type) -> str:
        """Message from websocket wants data, return as such"""

        data = None
        match type:
            case "1":
                data = self.function()
            case _ :
                data = None
            
        if data == None:
            return self.prep_data("Unknown", {"message" : f"Unknown GET type '{type}'"})
        else:
            return self.prep_data(type, data)
    
    def get_match(self, matchId) -> str:
        """ Returns a string formatted match """
        return Match(matchId)
    
    
def api_server() -> None:
    """
    Hosts a local API server using websockets
    """   
        
    async def handler(websocket):
        """Handles requests in and out of the websocket"""
        websocket_handler.add_websocket(websocket)
        await asyncio.gather(
            consumer_handler(websocket),
            producer_handler(websocket)
        )
                 
    async def producer_handler(websocket):                
        """Pushes out updates/events to websockets using the
        WebsocketHandler class. Checks the list every second"""
        
        while True:
            await asyncio.sleep(1)
            updates = websocket_handler.publish(websocket)
            while updates:
                message = updates.pop()
                if message:
                    await asyncio.create_task(send(websocket, message))
    
    async def consumer_handler(websocket):
        """Responds to websocket messages"""
        
        try:
            # Begin loop to prevent websocket termination after just 1 message
            while True:
                
                message = await websocket.recv()
                 # All different cases are handled by the WebsocketHandler class
                await websocket.send(websocket_handler.read_message(message, websocket))

        except Exception as e:
            pass
        finally:
            websocket_handler.remove_websocket(websocket)
    
    async def send(websocket, message):
        """Sends a message to the websocket"""
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            pass

    async def main():
        async with websockets.serve(handler, config["api"]["host"], config["api"]["port"]):
            await asyncio.Future()  # run forever

    # Show that the api sucessfully started
    host = config["api"]["host"]
    port = config["api"]["port"]
    print (f"started websocket api server on host {host}:{port}")
    # Start the websocket
    asyncio.run(main())
    
websocket_handler = WebsocketHandler()
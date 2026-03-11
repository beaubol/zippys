from fastapi import FastAPI, WebSocket
import asyncio
import json

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Simulated GPS pings moving down the road in Siesta Key
    route = [
        [27.2750, -82.5510],
        [27.2740, -82.5505],
        [27.2730, -82.5500],
        [27.2720, -82.5495],
        [27.2710, -82.5485],
        [27.2690, -82.5475],
        [27.2670, -82.5463] # Arrives at destination
    ]
    
    try:
        # Loop through the coordinates and send one every 2 seconds
        for coords in route:
            await asyncio.sleep(2) 
            data = {"lat": coords[0], "lng": coords[1]}
            await websocket.send_text(json.dumps(data))
            
    except Exception as e:
        print("Radio silent. Connection closed.")
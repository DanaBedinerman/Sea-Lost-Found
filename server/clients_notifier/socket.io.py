from aiohttp import web
import socketio
import json

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.on('location')
async def get_location(sid, message):
    ######function call
    print("Socket ID: " , sid)
    print(message)

def send_object_location(id, location):
    sio.emit('objcet_location', { "id":id , "location": location })

@sio.on('history')
async def get_history(sid, message):
    history=""
    #####function call
    sio.emit('objcet_history', { "id":message["id"] , "history": history  })

if __name__ == '__main__':
    web.run_app(app)
import json
import filetype
from channels.generic.websocket import AsyncWebsocketConsumer

class FileUploadConsumer(AsyncWebsocketConsumer):
    MAX_FILE_SIZE_BYTES = 4 * 1024 * 1024
    
    async def connect(self):
        await self.accept()
        
        if not self.scope["user"].is_active:
            await self.send(json.dumps({
                "type": "websocket.close",
                "code": 401,
                "reason": "User not authenticated",
            }))
            
            await self.close()
        return


    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            file_size = len(bytes_data)
            if file_size > self.MAX_FILE_SIZE_BYTES:
                await self.send(text_data=json.dumps({'error': 'File size exceeds maximum limit.'}))
                return

            file_extension = self.get_file_extension(bytes_data)
            await self.send(text_data=file_extension)

    async def disconnect(self, close_code):
        self.close()

    def get_file_extension(self, bytes_data):
        try:
            file_type = filetype.guess(bytes_data)
            return file_type.extension if file_type else 'Failed to identify'
        except Exception as e:
            self.logger.error("Error determining file extension: %s", e)
            return 'Failed to identify'
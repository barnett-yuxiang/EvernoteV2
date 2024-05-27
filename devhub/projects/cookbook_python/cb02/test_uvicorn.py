from fastapi import FastAPI
from datetime import datetime
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/time")
async def get_time():
    # 模拟异步操作，如从数据库或外部API获取数据
    await asyncio.sleep(1)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

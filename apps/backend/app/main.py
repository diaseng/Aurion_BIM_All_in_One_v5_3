from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root(): return {'msg':'Aurion BIM API v5.3'}
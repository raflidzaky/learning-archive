import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# Define input structure with Pydantic
class Item(BaseModel):
    X: int

# Make the model asynchronous (can be handled concurrently)
async def load_model():
    # Load the model asynchronously to avoid blocking other requests (such as POST request for feature or prediction)
     return await asyncio.to_thread(pickle.load, open('trained_model.pkl', 'rb'))

# The ML loading task currently is asynchronous
# It is initialized as None
# Initially, I want to make it active whenever user make a requests, but that's not efficient
ml_model = None

# On event might be prefered because the model is requested when the server is started
@app.on_event("startup")
async def startup_event():
    global ml_model
    # Load the model during the app startup
    ml_model = await load_model()
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Pass information of JSON (feature to API)
# Send POST request
# Classic Google won't accept this, so make script on JS
@app.post("/feature")
async def scoring_endpoint(item:Item):
    
    return item

# Konsepnya, kita POST the feature to API
# Once it is done (200 OK) - Then 

@app.post("/predict")
async def scores(item:Item):
    # Logic: 
    # 1. The model need to be feed
    # 2. We "assert" the X-feature as integer (from class Item)
    # 3. Thus, the POST body message need as an integer
    # 4. But, a model couldnt process a single integer
    # 5. The solution: Make sure the POST body message still integer
    # while processing to a 2D array

    # Convert the scalar X into a 2D array (1 sample, 1 feature)
    X_2d = np.array([[item.X]])
    
    # Make a prediction using the 2D array
    yhat = await asyncio.to_thread(ml_model.predict, X_2d)
    
    return {"prediction": yhat[0]}

# Modify the GET route to accept query parameters
@app.get("/predict") 
async def scores(X: int): # Query params
    # The difference between POST and GET
    # POST: Return response from body information, extracted from Pydantic
    # GET: Return response from query params, passed directly from the function params
    # In URL, you can see this http://local/predict?X='some_info'
    # Convert the scalar X into a 2D array (1 sample, 1 feature)
    X_2d = np.array([[X]])
    
    # Make a prediction using the 2D array
    yhat = await asyncio.to_thread(ml_model.predict, X_2d)
    
    return {"prediction": yhat[0]}

# Once it is done, the POST response a message
# So, we need to fetch those message using .JS script

# === SIMPLE POST LEARNING-BY-DOING INSIGHTS
# API POST is just like a communication
# 1. Send an active request (include Body information)
# 2. Script how it will respond
# 3. It responses. 
# 4. Fetch the responses

# API GET is also does the same way
# The difference is, GET supposed (best practice) to retrieve static data (not altering the backend)
# While API POST is to send data --> process it --> send back to the client (fetching)

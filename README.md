# Paddy-Disease-Classification
This was my 4th year project at the university which I did from the period of 8 months from 2023 September to 2024 April and the dataset I got from kaggle.

## Setup for Anaconda python package manager:

1. Install Anaconda ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install Python packages

```
pip3 install -r training/requirements.txt
pip3 install -r backend/requirements.txt
```

## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/competitions/paddy-disease-classification-2/data).
2. Run Jupyter Notebook in Visual Studio Code.
3. Open `training/notebook.ipynb` in Jupyter Notebook.
4. In cell #2, update the path to dataset.
5. Run all the Cells one by one.
6. Model generated will be saved with the version number in the `models` folder.

## Running the API

### Using FastAPI

1. Get inside `backend` folder
2. Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8080`

## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Create ReactJS project with the project name "frontend" 
4. Install dependencies
5. Change API url in `App.js`.
6. Change the css in `App.css`.

## Running the Frontend
1. Open frontend in Integrated Terminal
2. Run the frontend

```bash
npm run start
```

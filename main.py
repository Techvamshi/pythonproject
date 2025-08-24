from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Add Two Numbers</title>
        </head>
        <body>
            <h2>Enter Two Numbers</h2>
            <form action="/add" method="post">
                <input type="number" name="num1" placeholder="Enter first number" required>
                <input type="number" name="num2" placeholder="Enter second number" required>
                <button type="submit">Add</button>
            </form>
        </body>
    </html>
    """


@app.post("/add", response_class=HTMLResponse)
def add_numbers(num1: int = Form(...), num2: int = Form(...)):
    result = num1 + num2
    return f"""
    <html>
        <head>
            <title>Result</title>
        </head>
        <body>
            <h2>Results</h2>
            <p>Number 1: {num1}</p>
            <p>Number 2: {num2}</p>
            <p>Sum: {result}</p>
            <a href="/">Go Back</a>
        </body>
    </html>
    """



@app.get('/PYTHON',response_class=HTMLResponse)
def vamshi():
    import pandas as pd

    read_file=pd.read_excel('//Users//amithkarthikmalasani//Desktop//Markss.xlsx')
    df=pd.DataFrame(read_file)

    print(df.head())


    df['Total']=df['Math']+df['Science']+df['English']+df['History']+df['Computer']
    df['Percentage']=(df['Total']/500)*100


    sorted=df.sort_values(by='Percentage',ascending=False)

   


    

    return f"""
    <html>
        <head>
            <title>Pandas Example</title>
        </head>
        <body>
            <h1>Below are the Top 5 students marks:</h1>
            {sorted.head(5).to_html(index=False)}
        </body>
    </html>
    """
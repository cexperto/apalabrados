
# Apalabrados

This application classifies the user input, if the data is a number, it saves the number in the database and counts the accumulated number, if it is a text, it saves the first and last character, but if the text contains special characters, it saves the character and discards the text.

App for platzi master program week 2 
## Authors

- [@cexperto](https://github.com/cexperto/apalabrados)


  
## API Reference


#### Get all items


```http
  GET /numbers
```

```http
  GET /texts
```

```http
  GET /characters
```



  
## Deployment

To deploy this project run

https://apalabrados-api.herokuapp.com/




  
## Installation 

Install python 3+

clone the repository : https://github.com/cexperto/apalabrados
 run 
    pip install -r requirements.txt
  run
    py apalabrados.py
    
## Tech Stack

**Client:** python, request

**Server:** psycopg2, flask, jsonify, response, sqlalchemy, postgresql

  

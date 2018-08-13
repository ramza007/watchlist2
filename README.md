# WatchList ( ver. 2.0 )

### By **Ramza Reseni**, 
#### Published date **13/08/18**
 ---


## Description
A web application that allows the user to search a specific movie, see it details and ratings and also review it

### Setup/Installation Requirements

#### Prerequisites
* Python 3.6.6 (and higher)
* Virtual environment
* PostgreSQL


### Installation Process
* open my [GitHub](https://github.com/ramza007)
* find my repo *WatchList2*
* run `git clone <REPO-URL>` in your terminal
* write `cd WatchList2`
* create a virtual environment with `python3 -m venv virtual`
* enter virtual environment `. virtual/bin/activate`
* run `pip install -r requirements.txt`
* create a Postgres Database
* create a start.sh file in the parent directory and add the following
    * go to [themoviedb](https://www.themoviedb.org) website and create your API key that will be used in the application
    * place the api key in `export MOVIE_API_KEY='your-api-key'
    * create a secret key in `export SECRET_KEY='your-secret-key'
    * add the command to run the app `python3 manage.py server`
* run `./start.sh` or `. start.sh` to run the application



## Technologies Used
- Python ( **ver 3.7** )
- Flask microframework ( **ver 1.0.2** )
- PostgreSQL
- Heroku

### Acknowledgements

- Stack Overflow
- Google



#### License under [***MIT***](https://github.com/ramza007/watchlist2/blob/master/LICENSE)

Copyright (C) 2018 ~ Reseni
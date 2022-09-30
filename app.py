# Set up Flask Weather App

# Import dependencies
import datetime as dt

from zmq import Message
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up database engine for Flask app

# Create function allows access to SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# Set class variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to SQLite database
session = Session(engine)

# Create Flask app, all routes go after this code
app = Flask(__name__)
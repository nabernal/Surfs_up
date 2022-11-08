# import the Flask dependency
import datetime as dt
import numpy as np
import pandas as pd


# SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Flask dependencies
from flask import Flask, jsonify

# set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes.
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session linkfrom Python to our database
session = Session(engine)


# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# "/" denotes that we want to put our data at the root(homepage)  of our routes
# <br/> used for linebreak
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes: <br/>
    /api/v1.0/precipitation <br/>
    /api/v1.0/stations <br/>
    /api/v1.0/tobs <br/>
    /api/v1.0/temp/start/end
    ''')

# Build the precipitation route
@app.route("/api/v1.0/precipitation")
# Create new function called precipitation()
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Build the station route
@app.route("/api/v1.0/stations")
# Create new function called stations()
def stations():
    # create a query that will allow us to get all of the stations
    results = session.query(Station.station).all()
    # unravel our results into a one-dimensional array and convert the results to a list,
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Build the station route
@app.route("/api/v1.0/tobs")
# Create new function called temp_monthly()
def temp_monthly():
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year. 
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # unravel the results into a one-dimensional array and convert that array into a list.  
    temps = list(np.ravel(results))
    # jsonify our temps list
    return jsonify(temps=temps)

# Build the station route for start date and end date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Unravel results into a 1D array and convert to a list
        temps = list(np.ravel(results))
        return jsonify(temps)

    # calculate TMIN, TAVG, TMAX with start and stop
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
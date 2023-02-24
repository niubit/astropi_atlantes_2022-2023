##### IMPORTING LIBRARIES - BEGIN #####
from sense_hat import SenseHat
from picamera import PiCamera
from logzero import logger, logfile
from orbit import ISS
from skyfield.api import load
import csv
from datetime import datetime, timedelta
from time import sleep
from gpiozero import CPUTemperature
from pathlib import Path
import os
##### IMPORTING LIBRARIES - END #####


##### DATA STRUCTURES - BEGIN #####
# Consts
STEP_LAPSE = 10             # seconds
EXPERIMENT_DURATION = 178   # minutes
IMAGES_DIR = "images"
DATA_DIR = "data"

# Vars
image_counter = 1
start_time = datetime.now()
current_time = start_time
running = True
##### DATA STRUCTURES - END #####


##### FUNCTIONS - BEGIN #####
def label_result(file):
    """ Write header at the begining of `file` with `csv` library """
    header = ("datetime", "picture_file", "latitude", "longitude", "elevation", "temp_cpu", "temp_h",
              "temp_p", "humidity", "pressure", "pitch", "roll", "yaw", "mag_x", "mag_y", "mag_z",
              "accel_x", "accel_y", "accel_z", "gyro_x", "gyro_y", "gyro_z")
    with open(file, 'w', buffering=1) as f:
        csv.writer(f).writerow(header)
        f.flush()
        os.fsync(f)

def write_result(file, data):
    """ Append data at the end of `file` with `csv` library """
    with open(file, 'a', buffering=1) as f:
        csv.writer(f).writerow(data)
        f.flush()
        os.fsync(f)

def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = "%.0f/1,%.0f/1,%.0f/10" % (degrees, minutes, seconds*10)
    return sign < 0, exif_angle

def set_exif(picam, lat, lon):
    """ Set latitude, longitude to EXIF data in PiCam """
    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(lat)
    west, exif_longitude = convert(lon)
    
    # Set the EXIF tags specifying the current location
    picam.exif_tags['GPS.GPSLatitude'] = exif_latitude
    picam.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    picam.exif_tags['GPS.GPSLongitude'] = exif_longitude
    picam.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"
##### FUNCTIONS - END #####


##### PROGRAM SETUP - BEGIN #####
# Set up Sense Hat
sensehat = SenseHat()

# Switch off screen just in case
sensehat.clear()

# Set up camera
# Get possible resolutions from https://picamera.readthedocs.io/en/latest/fov.html#sensor-modes
cam = PiCamera(sensor_mode=2)
#cam.resolution = (2592, 1944)  # Full sensor area on V1
cam.resolution = (3280, 2464)  # Full sensor area on V2

# Get working directory
base_folder = Path(__file__).parent.resolve()
data_dir = base_folder/DATA_DIR
images_dir = base_folder/IMAGES_DIR

# Create directories
os.mkdir(data_dir)
os.mkdir(images_dir)

# Set up logging
logfile(data_dir/"atlantes.log")

# Preload ephemeris file
# https://rhodesmill.org/skyfield/planets.html
# https://rhodesmill.org/skyfield/files.html
eph = load("de421.bsp")

# Set up results file
results_file = data_dir/"atlantes.csv"
label_result(results_file)
##### PROGRAM SETUP - END #####


##### PROGRAM LOOP - BEGIN #####
while running:
    try:
        step_time = current_time

        # Read sensor data
        temp_cpu = round(CPUTemperature().temperature, 2)
        temp_h = round(sensehat.get_temperature_from_humidity(), 2)
        temp_p = round(sensehat.get_temperature_from_pressure(), 2)
        humidity = round(sensehat.get_humidity(), 2)
        pressure = round(sensehat.get_pressure(), 2)
        pitch = round(sensehat.get_orientation_degrees()["pitch"], 2)
        roll = round(sensehat.get_orientation_degrees()["roll"], 2)
        yaw = round(sensehat.get_orientation_degrees()["yaw"], 2)
        mag_x = round(sensehat.get_compass_raw()["x"], 4)
        mag_y = round(sensehat.get_compass_raw()["y"], 4)
        mag_z = round(sensehat.get_compass_raw()["z"], 4)
        accel_x = round(sensehat.get_accelerometer_raw()["x"], 6)
        accel_y = round(sensehat.get_accelerometer_raw()["y"], 6)
        accel_z = round(sensehat.get_accelerometer_raw()["z"], 6)
        gyro_x = round(sensehat.get_gyroscope_raw()["x"], 6)
        gyro_y = round(sensehat.get_gyroscope_raw()["y"], 6)
        gyro_z = round(sensehat.get_gyroscope_raw()["z"], 6)

        # Calculate ISS position
        location = ISS.coordinates()
        latitude = location.latitude
        longitude = location.longitude
        elevation = location.elevation

        # Check sunlight to make or not the picture
        t = load.timescale().now()
        if ISS.at(t).is_sunlit(eph):
            # Set location in EXIF
            set_exif(cam, latitude, longitude)

            # Take picture
            image_name = "atlantes_" + str(image_counter).zfill(3) + ".jpg"
            cam.capture(str(images_dir/image_name))
        else:
            image_name = "BLACKOUT"

        # Log iteration info to logging file
        logger.info(f"{step_time.strftime('%Y-%m-%d %H:%M:%S')} Iteration #{image_counter}")

        # Write data to results file
        line = (step_time, image_name, latitude.degrees, longitude.degrees, elevation.m,
                temp_cpu, temp_h, temp_p, humidity, pressure, pitch, roll, yaw,
                mag_x, mag_y, mag_z, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z)
        write_result(results_file, line)

    except Exception as e:
        # Log error to logging file
        logger.error(f"{e.__class__.__name__}: {e}")
        
    finally:
        # Check end of program condition
        running = step_time < start_time + timedelta(minutes=EXPERIMENT_DURATION)

        # Check end of iteration condition (wait STEP_LAPSE seconds to next iteration)
        waiting_next_step = running
        while waiting_next_step:
            current_time = datetime.now()
            waiting_next_step = current_time < step_time + timedelta(seconds=STEP_LAPSE)

        # Increase counter
        image_counter += 1
##### PROGRAM LOOP - END #####

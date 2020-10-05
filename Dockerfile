FROM python:3.9.0rc2-buster

# Make a directoy for application
WORKDIR /facedetection

# install dependencies
COPY requirements.txt ./
COPY projectManager/studentsAttendence/TrainImages ./
COPY projectManager/studentsAttendence/Attendence.csv ./
RUN pip install -r requirements.txt
# Copy source code
COPY detection.py ./
# Run the application
CMD ["python","detection.py"]

from app import app, db
from flask import render_template
from models import Survey, Task, Assignment, Response

@app.route('/')
def index():
    (headers, fields, data) = getSummary()
    return render_template("survey_summary.html", headers=headers, fields=fields, data=data)

def getSummary():
    fields = ["Filename", "A", "B", "C", "D", "E"] # column names for output
    headers = dict() # custom header names for given fieldname (no difference here)
    for field in fields:
        headers[field] = field

    # build data structures
    data = []
    rowMap = dict()    
    fileNames = ["file1.mp3", "file2.mp3", "file3.mp3", "file4.mp3"]    

    for fileName in fileNames:
        row = dict()
        row["Filename"] = fileName
        row["A"] = 0
        row["B"] = 0
        row["C"] = 0
        row["D"] = 0
        row["E"] = 0
        data.append(row)
        rowMap[fileName] = row

    # query
    query = db.session.query(Survey, Task, Assignment, Response) \
                      .join(Task, Survey.id==Task.survey_id) \
                      .join(Assignment, Task.id==Assignment.task_id) \
                      .join(Response, Assignment.id==Response.assignment_id) \
                      .filter(Survey.id == 1)

    results = query.all()

    # summarise counts
    for (_, _, _, response) in results:
        rowMap[response.response_item][response.response_value] = rowMap[response.response_item][response.response_value] + 1

    return (headers, fields, data)


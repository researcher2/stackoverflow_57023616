
from app import app, db
from flask import render_template
from models import Survey, Task, Assignment, Response

@app.route('/')
def index():
    (headers, fields, data) = getSummary()
    return render_template("survey_summary.html", headers=headers, fields=fields, data=data)

def getSummary():
    fields = ["Filename", "A", "B", "C", "D", "E"]
    headers = fields

    data = []

    query = db.session.query(Survey, Task, Assignment, Response) \
                      .join(Task, Survey.id==Task.survey_id) \
                      .join(Assignment, Task.id==Assignment.task_id) \
                      .join(Response, Assignment.id==Response.assignment_id) \
                      .filter(Survey.id == 1)

    results = query.all()
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

    # Easy Pointer to your data rows
    rowMap = dict()
    for i in range(0, len(fileNames)):
        fileName = fileNames[i]
        rowMap[fileName] = data[i]

    for (_, _, _, response) in results:
        rowMap[response.response_item][response.response_value] = rowMap[response.response_item][response.response_value] + 1

    return (headers, fields, data)


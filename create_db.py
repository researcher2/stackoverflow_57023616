from app import db
from models import Survey, Task, Assignment, Response

import os

try:
    os.remove("sample.db")
except:
    pass

db.create_all()

survey = Survey()
task = Task()
assignment = Assignment()

fileNames = ["file1.mp3", "file2.mp3", "file3.mp3", "file4.mp3"]
answers = ["A","B","C","D","E"]

counts = []
counts.append([10, 8, 5, 0, 1])
counts.append([1, 26, 2, 3, 7])
counts.append([4, 0, 0, 3, 57])
counts.append([1, 6, 1, 5, 28])

index = 0

for i in range(0, len(fileNames)):
    answerCounts = counts[i]
    for j in range(0, len(answerCounts)):
        for k in range(0, answerCounts[j]):
            response = Response()
            response.response_item = fileNames[i]
            response.response_value = answers[j]
            assignment.responses.append(response)

task.assignments.append(assignment)
survey.tasks.append(task)
db.session.add(survey)
db.session.commit()
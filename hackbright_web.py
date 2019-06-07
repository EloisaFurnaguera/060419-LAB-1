"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/add",  methods=['POST'])
def get_add_form():

    student_first = request.form.get("first_name")
    student_last = request.form.get("last_name")
    student_githup = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    print(student_first)
    return render_template("new_student.html", name=student_first, last=student_last, pass_github=student_last)






if __name__ == "__main__":

    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

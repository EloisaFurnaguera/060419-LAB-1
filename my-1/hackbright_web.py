"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/")
def home_page():
    answer1 = request.args.get("mama")
    if answer1 == "yes":
      return render_template("student_add_form.html")
    elif answer1 == "no":
      return render_template("student_search.html")
    return render_template("home_page.html")



@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    # student_id, first, last, github = hackbright.get_student_by_github(github)
    #we could also write:
    # row = hackbright.get_student_by_github(github)
    # first = row[0]
    # last = row[1]
    # github = row[2]

    student_id, first, last, github = hackbright.get_student_by_github(github)
    project_and_grade_list = hackbright.get_grades_by_github(github)


    html = render_template("student_info.html",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                           student_id= student_id,
                           first=first,
                           last=last,
                           github=github,
                           projects_list=project_and_grade_list)
                       
                
    return html


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student_add_form")
def add_student_form():
    """Show form for adding a student."""


    return render_template("student_add_form.html")
    

@app.route("/student_add", methods=["POST"])
def add_student():
    """adding a student."""
    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
    

    hackbright.make_new_student(first, last, github)

    return render_template("student_bueno.html",
                            first=first,
                            last=last,
                            github=github)

















if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

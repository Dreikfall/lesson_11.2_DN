from flask import Flask, render_template
from candidates import Candidates

app = Flask(__name__)


@app.route("/")
def func_list_candidates():
    list_candidates = Candidates().load_candidates_from_json()
    return render_template("list.html", list_candidates=list_candidates)


@app.route("/candidate/<int:id>")
def func_id_candidate(id):
    id_candidate = Candidates().get_candidate(id)
    return render_template("single.html", id_candidate=id_candidate)


@app.route("/search/<candidate_name>")
def func_search(candidate_name):
    tuple_candidates = Candidates().get_candidates_by_name(candidate_name)
    return render_template("search.html", tuple_candidates=tuple_candidates)


@app.route("/skill/<skill_name>")
def func_skill(skill_name):
    tuple_candidates = Candidates().get_candidates_by_skill(skill_name)
    return render_template("skill.html", tuple_candidates=tuple_candidates, skill_name=skill_name)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from utils import format_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route('/')
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidates/<int:uid>')
def page_candidates(uid):
    """Данные по кандидату"""
    candidate: dict = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Данные по навыку"""
    skill_lower = skill.lower()
    candidate: list[dict] = get_by_skill(skill_lower)
    result = format_candidates(candidate)
    return result


app.run()

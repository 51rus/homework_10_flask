import json


def load_candidates() -> list[dict]:
    """Загружает данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = '<pre>'

    for candidate in candidates:
        result += f""" 
                {candidate["name"]}\n
                {candidate["position"]}\n
                {candidate["skills"]}\n
            """
    result += '</pre>'
    return result


def get_all() -> list[dict]:
    """Показывает всех кандидатов"""
    return load_candidates()


def get_by_pk(uid: int) -> dict | None:
    """Возвращает кандидата по pk"""
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None


def get_by_skill(skill_name: str) -> list[dict]:
    """Возвращает кандидата по навыку"""
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

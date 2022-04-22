import json


class Candidates:

    def load_candidates_from_json(self):
        """Возвращается список кандидатов"""

        with open("candidates.json", "r", encoding="utf-8") as f:
            list_candidates = json.load(f)
            self.candidates = (candidate for candidate in list_candidates)  # создаем выражение-генератор
        return self.candidates                                              # говорят быстрее списка

    def get_candidate(self, candidate_id):
        """Возвращает словарь кандидата по ID"""

        list_candidates = self.load_candidates_from_json()
        for l in list_candidates:
            if l["id"] == candidate_id:
                return l

    def get_candidates_by_name(self, candidate_name):
        """Возвращает кортеж словарей в ключах "name" которых есть
        хотя бы частичные совпадения с аргументом"""

        tuple_candidates = ()
        list_candidates = self.load_candidates_from_json()
        for l in list_candidates:
            if candidate_name.lower() in l["name"].lower():
                tuple_candidates += (l,)
        return tuple_candidates

    def get_candidates_by_skill(self, skill_name):
        """Возвращает кортеж словарей у которых в ключах "skills"
        есть полное соответствие хотя бы с одним скиллом"""

        tuple_candidates = ()
        list_candidates = self.load_candidates_from_json()
        for l in list_candidates:
            if skill_name.lower() in l["skills"].lower().split(", "):
                tuple_candidates += (l,)
        return tuple_candidates

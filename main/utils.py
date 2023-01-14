import datetime
import requests





def clean_vacancy(vacancy):
    if vacancy['salary']['from'] != None and vacancy['salary']['to'] != None and vacancy['salary']['from'] != vacancy['salary']['to']:
        vacancy['salary'] = f"от {'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} до {'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['from'] != None:
        vacancy['salary'] = f"{'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['to'] != None:
        vacancy['salary'] = f"{'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    else:
        vacancy['salary'] = 'Нет данных'
    vacancy['key_skills'] = ', '.join(map(lambda x: x['name'], vacancy['key_skills']))
    return vacancy


def get_vacancies():
    try:
        params = {
            'text': 'Gamedev', #название твоей професии
            'specialization': 1,
            'page': 1,
            'per_page': 100,
            'date_from': f'2015-12-15T00:00:00+0300',
            'date_to': f'2022-12-17T00:00:00+0300',

        }
        data = []
        info = requests.get('https://api.hh.ru/vacancies', params).json()
        for row in info['items']:
            if not row['salary'] is None:
                data.append({'id': row['id'], 'published_at': row['published_at']})
        data = sorted(data, key=lambda x: x['published_at'])
        vacancies = []
        for vacancy in data[len(data) - 10:]:
            vacancies.append(clean_vacancy(requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()))
        return vacancies
    except Exception as e:
        print(e)
        print(datetime.datetime.now())
        return []


if __name__ == "__main__":
    get_vacancies()

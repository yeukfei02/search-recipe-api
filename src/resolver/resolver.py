from ariadne import QueryType, MutationType
import requests
import uuid

FORKIFY_API_ROOT_URL = 'https://forkify-api.herokuapp.com/api/search'
FORKIFY_API_ROOT_URL_GET_BY_ID = 'https://forkify-api.herokuapp.com/api/get'
RECIPEPUPPY_ROOT_URL = 'http://www.recipepuppy.com/api'

query = QueryType()
mutation = MutationType()


@query.field("searchRecipe")
def resolve_search_recipe(_, info, input):
    print("input = {0}".format(input))

    params = {}

    if 'query' in input:
        query = input['query']
        if query:
            params['q'] = query

    response = requests.get(FORKIFY_API_ROOT_URL, params=params)
    if response:
        response_json = response.json()
        print("response_json = {0}".format(response_json))

        if response_json:
            result_list = response_json.get('recipes')
            count = response_json.get('count')

            response = {
                'results': result_list,
                'count': count
            }

    return response


@query.field("searchRecipeById")
def resolve_search_recipe_by_id(_, info, id):
    print("id = {0}".format(id))

    params = {}

    if id:
        params['rId'] = id

        response = requests.get(FORKIFY_API_ROOT_URL_GET_BY_ID, params=params)
        if response:
            response_json = response.json()
            print("response_json = {0}".format(response_json))

            if response_json:
                result = response_json.get('recipe')

                response = {
                    'result': result,
                }

    return response


@query.field("searchAnothorRecipe")
def resolve_search_another_recipe(_, info, input):
    print("input = {0}".format(input))

    params = {}
    params['p'] = 1

    if 'ingredients' in input:
        ingredients = input['ingredients']
        if ingredients:
            params['i'] = ingredients

    if 'query' in input:
        query = input['query']
        if query:
            params['q'] = query

    if 'page' in input:
        page = input['page']
        if page:
            params['p'] = page

    response = requests.get(RECIPEPUPPY_ROOT_URL, params=params)
    if response:
        response_json = response.json()
        print("response_json = {0}".format(response_json))

        if response_json:
            result_list = response_json.get('results')

            response = {
                'results': result_list
            }

    return response


@mutation.field("createUser")
def resolve_create_user(_, info, input):
    request = info.context["request"]
    print("request.headers = {0}".format(request.headers))
    print("input = {0}".format(input))

    id = uuid.uuid4()
    name = input['name']
    print("id = {0}".format(id))
    print("name = {0}".format(name))

    if id and name:
        response = {
            'message': 'createUser'
        }

    return response

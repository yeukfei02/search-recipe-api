from ariadne import make_executable_schema
from ariadne.asgi import GraphQL

from src.schema.typeDefs import type_defs
from src.resolver.resolver import query, mutation


schema = make_executable_schema(type_defs, query, mutation)
app = GraphQL(schema, debug=True)

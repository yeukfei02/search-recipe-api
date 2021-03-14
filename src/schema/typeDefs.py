from ariadne import gql

type_defs = gql("""
    type Query {
        searchRecipe(input: SearchRecipeInput!): SearchRecipeResult!
        searchRecipeById(id: String!): SearchRecipeByIdResult!
        searchAnothorRecipe(input: SearchAnotherRecipeInput!): SearchAnotherRecipeResult!
    }

    type Mutation {
        createUser(input: CreateUserInput!): CreateUserResult!
    }

    type SearchRecipeResult {
        results: [Recipe!]!
        count: Int
    }

    type Recipe {
        recipe_id: String
        title: String
        publisher: String
        source_url: String
        image_url: String
        social_rank: Float
        publisher_url: String
    }

    type SearchRecipeByIdResult {
        result: SearchRecipeByIdRecipe!
    }

    type SearchRecipeByIdRecipe {
        recipe_id: String
        title: String
        publisher: String
        source_url: String
        image_url: String
        social_rank: Float
        publisher_url: String
        ingredients: [String]
    }

    type SearchAnotherRecipeResult {
        results: [AnotherRecipe!]!
    }

    type AnotherRecipe {
        title: String
        href: String
        ingredients: String
        thumbnail: String
    }

    type CreateUserResult {
        message: String!
    }

    input SearchRecipeInput {
        query: String!
    }

    input SearchAnotherRecipeInput {
        ingredients: String
        query: String
        page: String
    }

    input CreateUserInput {
        name: String!
    }
""")

import graphene

import demo.gql.resolvers as resolvers

class Mutation:
    create_prod_category = resolvers.CreateProductCategory.Field()
    create_product       = resolvers.CreateProduct.Field()
    manage_favorites     = resolvers.ManageFavorites.Field()
    comment              = resolvers.Comment.Field()
    register_user        = resolvers.RegisterUser.Field()
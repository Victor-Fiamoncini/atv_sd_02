''' This module defines all app data mappers '''

from post import Post

def map_post_dict_to_post_dto(post_dict: dict) -> Post:
    ''' Map post dictionary to a Post DTO '''

    return Post(
        id=post_dict['id'],
        user_id=post_dict['userId'],
        title=post_dict['title'],
        body=post_dict['body']
    )


def map_post_dto_to_post_dict(post: Post) -> dict:
    ''' Map post DTO to a post dictionary '''

    return {
        'id': post.id,
        'user_id': post.user_id,
        'title': post.title,
        'body': post.body
    }

from fastapi import APIRouter

from .services import (
    create_post,
    create_user,
    delete_post,
    read_all_posts,
    read_all_users,
    read_post,
    read_user,
)


def init_routes():
    router = APIRouter(prefix="/mysql", tags=["mysql"])

    router.add_api_route("/posts", create_post, methods={"POST"})
    router.add_api_route("/users", create_user, methods={"POST"})

    router.add_api_route("/users/{user_id}", read_user, methods={"GET"})
    router.add_api_route("/posts/{post_id}", read_post, methods={"GET"})
    router.add_api_route("/all_users", read_all_users, methods={"GET"})
    router.add_api_route("/all_posts", read_all_posts, methods={"GET"})

    router.add_api_route("/posts/{post_id}", delete_post, methods={"DELETE"})

    return router

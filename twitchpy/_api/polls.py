from .._utils import http
from ..dataclasses import Poll

ENDPOINT_POLLS = "https://api.twitch.tv/helix/polls"


def get_polls(
    token: str,
    client_id: str,
    broadcaster_id: str,
    poll_ids: list[str] | None = None,
    first: int = 20,
) -> list[Poll]:
    url = ENDPOINT_POLLS
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id,
    }
    params = {}
    params["broadcaster_id"] = broadcaster_id

    if poll_ids is not None and len(poll_ids) > 0:
        params["id"] = poll_ids

    polls = http.send_get_with_pagination(url, headers, params, first, 20)

    return [
        Poll(
            poll["id"],
            poll["broadcaster_id"],
            poll["broadcaster_name"],
            poll["broadcaster_login"],
            poll["title"],
            poll["choices"],
            poll["channel_points_voting_enabled"],
            poll["channel_points_per_vote"],
            poll["status"],
            poll["duration"],
            poll["started_at"],
        )
        for poll in polls
    ]


def create_poll(
    token: str,
    client_id: str,
    broadcaster_id: str,
    title: str,
    choices: list[str],
    duration: int,
    channel_points_voting_enabled: bool = False,
    channel_points_per_vote: int = 0,
) -> Poll:
    url = ENDPOINT_POLLS
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id,
        "Content-Type": "application/json",
    }

    choices_dicts = []

    for choice in choices:
        choices_dicts.append({"title": choice})

    payload = {
        "broadcaster_id": broadcaster_id,
        "title": title,
        "choices": choices_dicts,
        "duration": duration,
    }

    if channel_points_voting_enabled is not False:
        payload["channel_points_voting_enabled"] = channel_points_voting_enabled

    if channel_points_per_vote != 0:
        payload["channel_points_per_vote"] = channel_points_per_vote

    poll = http.send_post_get_result(url, headers, payload)[0]

    return Poll(
        poll["id"],
        poll["broadcaster_id"],
        poll["broadcaster_name"],
        poll["broadcaster_login"],
        poll["title"],
        poll["choices"],
        poll["channel_points_voting_enabled"],
        poll["channel_points_per_vote"],
        poll["status"],
        poll["duration"],
        poll["started_at"],
    )


def end_poll(
    token: str, client_id: str, broadcaster_id: str, poll_id: str, status: str
) -> Poll:
    url = ENDPOINT_POLLS
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id,
    }
    data = {"broadcaster_id": broadcaster_id, "id": poll_id, "status": status}

    poll = http.send_patch_get_result(url, headers, data)[0]

    return Poll(
        poll["id"],
        poll["broadcaster_id"],
        poll["broadcaster_name"],
        poll["broadcaster_login"],
        poll["title"],
        poll["choices"],
        poll["channel_points_voting_enabled"],
        poll["channel_points_per_vote"],
        poll["status"],
        poll["duration"],
        poll["started_at"],
    )

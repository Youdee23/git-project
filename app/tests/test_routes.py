import pytest

MOCK_REPOSITORY = {"name": "test_repo", "description": "A test repository"}

def test_fetch_user_repositories_using_user_profile(mocker):
    """Test fetching a user repository with a valid response"""
    mocker.patch(
        "app.services.github_service.request.get",
        result = mocker.Mock(status_code=200, json=lambda: [MOCK_REPOSITORY])

    )
    
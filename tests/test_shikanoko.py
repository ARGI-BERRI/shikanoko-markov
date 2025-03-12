from unittest import mock


import shikanoko.shikanoko as shikanoko


@mock.patch("shikanoko.shikanoko.next_token")
def test_get_markov_result(mock_next_token: mock.MagicMock) -> None:
    tokens = "しかのこのこのここしたんたん."
    mock_next_token.side_effect = list(tokens)

    assert shikanoko.get_markov_result() == tokens


def test_next_token() -> None:
    for k, v in shikanoko.MAPPING.items():
        assert shikanoko.next_token(k) in v

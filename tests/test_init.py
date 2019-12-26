import izakaya


def test_init() -> None:
    assert izakaya

    assert isinstance(izakaya.__version_info__, tuple)
    assert izakaya.__version_info__
    assert isinstance(izakaya.__version__, str)
    assert len(izakaya.__version__)

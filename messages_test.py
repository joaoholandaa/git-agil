from messages import display_messages

def test_messages():
    assert 'Legal demais' in display_messages

def test_messages_two():
    assert 'Seja Feliz :)' in display_messages
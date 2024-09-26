def test_flipper_v2_initial_state(flipper_v2):
    initial_state = flipper_v2.get_state()
    assert initial_state == True


def test_flipper_v2_change_state_with_flip(flipper_v2, alice):
    assert flipper_v2.get_state() == True

    flipper_v2.flip(sender=alice)

    assert flipper_v2.get_state() == False

def test_flipper_initial(flipper):
    assert flipper.flip() == True


def test_change_flip(flipper, another):
    flipper.flipping(sender=another)
    assert flipper.flip() == False

def test_get_fliped_event(flipper, another):
    tx = flipper.flipping(sender=another)
    event_list = tx.decode_logs(flipper.Fliped)
    event = event_list[0].event_arguments

    assert event == {"state": False}
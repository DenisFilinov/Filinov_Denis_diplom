import sender_stand_request
import data


def test_order_creation():
    new_res = sender_stand_request.CREATE_ORDER_PATH_NEW()
    track = new_res.json()['track']
    response = sender_stand_request.NUMBER_TRACK(track)
    assert response.status_code == 200


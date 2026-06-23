from sortex.models.detection_event import DetectionEvent


def test_detection_event_is_constructible() -> None:
    event = DetectionEvent(
        object_id=1,
        frame_id=2,
        timestamp_ms=3.0,
        class_name="proxy_product",
        decision="accept",
        confidence=0.9,
        center_px=(10.0, 20.0),
        bbox_px=(5.0, 10.0, 10.0, 20.0),
    )
    assert event.object_id == 1

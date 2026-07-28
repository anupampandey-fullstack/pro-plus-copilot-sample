import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.backend import database


def test_manga_maniacs_activity_is_seeded_with_expected_details():
    activity = database.initial_activities.get("Manga Maniacs")

    assert activity is not None
    assert activity["description"] == "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels)."
    assert activity["schedule"] == "Tuesdays, 7:00 PM - 8:00 PM"
    assert activity["schedule_details"]["days"] == ["Tuesday"]
    assert activity["schedule_details"]["start_time"] == "19:00"
    assert activity["schedule_details"]["end_time"] == "20:00"
    assert activity["max_participants"] == 15

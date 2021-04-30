from times import compute_overlap_time, time_range

def test_compute_overlap_within():
    long_time_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short_time_range = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(long_time_range, short_time_range)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_workshop_nonoverlapping():
    long_time_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short_time_range = time_range("2010-01-12 13:00:00", "2010-01-12 15:00:00", 2, 60)
    result = compute_overlap_time(long_time_range, short_time_range)
    expected = []
    assert result == expected

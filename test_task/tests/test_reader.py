from reader import read_csv, get_hourly_rate

def test_read_csv(tmp_path):
    test_file = tmp_path / "test.csv"
    test_file.write_text("id,name,department,hours_worked,rate\n1,Alice,Marketing,160,50\n")
    result = read_csv(str(test_file))
    assert result[0]['name'] == 'Alice'
    assert result[0]['department'] == 'Marketing'

def test_get_hourly_rate():
    row1 = {'hourly_rate': '40'}
    row2 = {'rate': '60'}
    row3 = {'salary': '70'}
    assert get_hourly_rate(row1) == 40
    assert get_hourly_rate(row2) == 60
    assert get_hourly_rate(row3) == 70

import demo
import pytest

#basics is a custom marker defined in pytest.ini 
@pytest.mark.basics
def test_basics():
    assert True
    assert 1 < 2
    assert 1 <= 2
    assert 2 > 1

#basics is a custom marker defined in pytest.ini   
@pytest.mark.basics
def test_basics2():
    assert 2 >= 1
    assert 2 == 2
    assert 3 != 2
    assert 'hello' in ' hello world'

#addition is a custom marker defined in pytest.ini 
@pytest.mark.addition
class TestAdd:
    def test_add(self):
        assert demo.add(1,2) == 3

    @pytest.mark.parametrize(
        'a, b, expected',[ 
            (1,1,2),
            (2,1,3),
            (3,1,4),
            (4,1,5),
            (5,1,6),
            (6,1,7),
            (7,1,8),
            (8,1,9),
            (9,1,10),
        ]
    )
    def test_with_param(self,a, b, expected):
        assert demo.add(a,b) == expected


    def test_error(self):
        # Waiting the code to fail. The test runs properly in terminal
        with pytest.raises(demo.MysteryError):
            demo.add(99,1)



def test_fixture(my_fixture):
    assert my_fixture ==51


def test_capsys(capsys):
    print("hello")
    out, err = capsys.readouterr()
    assert "hello" in out

def test_monkeypatch(monkeypatch):
    def fake_add(a,b):
        return 51
    monkeypatch.setattr(demo,"add",fake_add)
    assert demo.add(2,3) == 51

def test_tmpdir(tmpdir):
    some_file = tmpdir.join('something.txt')
    some_file.write('{"hello": "world"}')
    result = demo.read_json(str(some_file))
    assert result["hello"] == "world"

def test_fixture_with_fixtures(capsys,captured_print):
    print('more')

    out,err = capsys.readouterr()

    assert out == "hello\nmore\n"

import simple

def test_simple():
    assert simple.add(2, 2) == 4

def test_str():
    assert simple.add('hello', 'world') == 'helloworld'

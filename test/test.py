import pytest
import subprocess

@pytest.fixture
def test_simple():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "python files"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    if len(result) == 6:
        return True
    else:
        return False
    

@pytest.fixture
def test_medium():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "images file"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    if len(result) == 5:
        return True
    else:
        return False
    
@pytest.fixture
def test_hard():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "mp3 files with a a in the filename"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    if len(result) == 2:
        return True
    else:
        return False
    

@pytest.fixture
def test_file():
    proc = subprocess.Popen(['cat test/test-files/words.txt | lgrep "contains a hyphen"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    if len(result) == 8:
        return True
    else:
        return False


def test_directory_tree(test_simple, test_medium, test_hard):
    assert test_simple
    assert test_medium
    assert test_hard
    
def test_files(test_file):
    assert test_file
    
    
import pytest
import subprocess

def test_simple():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "python files"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    assert len(result) == 6
    

def test_medium():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "files that have an image extension"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    assert len(result) == 5
    

def test_hard():
    proc = subprocess.Popen(['ls test/test-tree | lgrep "mp3 files with a a in the filename"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    assert len(result) == 2
    

def test_file():
    proc = subprocess.Popen(['cat test/test-files/words.txt | lgrep "contains a hyphen"'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    out, _ = proc.communicate()
    result = out.decode('utf-8').split('\n')[1:-1]
    assert len(result) == 8
    
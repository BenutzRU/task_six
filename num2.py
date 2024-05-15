import pytest
from num2fix import merge_and_write

@pytest.fixture
def test_files(tmp_path):
    file1_content = 'cont1'
    file2_content = 'cont2'

    file1_path = tmp_path / 'file1.txt'
    file2_path = tmp_path / 'file2.txt'
    output_file_path = tmp_path / 'output.txt'

    with open(file1_path, 'w') as file1:
        file1.write(file1_content)
    with open(file2_path, 'w') as file2:
        file2.write(file2_content)

    return file1_path, file2_path, output_file_path

def testoutput(test_files):
    file1_path, file2_path, output_file_path = test_files
    assert merge_and_write(file1_path, file2_path, output_file_path) == 'cont1 cont2'

def testfiles(test_files):
    file1_path, file2_path, output_file_path = test_files
    assert merge_and_write(file1_path, 'test_file.txt', output_file_path) == "Один из файлов не найден"
    assert merge_and_write('test_file.txt', file2_path, output_file_path) == "Один из файлов не найден"
    assert merge_and_write('test_file1.txt', 'test_file2.txt', output_file_path) == "Один из файлов не найден"

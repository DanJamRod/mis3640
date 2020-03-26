def sed(pattern, replacement, file_1, file_2):
    """ Takes as arguments a pattern string, a replacement string, and two filenames;
    it should read the first file and write the contents into the second file (creating it if necessary).
    If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
    """
    with open(file_1, "r") as fin:
        with open(file_2, "w") as fout:
            for line in fin:
                fout.write(line.replace(pattern, replacement))

sed("'d", "ed", "session14/test_input.txt", "session14/test_output.txt")
import most_elected_name as prog
import pytest as p


# test function that removes non-names from start of name
def test_clean_names():
    names_set = {
        "Col. Daniel",
        "Dr. Carolina",
        "Padre Fábio"
        }
    clean_names =  prog.clean_names(names_set)
    assert clean_names == {"Daniel", "Carolina", "Fábio"}


# test function that counts amount of names
def test_count_names():
    names_set = {"Daniel A", "Carol C", "Carol J", "Jordan", "Jordandan"}
    names_count = prog.count_names(names_set)
    assert names_count == {"Daniel": 1, "Carol": 2, "Jordan": 1, "Jordandan": 1}


# test if the displayed dictionaries are in the right order
def test_display_scores(capsys):
    names_score = {"Carol": 2, "Daniel": 1, "Jordan": 1, "Jordandan": 1}
    prog.display_scores(names_score)
    # capture the print
    captured = capsys.readouterr()
    assert captured.out == "Carol: 2\nDaniel: 1\nJordan: 1\nJordandan: 1\n"
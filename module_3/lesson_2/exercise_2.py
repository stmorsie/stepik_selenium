def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring} to be substring of '{full_text}'"
    # ваша реализация, напишите assert и сообщение об ошибке
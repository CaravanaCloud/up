from up_lib.parser import parse


def test_wait_true():
    # given
    line = "wait: true"
    # when
    (cmd, opts, prompt) = parse(line)
    # then assert actual == expected
    assert cmd == "wait"
    assert tuple(prompt) == ("true",)


def test_parse_simple_wait():
    # given
    line = "WAIT --timeout=42: aws sts get-caller-identity"
    # when
    (cmd, opts, prompt) = parse(line)
    # then
    assert cmd == "wait"
    assert tuple(prompt) == ("aws", "sts", "get-caller-identity",)
    assert opts["timeout"] == '42'


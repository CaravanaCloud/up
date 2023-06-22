from up_lib.parser import parse_action

def parse_wait(line):
    return parse_action(line, ["wait"]).as_tuple()

def test_wait_true():
    # given
    line = "wait: true"
    # when
    (action, opts, prompt) = parse_wait(line)
    # then assert actual == expected
    assert action == "wait"
    assert tuple(prompt) == ("true",)


def test_parse_simple_wait():
    # given
    line = "WAIT --timeout=42: aws sts get-caller-identity"
    # when
    (action, opts, prompt) = parse_wait(line)
    # then
    assert action == "wait"
    assert tuple(prompt) == ("aws", "sts", "get-caller-identity",)
    assert opts["timeout"] == '42'


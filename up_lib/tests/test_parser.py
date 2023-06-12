from up_lib.parser import parse


def test_wait_true():
    # given
    line = "wait: true"
    # when
    cmd = parse(line)
    # then
    assert cmd.command == ("wait",)
    assert tuple(cmd.prompt) == ("true",)


def test_parse_simple_wait():
    # given
    line = "wait --timeout=42: aws sts get-caller-identity"
    # when
    cmd = parse(line)
    # then
    assert cmd.command == ("wait",)
    assert tuple(cmd.prompt) == ("aws", "sts", "get-caller-identity",)
    assert cmd.options["timeout"] == '42'


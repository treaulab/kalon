from kalon.cli import main


def test_cli_prints_version(capsys):
    main()
    assert capsys.readouterr().out.startswith("kalon ")

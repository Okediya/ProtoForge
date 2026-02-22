import pytest
from typer.testing import CliRunner
from protoforge.cli import app

runner = CliRunner()

def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "ProtoForge" in result.stdout

def test_new_project(tmp_path):
    # Change to tmp_path
    import os
    old_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        result = runner.invoke(app, ["new", "test-project"])
        assert result.exit_code == 0
        assert (tmp_path / "test-project" / "protoforge.yaml").exists()
    finally:
        os.chdir(old_cwd)

def test_simulate():
    result = runner.invoke(app, ["simulate"])
    assert result.exit_code == 0
    assert "Starting ProtoForge Simulation Engine" in result.stdout

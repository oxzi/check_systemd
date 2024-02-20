"""Test the D-Bus API as a data source."""

from unittest.mock import patch

import check_systemd


class TestDbus:
    def test_mocking(self) -> None:
        with patch("sys.exit"), patch("check_systemd.is_gi"), patch(
            "check_systemd.DbusManager"
        ), patch("sys.argv", ["check_systemd.py", "--dbus"]):
            check_systemd.main()

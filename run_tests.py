import pytest


pytest.main([
    "tests",
    "-v",
    "--html=reports/report.html",
    "--self-contained-html"
])
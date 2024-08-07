"""Tests the zorg project's 'db' CLI command."""

from __future__ import annotations

from pathlib import Path
import sqlite3

from pytest import fixture
from syrupy.assertion import SnapshotAssertion as Snapshot


@fixture(name="sql_cursor", scope="session")
def sql_cursor_fixture(zettel_dir: Path) -> sqlite3.Cursor:
    """Connects to the zorg DB created by 'zorg db create'."""
    db_path_str = f"{zettel_dir}/.zorg/zorg.db"
    conn = sqlite3.connect(db_path_str)
    return conn.cursor()


def test_run_db_create__table_names(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check the SQL table names generated by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__file_count(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check the number of *.zo files indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT COUNT(*) FROM page")
    assert snapshot == sql_cursor.fetchone()[0]


def test_run_db_create__note_count(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check the number of zorg notes indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT COUNT(*) FROM note")
    assert snapshot == sql_cursor.fetchone()[0]


def test_run_db_create__todo_count(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check the number of zorg todos indexed by running 'zorg db create'."""
    sql_cursor.execute(
        "SELECT COUNT(*) FROM note WHERE todo_status IS NOT NULL"
    )
    assert snapshot == sql_cursor.fetchone()[0]


def test_run_db_create__projects(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what projects are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM project")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__areas(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what areas are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM area")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__people(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what people are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM person")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__contexts(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what contexts are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM context")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__links(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what links are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM link")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__properties(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what properties are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT name FROM property")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__create_dates(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what create dates are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT DISTINCT create_date FROM note")
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__todo_priorities(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what todo priorities are indexed by running 'zorg db create'."""
    sql_cursor.execute(
        "SELECT DISTINCT todo_priority FROM note WHERE todo_priority IS"
        " NOT NULL"
    )
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__todo_statuses(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what todo statuses are indexed by running 'zorg db create'."""
    sql_cursor.execute(
        "SELECT DISTINCT todo_status FROM note WHERE todo_status IS NOT NULL"
    )
    assert snapshot == sorted(row[0] for row in sql_cursor.fetchall())


def test_run_db_create__zids(
    sql_cursor: sqlite3.Cursor, snapshot: Snapshot
) -> None:
    """Check what create dates are indexed by running 'zorg db create'."""
    sql_cursor.execute("SELECT DISTINCT zid FROM note")
    assert snapshot == sorted(
        row[0] for row in sql_cursor.fetchall() if row[0]
    )

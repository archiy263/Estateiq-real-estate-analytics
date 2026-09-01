import sqlite3
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

DB_PATH = PROJECT_ROOT / "data" / "estateiq.db"
SQL_DIR = PROJECT_ROOT / "sql"


if not DB_PATH.exists():
    raise FileNotFoundError(
        f"Database not found: {DB_PATH}"
    )


sql_filename = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "01_data_quality.sql"
)

SQL_PATH = SQL_DIR / sql_filename


if not SQL_PATH.exists():
    raise FileNotFoundError(
        f"SQL file not found: {SQL_PATH}"
    )


connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

sql_script = SQL_PATH.read_text(
    encoding="utf-8"
)

statements = [
    statement.strip()
    for statement in sql_script.split(";")
    if statement.strip()
]


print()
print("EstateIQ SQL Analysis")
print("=" * 45)
print(f"Database: {DB_PATH.name}")
print(f"SQL file: {SQL_PATH.name}")
print("=" * 45)


query_number = 0

for statement in statements:

    lines = [
        line
        for line in statement.splitlines()
        if not line.strip().startswith("--")
    ]

    statement = "\n".join(lines).strip()

    if not statement:
        continue

    query_number += 1

    cursor.execute(statement)

    print()
    print(f"Query {query_number}")
    print("-" * 45)

    if cursor.description:

        columns = [
            column[0]
            for column in cursor.description
        ]

        rows = cursor.fetchall()

        print(" | ".join(columns))

        for row in rows:
            print(
                " | ".join(
                    str(value)
                    for value in row
                )
            )

    else:
        print("Query executed successfully.")


connection.close()

print()
print("=" * 45)
print("SQL analysis completed successfully.")
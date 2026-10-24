# Python - Object-relational mapping

Scripts that connect Python to a MySQL database, first with `MySQLdb` and
raw SQL, then with the `SQLAlchemy` ORM where tables become Python classes
and no SQL is written.

## Requirements

- Ubuntu 20.04 LTS, `python3` 3.8.5
- MySQL 8.0, `mysqlclient` 2.0.x (`import MySQLdb`) and `SQLAlchemy` 1.4.x
- Code style checked with `pycodestyle`

## Usage

Every script takes the MySQL user name, password and database name as its
first three arguments, and connects to MySQL on localhost, port 3306. Some
take a fourth argument. Load the matching `.sql` file first to create the
data:

    $ cat 0-select_states.sql | mysql -uroot -p
    $ ./0-select_states.py root root hbtn_0e_0_usa
    (1, 'California')
    (2, 'Arizona')
    (3, 'Texas')
    (4, 'New York')
    (5, 'Nevada')

## Files

### Part 1: MySQLdb

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states of `hbtn_0e_0_usa` sorted by id |
| `1-filter_states.py` | Lists the states whose name starts with an upper case N |
| `2-my_filter_states.py` | Lists the states matching the argument (built with `format`, open to injection) |
| `3-my_safe_filter_states.py` | Same as above, safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities of `hbtn_0e_4_usa` with their state name |
| `5-filter_cities.py` | Lists the cities of the state given as argument, safe from injection |

### Part 2: SQLAlchemy

| File | Description |
|------|-------------|
| `model_state.py` | `Base` and the `State` class linked to the table `states` |
| `7-model_state_fetch_all.py` | Lists all `State` objects sorted by id |
| `8-model_state_fetch_first.py` | Prints the first `State`, or `Nothing` if the table is empty |
| `9-model_state_filter_a.py` | Lists the `State` objects containing the letter a |
| `10-model_state_my_get.py` | Prints the id of the state named in the fourth argument, or `Not found` |
| `11-model_state_insert.py` | Adds the state Louisiana and prints its id |
| `12-model_state_update_id_2.py` | Renames the state with id 2 to New Mexico |
| `13-model_state_delete_a.py` | Deletes the states whose name contains the letter a |
| `model_city.py` | The `City` class linked to the table `cities` |
| `14-model_city_fetch_by_state.py` | Prints all cities as `<state name>: (<city id>) <city name>` |

## Notes

- Each script does nothing when imported; the work is under
  `if __name__ == "__main__":`.
- Task 2 builds its query with `format` on purpose, to show SQL injection.
  Tasks 3 and 5 pass the input as a parameter, which makes them safe.
- No `execute` is used with SQLAlchemy; the queries are built with the ORM.

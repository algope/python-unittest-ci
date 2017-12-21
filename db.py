import sqlite3


def create_database():

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # insert multiple voters
    voters = [('44444444Y', 'Alejandro', 'González', False),
              ('43333333K', 'Carmen', 'Pérez', False),
              ('05888888G', 'Antonio', 'González', False)]

    cursor.executemany("INSERT INTO census VALUES (?,?,?,?,?)", voters)
    conn.commit()


def delete_voter(dni):
    """
    Delete an artist from the database
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = """
    DELETE FROM census
    WHERE id = ?
    """
    cursor.execute(sql, [dni])
    conn.commit()
    cursor.close()
    conn.close()


def update_voter(dni, voted):
    """
    Update the artist name
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = """
    UPDATE census
    SET has_voted = ?
    WHERE id = ?
    """
    cursor.execute(sql, (voted, dni))
    conn.commit()
    cursor.close()
    conn.close()


def select_voter(dni):
    """
    Query the database for all the albums by a particular artist
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM census WHERE id=?"
    cursor.execute(sql, [(dni)])
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os

    if not os.path.exists("mydatabase.db"):
        create_database()

    delete_voter('44444444Y')
    update_voter('43333333K', True)
    print(select_voter('43333333K'))

import sqlite3


def kindness(*data, symp_kind):
    con = sqlite3.connect('actions.db')
    cur = con.cursor()
    for i in data:
        result = cur.execute(f"""
        SELECT name FROM People
        WHERE id IN (SELECT city_id FROM Cities WHERE city = {i})
        """).fetchall()
    con.close()
    return result
kjhkjhkj

data = ['Genoa', 'Shiraz', 'Isfahan', 'Sivas', 'Iconion', 'Qom']
print(*kindness(*data, symp_kind=9), sep='\n')
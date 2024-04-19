import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        database='crud'
    )

    print("連結成功")

    cur = conn.cursor()

    cur.execute("SELECT * FROM students")

    # 查詢結果：
    data = cur.fetchall()
    print("查詢結果：", data)

    # 關閉
    cur.close()
    conn.close()

except pymysql.Error as e:
    print("連結錯誤:", e)

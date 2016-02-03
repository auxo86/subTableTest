import sqlite3

conn = sqlite3.connect('job_arrange.db')
c = conn.cursor()
c.execute('drop table if exists MemberWithoutByPass;')
c.execute('drop table if exists MemberWithoutByPassAndWithoutDiscount;')
c.execute('create table MemberWithoutByPass as select name from member_array where by_pass = 0 order by arrange_order;')
c.execute('create table MemberWithoutByPassAndWithoutDiscount as select name from member_array where by_pass = 0 and discount = 0 order by arrange_order;')
c.execute('delete from ForArrange;')
c.execute('vacuum;')
c.execute('insert into ForArrange (name) select name from (select * from MemberWithoutByPass union all select * from MemberWithoutByPassAndWithoutDiscount);')
conn.commit()

conn.close()
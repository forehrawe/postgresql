### If you want to change the database owner:

```sql
ALTER DATABASE {db_name} OWNER TO {target_user};
```

---

### Create a new user:

```sql
CREATE USER {name} WITH PASSWORD '1234';
```

---

### Grant privileges:

```sql
GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {user_name};
```

---

### Create a new database:

```sql
CREATE DATABASE {name};
```

---

### Connect to a database:

```sql
\c {db_name}
```

---

### List all databases:

```sql
\l
```

---

### List all tables:

```sql
\dt
```

---

### Show table structure:

```sql
\d {table_name}
```

---

### List all users:

```sql
\du
```

---

### Exit:

```sql
\q
```

---

```bash
sudo -i -u postgres
psql
...
```
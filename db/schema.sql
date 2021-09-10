create table regions (
    id integer primary key autoincrement,
    name varchar(30)
);

create table data_types (
    id integer primary key autoincrement,
    name varchar(10),
    units varchar(5)
);

create table reports (
    id integer primary key autoincrement,
    year varchar(4),
    month varchar(2),
    region_id ref int,
    co2_output float,
    trees_num int,
    FOREIGN KEY(region_id) REFERENCES regions(id)
);
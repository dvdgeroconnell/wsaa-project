
use wsaa_project

create table records (id int AUTO_INCREMENT PRIMARY KEY, title varchar(250), artist varchar(250), year int, genre varchar(250));

insert into records (title, artist, year, genre) values ('Foxtrot','Genesis',1973,'Prog');
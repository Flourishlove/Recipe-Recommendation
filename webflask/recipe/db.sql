drop table if exists recipes;
create table recipes (
  id integer primary key,
  name text not null,
  ingredient text not null,
  flavor varchar(50) not null
);

INSERT INTO `recipes` (`id`, `name`, `ingredient`, `flavor`)
VALUES
    (1,'Ajiaco Cubano','egg', 'spicy'),
    (2,'Cacio e Pepe with English Peas','egg,water','sweet'),
    (3,'Cheesy Chili Mac','ingredient1,ingredient2','sweet'),
    (4,'Chicken And Chorizo Paella','vegetable, meat','hot');

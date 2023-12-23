CREATE TABLE Hero
(
  Name CHAR(20) NOT NULL,
  Attribute CHAR(3) NOT NULL,
  Attack_type CHAR(10) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE Role
(
  Role_name CHAR(20) NOT NULL,
  PRIMARY KEY (Role_name)
);

CREATE TABLE play_role
(
  Name CHAR(20) NOT NULL,
  Role_name CHAR(20) NOT NULL,
  PRIMARY KEY (Name, Role_name),
  FOREIGN KEY (Name) REFERENCES Hero(Name),
  FOREIGN KEY (Role_name) REFERENCES Role(Role_name)
);

create view HeroNumberByAttribute as select attribute, count(*) from hero
group by attribute;
create view HeroNumberByAttackType as select attack_type, count(*) from hero
group by attack_type;
create view PossibleRolesNumberByAttribute as select attribute, count(*) from play_role, hero
where hero.name = play_role.name
group by attribute;
-------------------Populate heros------------------
INSERT INTO hero(name, attribute, attack_type)
VALUES('Abaddon', 'all', 'meele');
INSERT INTO hero(name, attribute, attack_type)
VALUES('Bloodseeker', 'agi', 'meele');
INSERT INTO hero(name, attribute, attack_type)
VALUES('Drow Ranger', 'agi', 'ranged');
INSERT INTO hero(name, attribute, attack_type)
VALUES('Enigma', 'all', 'ranged');
INSERT INTO hero(name, attribute, attack_type)
VALUES('Mars', 'str', 'meele');
------------------Populate roles------------------
INSERT INTO role(role_name)
VALUES('Support');
INSERT INTO role(role_name)
VALUES('Carry');
INSERT INTO role(role_name)
VALUES('Initiator');
INSERT INTO role(role_name)
VALUES('Disabler');
INSERT INTO role(role_name)
VALUES('Durable');
-----------------Populate play_role---------------
INSERT INTO play_role(name, role_name)
VALUES('Abaddon', 'Support');
INSERT INTO play_role(name, role_name)
VALUES('Abaddon', 'Carry');
INSERT INTO play_role(name, role_name)
VALUES('Abaddon', 'Durable');
INSERT INTO play_role(name, role_name)
VALUES('Bloodseeker', 'Carry');
INSERT INTO play_role(name, role_name)
VALUES('Bloodseeker', 'Initiator');
INSERT INTO play_role(name, role_name)
VALUES('Drow Ranger', 'Carry');
INSERT INTO play_role(name, role_name)
VALUES('Drow Ranger', 'Disabler');
INSERT INTO play_role(name, role_name)
VALUES('Enigma', 'Disabler');
INSERT INTO play_role(name, role_name)
VALUES('Mars', 'Disabler');
INSERT INTO play_role(name, role_name)
VALUES('Mars', 'Durable');

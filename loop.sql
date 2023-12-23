--select * from hero;
--create table herocopy as select * from hero; 
--delete from herocopy;
select * from herocopy;


DO $$
 DECLARE
     hero_name   		herocopy.name%TYPE;
     hero_attribute 	herocopy.attribute%TYPE;
	 hero_attacktype	herocopy.attack_type%TYPE;

 BEGIN
     hero_name := 'Hero';
	 hero_attribute := 'at';
	 hero_attacktype := 'type';
     FOR counter IN 0..9
         LOOP
            INSERT INTO herocopy (name, attribute, attack_type)
             VALUES (hero_name || counter, hero_attribute || counter, hero_attacktype || counter);
         END LOOP;
 END;
 $$

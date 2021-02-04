 DROP DATABASE IF EXISTS Week_plane;
 CREATE DATABASE Week_plane;
 USE Week_plane;
 
 
 
 DROP TABLE IF EXISTS interests;
 CREATE TABLE interests (
 	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
 	interest Varchar(255),
 	color Varchar(255),
 	created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
     ) COMMENT '������� ���������';
    
 DROP TABLE IF EXISTS goals;
 CREATE TABLE goals (
	id BIGINT UNSIGNED NOT NULL auto_increment unique,
 	interest_id BIGINT UNSIGNED NOT NULL,
	goal VARCHAR(255),
	status ENUM ('�������','�� �������') default '�� �������',
        created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
 	FOREIGN KEY (interest_id) REFERENCES interests(id),
 	INDEX goal (goal)
     ) COMMENT '���� ��������';
     
 DROP TABLE IF EXISTS date_interest;
 CREATE TABLE date_interest (
 	id BIGINT UNSIGNED NOT NULL auto_increment unique,
 	interest_id BIGINT UNSIGNED NOT NULL,
	dt DATE,
        created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
 	FOREIGN KEY (interest_id) REFERENCES interests(id),
 	INDEX dt (dt)
     ) COMMENT '���� ����';
     
 INSERT INTO interests(interest,color) VALUES 
 ('���-���','green'),
 ('�����','blue'),
 ('����������','red'),
 ('����','yellow');
 
 INSERT INTO goals(interest_id,goal) VALUES 
 (1,'������� � ����'),
 (1,'�������� 14 �������'),
 (2,'������� �������'),
 (3,'������� �� ��� ���������� �� �����'),
 (3,'����� �� ���'),
 (4,'����� ����� ����');


CREATE OR REPLACE VIEW  inter_goal AS SELECT a.interest , b.goal,b.status from  interests a join goals b on a.id =b.interest_id ;

select * from inter_goal;

CREATE OR REPLACE VIEW  inter_date AS SELECT a.interest , b.dt from  interests a join date_interest b on a.id =b.interest_id ;

select * from inter_date;
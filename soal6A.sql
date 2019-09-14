CREATE TABLE Category(
	id Int NOT NULL,
    salary Money,
    PRIMARY KEY (id)
    );

CREATE TABLE Work(
	id Int NOT NULL,
    name Varchar(255),
    id_salary Int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_salary) REFERENCES Category(id)
    );

CREATE TABLE Name(
	id Int NOT NULL,
    name Varchar(255),
    id_work Int,
    id_salary Int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_work) REFERENCES Work(id),
    FOREIGN KEY (id_salary) REFERENCES Category(id)
    );

INSERT INTO Category(id, salary)
    VALUES  (1, 10000000),
            (2, 12000000);

INSERT INTO Work(id, name, id_salary)
    VALUES  (1, 'Frontend Dev', 1),
            (2, 'Backend Dev', 2);

INSERT INTO Name(id, name, id_work, id_salary)
    VALUES  (1, 'Rebecca', 1, 1),
            (2, 'Vita', 2, 2);

SELECT n.name, w.name, c.salary
    FROM Name n, Work w, Category c
    WHERE n.id_work=w.id
        AND w.id_salary=c.id;
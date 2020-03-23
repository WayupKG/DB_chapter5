1. '''* Напишите запрос для отображения имен (имя, фамилия) сотрудника, используя псевдоним
        имя «Имя», «Фамилия»'''
    SELECT FIRST_NAME, LAST_NAME FROM employees;

 2. '''* Напишите запрос, чтобы получить уникальный идентификатор отдела из таблицы сотрудников.'''
    SELECT DEPARTMENT_ID FROM employees;

 3. '''* Напишите запрос, чтобы получить все данные о сотруднике из таблицы сотрудников по имени,
        по убыванию'''
    SELECT FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, JOB_ID, SALARY, DEPARTMENT_ID FROM employees ORDER BY SALARY DESC;

 4. '''* Написать запрос, чтобы получить идентификатор сотрудника, имена (имя, фамилия), зарплата в
        возрастающий порядок оплаты труда'''
    SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY FROM employees ORDER BY SALARY;

 5. '''* Напишите запрос, чтобы узнать количество сотрудников, работающих в компании.'''
    SELECT COUNT(EMPLOYEE_ID) FROM employees;

 6. '''* Написать запрос, чтобы отобразить имя (имя, фамилия) и зарплату для всех сотрудников
        чья зарплата не находится в диапазоне от 10000 до 15000 долларов'''
    SELECT FIRST_NAME, LAST_NAME, SALARY FROM employees WHERE SALARY NOT BETWEEN 10000 AND 15000 ORDER BY SALARY DESC;

 7. '''* Напишите запрос, чтобы отобразить имя (имя, фамилия) и идентификатор отдела всех
        сотрудники в отделах 30 или 100 в порядке возрастания'''
    SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM employees WHERE DEPARTMENT_ID BETWEEN 30 AND 100 ORDER BY DEPARTMENT_ID;
 
 8. ''' * Напишите запрос, чтобы отобразить имя (имя, фамилия) и дату приема на работу для всех
        сотрудники, которые были приняты на работу в 1987 году'''
    SELECT em.FIRST_NAME, em.LAST_NAME, jhD.START_DATE from job_history jhD LEFT JOIN employees em on em.EMPLOYEE_ID=jhD.EMPLOYEE_ID where START_DATE <= '1988 year';

 9. '''* Напишите запрос, чтобы отобразить фамилию, должность и зарплату для всех сотрудников, чья работа
         зарплата программиста или клерка доставки, чья зарплата не равна 4500 долларов,
         10 000 долларов США или 15 000 долларов США'''
    SELECT E.LAST_NAME, J.JOB_TITLE, E.SALARY FROM employees E LEFT JOIN jobs J ON J.JOB_ID = E.JOB_ID WHERE J.JOB_TITLE IN ('Programmer', 'Shipping Clerk') AND E.SALARY <> 4500 AND E.SALARY <> 10000 AND E.SALARY <> 15000 ORDER BY SALARY DESC;

 10. '''Написать запрос, чтобы выбрать все записи из сотрудников, где фамилия в «BLAKE», «SCOTT»,
        «КИНГ» и «ФОРД»'''
    SELECT * FROM employees WHERE LAST_NAME in ('King', 'Blake', 'Scott', 'Ford');

 11. '''* Напишите запрос, чтобы получить общую зарплату, выплачиваемую сотрудникам'''
    1) SELECT sum(SALARY) FROM employees;
    2) SELECT count(FIRST_NAME), sum(SALARY) FROM employees;

 12. '''* Напишите запрос, чтобы получить минимальную зарплату из таблицы сотрудников'''
    SELECT MIN(SALARY) FROM employees;

 13. '''* Напишите запрос, чтобы получить среднюю зарплату и количество сотрудников, 
          работающих на
          Отдел 90'''
    SELECT AVG(SALARY) AS Average_Salary, COUNT(DEPARTMENT_ID) AS Quantity_Employees FROM employees WHERE DEPARTMENT_ID = 90;

 14. '''* Напишите запрос, чтобы получить количество сотрудников с одинаковой работой'''
    SELECT J.JOB_TITLE, COUNT(E.EMPLOYEE_ID) AS number_of_employees_with_the_same_job FROM employees E LEFT JOIN jobs J ON E.JOB_ID = J.JOB_ID GROUP BY J.JOB_TITLE;

 15. '''* Напишите запрос, чтобы получить среднюю зарплату для каждого 
          идентификатора работы, исключая программиста'''
    SELECT J.JOB_ID, AVG(E.SALARY) AS Average_Salary FROM employees E LEFT JOIN jobs J ON E.JOB_ID = J.JOB_ID GROUP BY J.JOB_ID;
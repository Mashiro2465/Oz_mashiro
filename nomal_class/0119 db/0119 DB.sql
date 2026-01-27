-- DB 생성
create database test;
-- DB 선택
use test;

-- 1. employees 테이블 생성
create table employees(
	id int auto_increment primary key,
    name varchar(100),
    position varchar(100),
    salary decimal(10,2)
    );
    
-- 2. 직원 데이터 추가
insert into employees values(default, '혜린', 'PM', 90000);
insert into employees values(default, '은우', 'Frontend', 80000);
insert into employees values(default, '가을', 'Backend', 92000);
insert into employees values(default, '지수', 'Frontend', 7800);
insert into employees values(default, '민혁', 'Frontend', 96000);
insert into employees values(default, '하온', 'Backend', 130000);

-- 3. 모든 직원의 이름과 연봉 정보 조회

-- 1) Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요
select name,salary from employees where salary <=90000 and position ='Frontend';

-- 2) PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요
update employees set salary = salary*1.1 where position = 'pm';
select name,salary from employees where position = 'pm';

-- 3) 모든 Backend' 직책을 가진 직원의 연봉을 5% 인상하세요.
update employees set salary = salary*1.05 where position = 'Backend';
select name,salary from employees where position = 'Backend';

-- 4) 민혁 사원의 데이터를 삭제하세요
delete from employees where name = "민혁";
select * from employees;

-- 5) 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
select position, avg(salary) from employees group by position;

-- 6) employees 테이블 삭제
drop table employees;

    
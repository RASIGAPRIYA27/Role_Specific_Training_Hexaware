CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients
(
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
gender VARCHAR(10),
age INT,
city VARCHAR(50),
phone VARCHAR(15)
);

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(100)
);

CREATE TABLE doctors
(
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(100),
department_id INT,
consultation_fee DECIMAL(10,2)
);

CREATE TABLE appointments
(
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
appointment_status VARCHAR(30)
);

CREATE TABLE treatments
(
treatment_id INT PRIMARY KEY,
appointment_id INT,
treatment_name VARCHAR(100),
treatment_cost DECIMAL(10,2)
);

CREATE TABLE bills
(
bill_id INT PRIMARY KEY,
patient_id INT,
appointment_id INT,
bill_date DATE,
total_amount DECIMAL(10,2),
bill_status VARCHAR(30)
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
bill_id INT,
payment_mode VARCHAR(30),
paid_amount DECIMAL(10,2),
payment_status VARCHAR(30)
);

INSERT INTO departments VALUES
(101,'Cardiology'),
(102,'Neurology'),
(103,'Orthopedics'),
(104,'Pediatrics'),
(105,'Dermatology');

INSERT INTO doctors VALUES
(201,'Dr. Arjun Kumar','Cardiologist',101,1200),
(202,'Dr. Priya Menon','Neurologist',102,1000),
(203,'Dr. Sanjay Rao','Orthopedic Surgeon',103,900),
(204,'Dr. Meena Iyer','Pediatrician',104,700),
(205,'Dr. Karthik Raj','Dermatologist',105,800),
(206,'Dr. Nisha Verma','Cardiologist',101,1500),
(207,'Dr. Rahul Singh','Neurologist',102,950),
(208,'Dr. Vikram Patel','General Physician',999,600);

INSERT INTO patients VALUES
(301,'Ramesh Kumar','Male',45,'Hyderabad','9876543210'),
(302,'Suresh Babu','Male',38,'Chennai','9876543211'),
(303,'Lakshmi Devi','Female',29,'Hyderabad','9876543212'),
(304,'Anita Sharma','Female',52,'Bangalore','9876543213'),
(305,'Kiran Reddy','Male',41,'Hyderabad','9876543214'),
(306,'Deepa Nair','Female',35,'Kochi','9876543215'),
(307,'Vijay Kumar','Male',48,'Chennai','9876543216'),
(308,'Pooja Singh','Female',32,'Mumbai','9876543217'),
(309,'Amit Joshi','Male',27,'Delhi','9876543218'),
(310,'Sneha Patil','Female',44,'Pune','9876543219'),
(311,'Rajesh Gupta','Male',55,'Chennai','9876543220'),
(312,'Divya Rao','Female',36,'Bangalore','9876543221');

INSERT INTO appointments VALUES
(401,301,201,'2026-01-10','Completed'),
(402,302,202,'2026-01-12','Completed'),
(403,303,201,'2026-01-15','Completed'),
(404,304,203,'2026-01-20','Cancelled'),
(405,305,206,'2026-02-01','Completed'),
(406,306,204,'2026-02-05','Completed'),
(407,307,205,'2026-02-10','Completed'),
(408,308,201,'2026-02-15','Completed'),
(409,309,202,'2026-02-18','Cancelled'),
(410,310,203,'2026-02-20','Completed'),
(411,311,206,'2026-02-25','Completed'),
(412,312,204,'2026-03-01','Completed'),
(413,301,201,'2026-03-05','Completed'),
(414,302,202,'2026-03-08','Completed'),
(415,303,203,'2026-03-10','Completed'),
(416,304,204,'2026-03-12','Completed'),
(417,305,205,'2026-03-15','Completed'),
(418,306,201,'2026-03-18','Completed'),
(419,307,206,'2026-03-20','Completed'),
(420,999,201,'2026-03-25','Completed');

INSERT INTO treatments VALUES
(501,401,'ECG',2000),
(502,402,'Brain Scan',4500),
(503,403,'Heart Checkup',3000),
(504,405,'Angiography',12000),
(505,406,'Vaccination',1500),
(506,407,'Skin Therapy',2500),
(507,408,'ECG',2200),
(508,410,'Knee Treatment',6000),
(509,411,'Angioplasty',25000),
(510,412,'Vaccination',1500),
(511,413,'Heart Checkup',3500),
(512,414,'Brain Scan',5000),
(513,415,'Bone Surgery',15000),
(514,417,'Skin Therapy',3000),
(515,419,'Angiography',14000);

INSERT INTO bills VALUES
(601,301,401,'2026-01-10',3500,'Paid'),
(602,302,402,'2026-01-12',6000,'Paid'),
(603,303,403,'2026-01-15',4500,'Paid'),
(604,304,404,'2026-01-20',5500,'Unpaid'),
(605,305,405,'2026-02-01',15000,'Paid'),
(606,306,406,'2026-02-05',2500,'Paid'),
(607,307,407,'2026-02-10',4000,'Paid'),
(608,308,408,'2026-02-15',5000,'Paid'),
(609,309,409,'2026-02-18',7000,'Unpaid'),
(610,310,410,'2026-02-20',8000,'Paid'),
(611,311,411,'2026-02-25',30000,'Paid'),
(612,312,412,'2026-03-01',3000,'Paid'),
(613,301,413,'2026-03-05',4500,'Paid'),
(614,302,414,'2026-03-08',7000,'Paid'),
(615,303,415,'2026-03-10',18000,'Paid');

INSERT INTO payments VALUES
(701,601,'UPI',3500,'Paid'),
(702,602,'Credit Card',6000,'Paid'),
(703,603,'Cash',4500,'Paid'),
(704,604,'UPI',0,'Pending'),
(705,605,'UPI',15000,'Paid'),
(706,606,'Cash',2500,'Paid'),
(707,607,'Debit Card',4000,'Paid'),
(708,608,'UPI',5000,'Paid'),
(709,609,'Cash',0,'Pending'),
(710,610,'Credit Card',7500,'Paid'),
(711,611,'UPI',30000,'Paid'),
(712,612,'Cash',3000,'Paid'),
(713,613,'UPI',4500,'Paid'),
(714,614,'Credit Card',7000,'Paid'),
(715,615,'UPI',18000,'Paid');


-- 1:
select * from patients;

-- 2:
select * from doctors;

-- 3:
select * from patients where city='Hyderabad';

-- 4:
select d.* from doctors d
join departments dp
on d.department_id = dp.department_id
where dp.department_name = 'Cardiology';

-- 5:
select * from appointments
where appointment_date > '2026-01-01';

-- 6:
select * from appointments
where appointment_status = 'Cancelled';

-- 7:
select * from bills
where total_amount > 5000;

-- 8:
select * from payments
where payment_mode='UPI';

-- 9:
select * from patients 
where age between 30 and 50;

-- 10:
select * from doctors 
where consultation_fee>800;

-- 11:
select count(*) as Total_patients from patients;

-- 12:
select count(*) as Total_doctors from doctors;

-- 13:
select count(*) as Total_appointments from appointments;

-- 14:
select avg(consultation_fee) as Average_Consultation_Fee from doctors;

-- 15:
select max(treatment_cost) as Highest_treatment_cost from treatments;

-- 16:
select sum(total_amount) as Toatl_Billing_Amount from bills;

-- 17:
select sum(total_amount) as Toatl_Paid_Amount from bills
where bill_status='Paid';

-- 18:
select city,count(*) from patients
group by city;

-- 19:
select specialization,count(*) from doctors
group by specialization;

-- 20:
select appointment_status,count(*) from appointments
group by appointment_status;

-- 21:
select 
	p.patient_name,
    a.appointment_date,
    a.appointment_status from patients p
join appointments a 
on a.patient_id=p.patient_id;

-- 22:
select 
	d.doctor_name,
    dt.department_name from doctors d
join departments dt 
on d.department_id =dt.department_id;

-- 23:
select p.patient_name,
       d.doctor_name,
       a.appointment_date
from appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id;

-- 24:
select 
	a.appointment_id,
    t.treatment_name,
    t.treatment_cost
    from appointments a 
join treatments t 
on a.appointment_id=t.appointment_id;

-- 25:
select
	p.patient_name,
    b.bill_id,
    b.total_amount from patients p 
left join bills b
on p.patient_id=b.patient_id;

-- 26:
select
	b.bill_id,
    p.payment_mode,
    p.paid_amount,
    p.payment_status from payments p
right join bills b 
on p.bill_id=b.bill_id;

-- 27:
select p.patient_name,
       d.doctor_name,
       dp.department_name,
       a.appointment_date,
       a.appointment_status,
       t.treatment_name,
       t.treatment_cost,
       b.total_amount,
       py.payment_status
from appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
left join treatments t on a.appointment_id = t.appointment_id
left join bills b on a.appointment_id = b.appointment_id
left join payments py on b.bill_id = py.bill_id;

-- 28:
select doctor_id,
       count(*) as total_appointments
from appointments
group by doctor_id;

-- 29:
select dp.department_name,
       count(*) as total_appointments
FROM appointments a
join doctors d
on a.doctor_id = d.doctor_id
join departments dp
on d.department_id = dp.department_id
group by dp.department_name;

-- 30:
select dp.department_name,
       sum(b.total_amount) as revenue
from bills b
join appointments a on b.appointment_id = a.appointment_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
group by dp.department_name;

-- 31:
select treatment_name,
       sum(treatment_cost) as Total_cost
from treatments
group by treatment_name;

-- 32:
select p.city,
       sum(b.total_amount) as total_billing
from bills b
join patients p on b.patient_id = p.patient_id
group by p.city;

-- 33:
select doctor_id,count(*) as total_appointments
from appointments
group by doctor_id
having count(*) > 2;

-- 34:
select dp.department_name,sum(b.total_amount) as revenue
from bills b
join appointments a on b.appointment_id = a.appointment_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
group by dp.department_name
having sum(b.total_amount) > 20000;

-- 35:
select city,count(*) as patient_count
from patients
group by city
having count(*) > 2;

-- 36:
select * from patients
where patient_id in(
    select patient_id
    from appointments
);

-- 37:
select * from patients
where patient_id not in(
    select patient_id
    from appointments
);

-- 38:	
select * from doctors
where doctor_id not in(
    select doctor_id
    from appointments
);

-- 39:
select * from bills
where total_amount >(
    select avg(total_amount)
    from bills
);

-- 40:
select p.patient_name,
       b.total_amount from patients p
join bills b on p.patient_id = b.patient_id
where b.total_amount =(
    select max(total_amount)
    from bills
);

-- 41:
select * from doctors
where consultation_fee >(
    select avg(consultation_fee)
    from doctors
);

-- 42:
select distinct p.* from patients p
join appointments a on p.patient_id = a.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
where dp.department_name = 'Cardiology';

-- 43:
select * from bills
where bill_status = 'Unpaid';

-- 44:
select * from appointments
where appointment_id in (
    select appointment_id
    from treatments
);

-- 45:
select patient_id,sum(total_amount) as total_bill
from bills
group by patient_id
having sum(total_amount) > (
    select avg(total_bill)
    from(
        select sum(total_amount) as total_bill
        from bills
        group by patient_id
    ) x
);

-- 46:
select * from appointments
where appointment_id not in (
    select appointment_id
    from treatments
);

-- 47:
select * from bills
where bill_id not in (
    select bill_id
    from payments
);

-- 48:
select * from payments
where paid_amount is null
or paid_amount = 0;

-- 49:
select a.*,b.bill_id from appointments a
join bills b
on a.appointment_id = b.appointment_id
where a.appointment_status = 'Cancelled';

-- 50:
select b.bill_id,
       b.total_amount,
       p.paid_amount from bills b
join payments p on b.bill_id = p.bill_id
where p.payment_status = 'Paid'
and p.paid_amount < b.total_amount;

-- 51:
select * from doctors
where department_id not in(
    select department_id
    from departments
);

-- 52:
select * from appointments
where patient_id not in(
    select patient_id
    from patients
)
or doctor_id not in (
    select doctor_id
    from doctors
);


-- Final Patient Billing Report:
select
    p.patient_name,
    p.city,
    count(a.appointment_id) as total_appointments,
    ifnull(sum(b.total_amount),0) as total_bill_amount,
    ifnull(sum(py.paid_amount),0) as total_paid_amount,
    ifnull(sum(b.total_amount),0) -
    ifnull(sum(py.paid_amount),0) as pending_amount
from patients p
left join appointments a
on p.patient_id = a.patient_id
left join bills b
on p.patient_id = b.patient_id
left join payments py
on b.bill_id = py.bill_id
group by p.patient_id,
         p.patient_name,
         p.city;



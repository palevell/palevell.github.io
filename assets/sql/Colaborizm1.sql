USE patrick;
BEGIN TRANSACTION;

INSERT INTO bios(Name, Degree, Email, LinkedIn, GeoLocation) VALUES (
	'Patrick Levell',
	'BSc. in Computer Information Systems from DeVry University/Chicago',
	'patrick.a.levell@gmail.com',
	'https://www.linkedin.com/in/patricklevell/',
	'Ontario, Canada',
);

INSERT INTO skills(Skill, Experience) VALUES
	('SQL Sever',           '15+ years'),
	('Visual Basic',        '15+ years'),
	('Visual Studio'        '15+ years'),
	('JDE Edwards ERP'      '10+ years'),
	('Java'                 '2 years'),
	('Python'               '2 years');

INSERT INTO Highlights(Project, Description, Keywords ) VALUES
	('Job Master Inquiry', 'Data mining utility for top-level management,
				comparing steel tons sold vs. steel tons fabricated',
				'SQLServer, JDEdwards, VisualBasic, SSAS, MDX'),
	('iWarehouse', 'Fleet management system for lift trucks',
			'SQLServer, OracleEnterpriseOne, JDE, Data Definitions');

INSERT INTO work_history(Title, Employer, Dates) VALUES
	('Freelance IT Guy',            'Self-Employed',                '2012 - present'),
	('Programmer/Analyst',          'Raymond Corporation',          '2007 - 2012),
	('Computer Systems Analyst',    'NUCOR Vulfraft - Florence',    '1997 - 2007');

INSERT INTO introductions(BlockText) VALUES (
	'I am an IT guy with 15+ years experience in manufacturing environments.
	Much of that time has been spent working with database applications like
	J.D. Edwards (aka. Oracle EnterpriseOne) that drive management and decision-support
	systems. By the time stuff lands on my desk, it is usually already over time and
	over budget. Said another way, when people come to me, they have already tried cheaper
	and faster--now, they want it better.'
)

COMMIT;



--
-- Insercion en EXAMEN
--
insert into examen(nombre) values('Simulación UNAM 2012');
insert into examen(nombre) values('Simulación UNAM 2013');
insert into examen(nombre) values('Simulación UNAM 2014');
insert into examen(nombre) values('Simulación UNAM 2015');
insert into examen(nombre) values('Simulación UNAM 2016');
insert into examen(nombre) values('Simulación UNAM 2017');
insert into examen(nombre) values('Simulación UNAM 2018');
insert into examen(nombre) values('Simulación UNAM 2019');
insert into examen(nombre) values('Simulación UNAM 2020');
insert into examen(nombre) values('Simulación UNAM 2021');


--
-- Insercion en  STATUS_EVALUACION
--
insert into status_evaluacion(nombre,descripcion) 
  values('INCONCLUSO','Este estado se da cuando un alumno inicio un examen, pero aún no lo termina de contestar.');
insert into status_evaluacion(nombre,descripcion) 
  values('TERMINADO','Este estado se da cuando un alumno termina de contestar el examen y recibe su puntaje');
insert into status_evaluacion(nombre,descripcion) 
  values('NUNCA','Este estado se da cuando nunca se ha abierto la evaluacion');

--
-- Insercion en MATERIA
--
insert into materia(nombre) values('Matemáticas');
insert into materia(nombre) values('Español');
insert into materia(nombre) values('Física');
insert into materia(nombre) values('Química');
insert into materia(nombre) values('Biología');
insert into materia(nombre) values('Historia Universal');
insert into materia(nombre) values('Historia de México');
insert into materia(nombre) values('Literatura');
insert into materia(nombre) values('Geografía');
insert into materia(nombre) values('Filosofía');

\i pregunta.sql
\i opcion.sql

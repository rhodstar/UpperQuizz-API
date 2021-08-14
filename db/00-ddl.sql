CREATE TABLE alumno(
  alumno_id   serial primary key,
  nombre      varchar(60) not null,
  apellidos   varchar(60) not null,
  correo      varchar(255) unique not null,
  contrasena  varchar(255) not null
);

CREATE TABLE examen(
  examen_id   serial primary key,
  nombre      varchar(60) not null
);

CREATE TABLE status_evaluacion(
  status_evaluacion_id  serial primary key,
  nombre                varchar(40) not null,
  descripcion           varchar(200) not null
);

CREATE TABLE materia(
  materia_id  serial primary key,
  nombre      varchar(60) not null
);

CREATE TABLE pregunta(
  pregunta_id serial primary key,
  texto_pregunta    varchar(2000) not null,
  examen_id   int not null,
  materia_id  int not null,
  foreign key(examen_id) references examen(examen_id),
  foreign key(materia_id) references materia(materia_id)

);

CREATE TABLE opcion(
  opcion_id   serial primary key,
  texto_opcion varchar(2000),
  pregunta_id int not null,
  es_correcta boolean not null,
  foreign key(pregunta_id) references pregunta(pregunta_id)
);

CREATE TABLE evaluacion_alumno(
  evaluacion_id               serial primary key,
  examen_id                   int not null,
  alumno_id                   int not null,
  status_evaluacion_id        int not null,
  num_intento                 int not null,
  aciertos_totales  int,
  fecha_aplicacion  timestamp,
  foreign key(examen_id) references examen(examen_id),
  foreign key(alumno_id) references alumno(alumno_id),
  foreign key(status_evaluacion_id) references status_evaluacion(status_evaluacion_id)
);

CREATE TABLE respuestas_alumno(
  respuestas_alumno_id   serial primary key,
  opcion_id       int not null,
  pregunta_id     int not null,
  evaluacion_id   int not null,
  foreign key(evaluacion_id) references evaluacion_alumno(evaluacion_id),
  foreign key(opcion_id) references opcion(opcion_id),
  foreign key(pregunta_id) references pregunta(pregunta_id),
  unique(evaluacion_id,pregunta_id)
);

CREATE TABLE puntaje_materia(
  materia_id      int not null,
  evaluacion_id   int not null,
  puntaje         int not null,
  foreign key(evaluacion_id) references evaluacion_alumno(evaluacion_id),
  foreign key(materia_id) references materia(materia_id)
);

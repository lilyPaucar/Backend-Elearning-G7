create database vacunaciones;
use vacunaciones;
-- crear una tabla llamada vacunas en la cual tengamos las siguientes columnas:
-- el id sera numerico y sera autoincrementable y primary key
-- el nombre de la vacuna que sera hasta 100 caracteres:
-- el pais de procedencis que sera hasta 20 caracteres:
-- el lote sera de 6 caracteres

create table vacuna(
id INT auto_increment primary key,
NOMBRE varchar(100) unique not null,  		-- unique es para que los valores nose repitan
pais varchar(20) not null,  -- not null para que vaye si o si un dato y no dejarlo vacio
lote char(6)
);

insert into vacuna(id,nombre,pais,lote) values
					(default, 'pfizer','eeuu','123abc'),
                    (default,'sputnik', 'rusa', '3d3afg'),
                    (default,'astrazeneca','china','234oiu'),
                    (default,'chinopharm','china','5678rg'),
                    (default,'jhonson & jhonson','eeuu','h675hh');

-- devolver todas las vacunas que tengan id 3
select *from vacuna where id=3;
-- devolver todas las vacunas que sean hechas en china
select * from vacuna where pais= 'china';
-- devolver todas las vacunas que en su nombre twngan un espacio
select* from vacuna where nombre like '% %';
-- devolver todas las vacunas que tengan como tercer caracter la letra ´i´ y como 5to la letra 'o'
select *from vacuna where  nombre like '__i_o%';

-- id primary key entero
-- direccion hasta 100 caracteres
-- numero numeral no puede ser nulo
-- atencion_preferencial booleano no puede ser nulo
-- latitud decimal de 2 enteros y 2 flotantes
-- longitud decimal de 2 enteros y 2 flotantes
create table vacunatorios(
-- columnas propias de la tabla
id int primary key,
direccion varchar(100),
numero int not null,
atencion_preferencial boolean not null default true,
latitud float(4,2),
longitud float(4,2),
-- columnas que van a cumplir como relaciones
-- las columnas que van a hacer relaciones deben usar el siguiente formato:
-- nombre_de_la_tabla_columna
vacuna_id int,

-- relaciones
foreign key (vacuna_id) references vacuna(id)
);
alter table vacunatorios drop column id; -- eliminar la columna id porque no pusimos autoincrementable 
alter table vacunatorios add column id int auto_increment primary key first; -- agregamos la columna id con sus propiedades y ponemos q comience primero

INSERT INTO VACUNATORIOS (id, direccion, numero, atencion_preferencial, latitud, longitud, vacuna_id) VALUES 
                         (DEFAULT, 'CALLE LOS PALITOS', 123, TRUE, 10.53, 14.80, 1),
                         (DEFAULT, 'AV GIRASOL', 1213, FALSE, 12.53, 19.80, 1),
                         (DEFAULT, 'HOSP. GNRAL.', 111, DEFAULT, 12.49, 80.15, 2),
                         (DEFAULT, 'POSTA CERRO 7 COLORES', 1485, DEFAULT, 10.53, 14.80, 3),
                         (DEFAULT, 'ESTADIO LOS AGUATEROS', 1489, FALSE, 20.52, 18.10, 4),
                         (DEFAULT, 'PLAZA DE ARMAS', 1256, FALSE, 12.54, 17.26, 4);

-- devolver la direcciones y sus numeros  que tenga atencion preferencial 
select direccion, numero from vacunatorios where atencion_preferencial= true;
-- devolver las direcciones que se encuentren entre let >20.00 y long <20.00 
select direccion from vacunatorios where latitud >20.00 and longitud <20.00;
-- devolver las direcciones que sean pfizer y que tengan atenvion pregferencial
select direccion from vacunatorios where vacuna_id =1 and atencion_preferencial=true;
-- deolver las direcciones cuyas vacuna no sea pfizer o tengan atencion preferencial
select direccion from vacunatorios where  vacuna_id != 1 or atencion_preferencial=false;
CREATE TABLE Categoria(
	id INT PRIMARY KEY NOT NULL,
	nombre TEXT
);
CREATE TABLE Producto(
	id INT PRIMARY KEY NOT NULL,
	nombre TEXT,
	marca TEXT,
	categoria_id INT,
	precio_unitario REAL
);
CREATE TABLE Stock(
	id INT PRIMARY KEY NOT NULL,
	sucursal_id INT NOT NULL,
	producto_id INT NOT NULL,
	cantidad INT,
	UNIQUE(sucursal_id, producto_id)
);
CREATE TABLE Cliente(
	id INT PRIMARY KEY NOT NULL,
	nombre TEXT,
	telefono INT
);
CREATE TABLE Orden(
	id INT PRIMARY KEY NOT NULL,
	cliente_id INT,
	sucursal_id INT,
	fecha TEXT,
	total REAL
);
CREATE TABLE Item(
	id INT PRIMARY KEY NOT NULL,
	orden_id INT,
	producto_id INT,
	cantidad INT,
	monto_venta REAL
);
CREATE TABLE Sucursal(
	id INT PRIMARY KEY NOT NULL,
	nombre TEXT,
	direccion TEXT
);

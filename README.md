\# ABP \- Evidencia 6  
\# Team Ramona

\#\# Propósito  
El objetivo de esta entrega es mostrar el uso práctico de consultas SQL dentro del proyecto general SmartHome Solutions. El trabajo consiste en crear un script que cargue información en la base de datos y permite realizar diferentes tipos de consultas, tanto simples como multitabla y con subconsultas, relacionadas con el funcionamiento del sistema de domótica desarrollado durante el módulo.

\#\# Contexto  
Este trabajo forma parte del Módulo Programador y se vincula directamente con el sistema de SmartHome, una aplicación que permite controlar y automatizar distintos dispositivos dentro de una vivienda. Desde este módulo se busca que el programa funcione con una base de datos relacional, respetando el modelo diseñado en las evidencias anteriores y conectándose mediante el patrón DAO. Las tablas creadas representan usuarios, viviendas, dispositivos, rutinas e historiales, simulando datos reales que se usarían dentro del sistema.

\#\# Alcance  
El script de esta evidencia incluye:  
\- Inserción de datos iniciales en cada tabla (mínimo 10 registros).  
\- Consultas simples para verificar el contenido de cada tabla.  
\- Consultas multitabla (JOIN) con sentido dentro del negocio, como por ejemplo: ver los dispositivos que tiene cada usuario, las rutinas activas o los últimos eventos registrados.  
\- Subconsultas con fines prácticos, como detectar usuarios con más dispositivos o equipos sin rutinas configuradas.

Todo el contenido se encuentra dentro de la carpeta del repositorio llamada: [Abp-Programación-Team-Ramona/abp\_programacion\_2](https://github.com/Abp-Programacion-Team-Ramona/abp_programacion_2)

\#\# Autores  
\- Candela Esperanza Blanco  
\- Luz Ottero Grion    
\- Diego Germán Mendia    
\- Marco Remon    
\- Nicolas Oggero    
\- Benjamín Siri  

Instituto Superior Politécnico Córdoba (ISPC)    
Tecnicatura Superior en Desarrollo de Software – Módulo Programador

\#\# Cómo ejecutar el script online

\#\#\# Opción 1 – OneCompiler (recomendado)  
1\. Entrar a https://onecompiler.com/mysql    
2\. Seleccionar MySQL como lenguaje.    
3\. Borrar el contenido que aparece por defecto.    
4\. Pegar el contenido completo del archivo “queries.sql”..    
5\. Presionar Run para ejecutar.

El sitio mostrará los resultados de las consultas y confirmará que las tablas fueron creadas correctamente.

\#\# Requisitos técnicos  
\- Motor de base de datos: MySQL  
\- Compatible con cualquier DBMS online.    
\- No requiere instalación ni configuración local.

\#\# Resultado esperado  
Al ejecutar el script se puede:  
\- Ver la creación de todas las tablas del sistema.  
\- Insertar los datos de ejemplo en cada una.  
\- Ejecutar las consultas que muestran información útil para la aplicación, como:  
  \- Usuarios y viviendas registradas.  
  \- Dispositivos y su estado.  
  \- Rutinas activas o inactivas.  
  \- Historial de eventos y configuraciones de los aires acondicionados.

Este trabajo representa la última parte del módulo y completa la integración entre la lógica del programa y la base de datos del proyecto Smart Home.

Año: 2025    
Materia: Módulo Programador – Evidencia 6    
Proyecto: SmartHome Solutions


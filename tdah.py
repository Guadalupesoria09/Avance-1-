Algoritmo test_TDAH

     definir preg1,preg2,preg3,preg4,preg5,preg6,preg7,preg8,preg9,preg10
     
     Escribir"1.Con frecuencia falla en PRESTAR la debida atencion a los detalles o por descuido se cometen errores en las tareas escolares, en el trabajo o durante otras actividades (por ejemplo, se pasan por alto o se pierden detalles, el trabajo no se lleva a cabo con precision)";
    
     Leer preg1;
     
     Si preg1="si"Entonces
        
        Escribir"2.Con frecuencia tiene dificultades para mantener la atencion en tareas o actividades recreativas (por ejemplo, tiene dificultad para mantener la atencion en clases, conversaciones o lectura prolongada)";
        
        Leer preg2;
      
      SiNo
      
         Si preg2="si"Entonces
         
         Escribir"3.Con frecuencia parece no escuchar cuando se le habla directamente (por ejemplo, parece tener la mente en otras cosas, incluso en ausencia de cualquier distraccion aparente)";
         
         Leer preg3;
         
          SiNo
      
               Si preg3="si"Entonces
          
                Escribir"4.Con frecuencia no sigue las INSTRUCCIONES y no termina las tareas escolares, los quehaceres o los deberes laborales (por ejemplo, inicia tareas pero se distrae rapidamente y se evade con facilidad)";
              
                Leer preg4;
              
              SiNo
      
                  Si preg4="si"Entonces
          
                  Escribir"5.Con frecuencia tiene dificultad para organizar tareas y actividades (por ejemplo, dificultad para gestionar tareas secuenciales; dificultad para poner los materiales y pertenencias en orden; descuido y desorganizacion en el trabajo; mala gestion del tiempo; no cumple los plazos)";
              
                 Leer preg5;
              
                    SiNo
       
                      Si preg5="si"Entonces
          
                       Escribir"6.Con frecuencia evita, le disgusta o se muestra poco entusiasta en INICIAR tareas que requieren un esfuerzo mental sostenido (por ejemplo tareas escolares o quehaceres domesticos; en adolescentes mayores y adultos, preparacion de informes, completar formularios, revisar articulos largos)";
             
                      Leer preg6;
             
                      SiNo
       
                          Si preg6="si"Entonces
         
                          Escribir"7.Con frecuencia pierde cosas necesarias para tareas o actividades (por ejemplo, materiales escolares, lapices, libros, instrumentos, billetero, llaves, papeles de trabajo, gafas, movil)";
              
                          Leer preg7;
              
                          SiNo
       
                              Si preg7="si"Entonces
                     
                              Escribir"8.Con frecuencia se distrae con facilidad por estimulos externos (para adolescentes mayores y adultos, puede incluir pensamientos no relacionados)";
              
                               Leer preg8;
              
                              SiNo 
       
                                  Si preg8="si"Entonces
          
                                 Escribir"9.Con frecuencia olvida las actividades cotidianas (por ejemplo, hacer las tareas, hacer las diligencias; en adolescentes mayores y adultos, devolver las llamadas, pagar las facturas, acudir a las citas)";
              
                                 Leer preg9;
              
                                 SiNo
       
                                       Si preg9="si"Entonces
          
                                       Escribir"10.Con frecuencia juguetea o golpea con las manos o los pies o se retuerce en el asiento";
              
                                       Leer preg10;
              
                                       SiNo
       
                                          Si preg10="si"Entonces
         
                                         Leer Si >=7"si"Entonces
             
                                         Escribir"Requieres diagnostico profecional, acude con especialista";
             
                                           SiNo
        
                                               Leer Si<7"si"Entinces
            
                                              Escribir"Gracias por tomar el test";
             
                                             FinSi
                                        FinSi
                                    FinSi    
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinProceso                       
